#!/usr/bin/env python3
"""
assignment6.py

Standalone script version of Lab 6: Evaluation of Vulnerability Analysis Tools using CWE-based Comparison
Targets the selected tools: PVS-Studio (commercial - CWE mapping), StaticReviewer (commercial - CWE), cwe_checker (open source - CWE-focused).

Usage examples:
  - Prepare directories:
      python assignment6.py prepare
  - Clone repos (uses PROJECTS mapping):
      python assignment6.py clone
  - (Optional) Run cwe_checker on a binary (if installed and binary available):
      python assignment6.py run-cwechecker --project synology_hdd_db --target repos/synology_hdd_db/some_binary
  - Aggregate findings (parses raw outputs placed in RAW_OUTPUT_DIR):
      python assignment6.py aggregate
  - Show coverage & IoU report:
      python assignment6.py report

Notes:
 - PVS‑Studio and StaticReviewer are commercial products. Run them externally (or via their CLI/service) and place their output files into RAW_OUTPUT_DIR using the naming convention:
       <project_label>__<toolname>.<ext>
   e.g. repos outputs: repos/synology_hdd_db__pvs-studio.sarif
 - cwe_checker analyzes binaries. If you can produce binaries for a project, you can run cwe_checker and save its JSON output using the naming convention:
       repos/synology_hdd_db__cwe_checker.json
 - Supported input formats: JSON (including SARIF), XML, CSV. The script contains robust parsers to extract CWE IDs from these formats.

"""

import subprocess
import json
import csv
import xml.etree.ElementTree as ET
import re
from collections import Counter
import argparse
import datetime as dt
import sys
import math
import os
from pathlib import Path

try:
    import pandas as pd
except Exception:
    pd = None

# ----------------------- PARAMETERS (Edit me) -----------------------
PROJECTS = {
    'dl-art-school': 'repos/dl-art-school',   # 152334h/dl-art-school
    'two1-python': 'repos/two1-python',       # 21dotco/two1-python
    'instructor': 'repos/instructor',         # 567-labs/instructor
}

# Selected tools for the assignment (identifiers used in filenames)
TOOLS = [
    'codeql',       # CodeQL produces SARIF with CWE tags for Python rules
    'semgrep',      # Semgrep rules can include CWE metadata; use python ruleset
    'sonarqube',    # SonarQube/SonarScanner for Python; export JSON or SARIF with CWE
    'bandit',       # Bandit (OpenStack) Python security linter with CWE metadata in JSON
    'detect-secrets', # Yelp detect-secrets for hardcoded credentials mapped to CWE-798
    'dlint',        # Dlint (flake8 plugin) security checks; we'll map messages to CWEs
]

RAW_OUTPUT_DIR = Path('raw_tool_outputs')
RAW_OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
CONSOLIDATED_CSV = Path('cwe_findings_consolidated.csv')
CWE_TOP25_FILE = Path('cwe_top25_2024.txt')
MIN_SEVERITY = None  # placeholder
RUN_TIMESTAMP = dt.datetime.now(dt.UTC).isoformat()

# ----------------------- Utilities -----------------------

def run_cmd(cmd, capture=False, check=False):
    print('RUN:', ' '.join(cmd))
    return subprocess.run(cmd, capture_output=capture, text=True, check=check)

# ----------------------- CWE helpers & parsers -----------------------

def normalize_cwe(raw_cwe: str) -> str:
    if not raw_cwe:
        return None
    raw_cwe = str(raw_cwe).strip()
    # Extract numeric portion and strip leading zeros so CWE-094 -> CWE-94
    m = re.search(r'(?:CWE-?)(\d+)', raw_cwe, re.IGNORECASE)
    if m:
        try:
            num = int(m.group(1))
            return f'CWE-{num}'
        except Exception:
            return f'CWE-{m.group(1).lstrip("0") or m.group(1)}'
    if raw_cwe.isdigit():
        try:
            return f'CWE-{int(raw_cwe)}'
        except Exception:
            return f'CWE-{raw_cwe.lstrip("0") or raw_cwe}'
    if raw_cwe.lower().startswith('cwe-'):
        suffix = raw_cwe.split('-',1)[1]
        try:
            return f'CWE-{int(suffix)}'
        except Exception:
            return f'CWE-{suffix.lstrip('0') or suffix}'
    return None


def load_cwe_top25(path=CWE_TOP25_FILE):
    if path.exists():
        raw = path.read_text().strip().splitlines()
        ids = {line.strip() for line in raw if line.strip()}
        print(f"Loaded {len(ids)} CWE IDs from {path}")
        return ids
    else:
        placeholder = [
            'CWE-787','CWE-79','CWE-89','CWE-20','CWE-125','CWE-78','CWE-416','CWE-22','CWE-352','CWE-434',
            'CWE-862','CWE-476','CWE-287','CWE-190','CWE-502','CWE-77','CWE-306','CWE-119','CWE-200','CWE-269',
            'CWE-94','CWE-863','CWE-918','CWE-276','CWE-611',
        ]
        print('Using embedded placeholder Top 25 list (replace with official list).')
        return set(placeholder)

CWE_TOP25 = load_cwe_top25()

# ---- Parsers (CodeQL SARIF + Semgrep-like JSON + generic JSON/XML/CSV)

def parse_codeql_sarif(path, tool_name, project):
    data = json.loads(Path(path).read_text())
    rule_cwe = {}
    for run in data.get('runs', []):
        driver = run.get('tool', {}).get('driver', {})
        for rule in driver.get('rules', []) if isinstance(driver.get('rules', []), list) else []:
            rid = rule.get('id') or rule.get('name') or (rule.get('shortDescription') or {}).get('text')
            props = rule.get('properties', {}) or {}
            tags = props.get('tags') or []
            if isinstance(tags, str):
                tags = [tags]
            found = None
            for t in tags:
                if not isinstance(t, str):
                    continue
                m = re.search(r'(CWE-?\d+)', t, re.IGNORECASE)
                if m:
                    found = normalize_cwe(m.group(1))
                    break
            if not found:
                if 'cwe' in props:
                    found = normalize_cwe(props.get('cwe'))
                elif 'CWE' in props:
                    found = normalize_cwe(props.get('CWE'))
                elif props.get('cwes'):
                    c = props.get('cwes')
                    if isinstance(c, (list, tuple)) and c:
                        found = normalize_cwe(c[0])
            if found and rid:
                rule_cwe[rid] = found
    out = []
    for run in data.get('runs', []):
        for res in run.get('results', []):
            cwe = None
            props = res.get('properties', {}) or {}
            if 'cwe' in props:
                cwe = normalize_cwe(props.get('cwe'))
            if not cwe:
                rid = res.get('ruleId') or (res.get('rule', {}) or {}).get('id')
                if rid and rid in rule_cwe:
                    cwe = rule_cwe[rid]
            if not cwe:
                blob = json.dumps(res)
                m = re.search(r'(?:CWE-?)(\d+)', blob, re.IGNORECASE)
                if m:
                    cwe = f'CWE-{m.group(1)}'
            if cwe:
                out.append({'tool': tool_name, 'project': project, 'cwe_id': cwe})
    return out


def parse_semgrep_json(path, tool_name, project):
    data = json.loads(Path(path).read_text())
    out = []
    for r in data.get('results', []):
        cwe = None
        extra = r.get('extra', {}) or {}
        meta = extra.get('metadata') or {}
        if meta:
            cwe_field = meta.get('cwe') or meta.get('CWE') or meta.get('cwe_id')
            if cwe_field:
                if isinstance(cwe_field, (list, tuple)) and cwe_field:
                    cwe = normalize_cwe(cwe_field[0])
                else:
                    cwe = normalize_cwe(cwe_field)
        if not cwe:
            check_id = r.get('check_id') or ''
            m = re.search(r'(CWE-?\d+)', str(check_id), re.IGNORECASE)
            if m:
                cwe = normalize_cwe(m.group(1))
        if not cwe:
            blob = json.dumps(r)
            m = re.search(r'(?:CWE-?)(\d+)', blob, re.IGNORECASE)
            if m:
                cwe = f'CWE-{m.group(1)}'
        if cwe:
            out.append({'tool': tool_name, 'project': project, 'cwe_id': cwe})
    return out


def parse_tool_json_generic(path, tool_name, project):
    data = json.loads(Path(path).read_text())
    out = []
    candidates = []
    if isinstance(data, dict):
        if 'findings' in data and isinstance(data['findings'], list):
            candidates = data['findings']
        elif 'results' in data and isinstance(data['results'], list):
            candidates = data['results']
        else:
            candidates = [data]
    elif isinstance(data, list):
        candidates = data
    for item in candidates:
        cwe = None
        if isinstance(item, dict):
            for k in ('cwe','cwe_id','CWE','CWE_ID'):
                v = item.get(k)
                if v:
                    if isinstance(v, (list,tuple)) and v:
                        cwe = normalize_cwe(v[0])
                    else:
                        cwe = normalize_cwe(v)
                    break
            if not cwe:
                blob = json.dumps(item)
                m = re.search(r'(?:CWE-?)(\d+)', blob, re.IGNORECASE)
                if m:
                    cwe = f'CWE-{m.group(1)}'
        else:
            blob = str(item)
            m = re.search(r'(?:CWE-?)(\d+)', blob, re.IGNORECASE)
            if m:
                cwe = f'CWE-{m.group(1)}'
        if cwe:
            out.append({'tool': tool_name, 'project': project, 'cwe_id': cwe})
    return out


def parse_tool_xml_generic(path, tool_name, project):
    root = ET.parse(path).getroot()
    out = []
    for elem in root.iter():
        for v in elem.attrib.values():
            m = re.search(r'(?:CWE-?)(\d+)', v, re.IGNORECASE)
            if m:
                out.append({'tool': tool_name, 'project': project, 'cwe_id': f'CWE-{m.group(1)}'})
        if elem.text:
            m = re.search(r'(?:CWE-?)(\d+)', elem.text, re.IGNORECASE)
            if m:
                out.append({'tool': tool_name, 'project': project, 'cwe_id': f'CWE-{m.group(1)}'})
    return out


def parse_tool_csv_generic(path, tool_name, project):
    out = []
    with open(path, newline='') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            cwe = row.get('cwe') or row.get('cwe_id') or row.get('CWE') or row.get('CWE_ID')
            if cwe:
                c = normalize_cwe(cwe)
                if c:
                    out.append({'tool': tool_name, 'project': project, 'cwe_id': c})
                    continue
            blob = json.dumps(row)
            m = re.search(r'(?:CWE-?)(\d+)', blob, re.IGNORECASE)
            if m:
                out.append({'tool': tool_name, 'project': project, 'cwe_id': f'CWE-{m.group(1)}'})
    return out

def map_dlint_message_to_cwe(message: str) -> str | None:
    msg = message.lower()
    # Best-effort mappings to Top-25 CWEs
    if 'yaml.load' in msg or 'pickle' in msg or 'marshal' in msg:
        return 'CWE-502'  # Deserialization of untrusted data
    if ('subprocess' in msg or 'popen' in msg or 'os.system' in msg) and ('shell=true' in msg or 'shell=' in msg or 'system' in msg):
        return 'CWE-78'   # OS Command Injection
    if 'eval(' in msg or 'exec(' in msg or "builtins.__import__" in msg:
        return 'CWE-94'   # Code Injection
    if 'md5' in msg or 'sha1' in msg or 'weak hash' in msg:
        return 'CWE-327'  # Broken/weak crypto
    if 'telnetlib' in msg or 'ftplib' in msg:
        return 'CWE-319'  # Cleartext transmission
    if ('xml' in msg and ('entity' in msg or 'xxe' in msg or 'external' in msg)):
        return 'CWE-611'  # XXE
    if 'jinja2' in msg or 'mark_safe' in msg or 'autoescape' in msg:
        return 'CWE-79'   # XSS
    if 'input(' in msg and ('python 2' in msg or 'py2' in msg or 'unsafe' in msg):
        return 'CWE-94'
    if 'path traversal' in msg or 'path join' in msg or 'os.path' in msg:
        return 'CWE-22'   # Path traversal
    return None

def parse_dlint_text(path, tool_name, project):
    """Parse flake8+dlint plain text output lines: 'file:line:col: CODE message'.
    Map messages to CWEs using heuristics above.
    """
    out = []
    for line in Path(path).read_text(errors='ignore').splitlines():
        # Expect format: path:row:col: CODE message
        parts = line.split(':', 3)
        if len(parts) < 4:
            continue
        msg = parts[3].strip()
        cwe = map_dlint_message_to_cwe(msg)
        if cwe:
            out.append({'tool': tool_name, 'project': project, 'cwe_id': cwe})
    return out

def parse_bandit_json(path, tool_name, project):
    """Parse Bandit JSON output to extract CWE IDs.
    Bandit JSON typically contains 'results' where each result may have 'issue_confidence',
    'issue_severity', 'test_id', 'test_name', and optionally 'cwe' or 'more_info' with CWE references.
    We'll look for 'cwe' fields (Bandit>=1.7 sometimes includes) and otherwise regex CWE patterns
    in 'more_info' and the entire result blob.
    """
    data = json.loads(Path(path).read_text())
    results = data.get('results') or data.get('issues') or []
    out = []
    # Common Bandit test_id -> CWE mapping (best-effort, not exhaustive)
    id_to_cwe = {
        'B102': 'CWE-94',   # exec used
        'B307': 'CWE-94',   # eval used
        'B301': 'CWE-502',  # pickle
        'B302': 'CWE-502',  # marshal (unsafe deserialization-like)
        'B405': 'CWE-502',  # import pickle
        'B408': 'CWE-502',  # yaml load (unsafe)
        'B602': 'CWE-78',   # subprocess with shell=True
        'B603': 'CWE-78',   # subprocess call
        'B604': 'CWE-78',   # any function with shell=True
        'B605': 'CWE-78',   # start process with a shell
        'B606': 'CWE-78',   # start process no shell (potential command injection)
        'B607': 'CWE-428',  # partial path (not Top 25 but map anyway)
        'B611': 'CWE-611',  # XML external entities
        'B406': 'CWE-611',  # import xml.etree.cElementTree
        'B407': 'CWE-611',  # import xml.etree.ElementTree
        'B303': 'CWE-327',  # md5
        'B304': 'CWE-327',  # insecure ciphers
        'B305': 'CWE-327',  # insecure cipher modes
        'B311': 'CWE-338',  # random used for security
        'B401': 'CWE-319',  # telnetlib
        'B402': 'CWE-319',  # ftplib
        'B701': 'CWE-79',   # jinja2 autoescape off
        'B702': 'CWE-79',   # mark_safe misuse
        'B608': 'CWE-89',   # hardcoded SQL expression
    }
    for r in results:
        cwe = None
        # Some Bandit outputs include {'cwe': {'id': 78, 'link': '...', 'name': 'OS Command Injection'}}
        cw = r.get('cwe') or r.get('CWE')
        if isinstance(cw, dict):
            cid = cw.get('id') or cw.get('ID') or cw.get('cwe_id')
            cwe = normalize_cwe(cid) if cid is not None else None
        elif cw:
            cwe = normalize_cwe(cw)
        # Fallback to mapping by test_id
        if not cwe:
            tid = r.get('test_id') or r.get('testId') or r.get('id')
            if isinstance(tid, str) and tid.upper() in id_to_cwe:
                cwe = id_to_cwe[tid.upper()]
        if not cwe:
            mi = r.get('more_info') or r.get('more-info') or ''
            m = re.search(r'(?:CWE-?)(\d+)', str(mi), re.IGNORECASE)
            if m:
                cwe = f"CWE-{m.group(1)}"
        if not cwe:
            blob = json.dumps(r)
            m = re.search(r'(?:CWE-?)(\d+)', blob, re.IGNORECASE)
            if m:
                cwe = f"CWE-{m.group(1)}"
        if cwe:
            out.append({'tool': tool_name, 'project': project, 'cwe_id': cwe})
    return out

def parse_detect_secrets_json(path, tool_name, project):
    """Parse detect-secrets JSON baseline or scan output and map to CWE-798 (Use of Hard-coded Credentials).
    detect-secrets outputs either a baseline with {'results': {file: [secrets...]}} or a findings list.
    We'll count each secret finding as CWE-798.
    """
    data = json.loads(Path(path).read_text())
    out = []
    cwe = 'CWE-798'
    if isinstance(data, dict) and 'results' in data and isinstance(data['results'], dict):
        for file, findings in data['results'].items():
            if not isinstance(findings, list):
                continue
            for _ in findings:
                out.append({'tool': tool_name, 'project': project, 'cwe_id': cwe})
    elif isinstance(data, dict) and 'results' in data and isinstance(data['results'], list):
        for _ in data['results']:
            out.append({'tool': tool_name, 'project': project, 'cwe_id': cwe})
    elif isinstance(data, list):
        for _ in data:
            out.append({'tool': tool_name, 'project': project, 'cwe_id': cwe})
    else:
        blob = json.dumps(data)
        # if any secret-like indicator exists, still map one finding conservatively
        if re.search(r'secret|credential|password|api[_-]?key', blob, re.IGNORECASE):
            out.append({'tool': tool_name, 'project': project, 'cwe_id': cwe})
    return out

# ----------------------- Aggregation & Analysis -----------------------

def collect_all_findings():
    all_records = []
    current_projects = set(PROJECTS.keys())
    for path in RAW_OUTPUT_DIR.iterdir():
        if not path.is_file():
            continue
        name = path.name
        try:
            project, tool_and_ext = name.split('__', 1)
            tool_name, ext = tool_and_ext.rsplit('.', 1)
        except ValueError:
            continue
        # Skip outputs for projects that are not part of the current selection
        if project not in current_projects:
            continue
        # Skip tools that are not part of the active selection
        if tool_name not in TOOLS:
            continue
        ext = ext.lower()
        # route to tool-specific parser where appropriate
        if tool_name in ('pvs-studio','codeql') and ext in ('json','sarif'):
            parsed = parse_codeql_sarif(path, tool_name, project)
        elif tool_name == 'staticreviewer' and ext in ('json','xml'):
            # assume JSON/XML from product; fall back to generic
            if ext == 'json':
                parsed = parse_tool_json_generic(path, tool_name, project)
            else:
                parsed = parse_tool_xml_generic(path, tool_name, project)
        elif tool_name == 'semgrep' and ext == 'json':
            parsed = parse_semgrep_json(path, tool_name, project)
        elif tool_name == 'bandit' and ext == 'json':
            parsed = parse_bandit_json(path, tool_name, project)
        elif tool_name == 'detect-secrets' and ext == 'json':
            parsed = parse_detect_secrets_json(path, tool_name, project)
        elif tool_name == 'sonarqube' and ext in ('json','sarif'):
            # Some SonarQube exports include CWE in rule metadata; try generic JSON or SARIF mapping
            parsed = parse_tool_json_generic(path, tool_name, project)
        elif tool_name == 'cwe_checker' and ext == 'json':
            parsed = parse_tool_json_generic(path, tool_name, project)
        elif tool_name == 'dlint' and ext in ('txt','log','out'):
            parsed = parse_dlint_text(path, tool_name, project)
        
        else:
            if ext == 'json':
                parsed = parse_tool_json_generic(path, tool_name, project)
            elif ext == 'xml':
                parsed = parse_tool_xml_generic(path, tool_name, project)
            elif ext == 'csv':
                parsed = parse_tool_csv_generic(path, tool_name, project)
            else:
                parsed = []
        all_records.extend(parsed)
    return all_records


def aggregate_and_write_csv(records):
    counts = Counter((r['project'], r['tool'], r['cwe_id']) for r in records)
    rows = []
    for (project, tool, cwe_id), n in counts.items():
        rows.append({
            'Project_name': project,
            'Tool_name': tool,
            'CWE_ID': cwe_id,
            'Number_of_Findings': n,
            'Is_In_CWE_Top_25?': 'Yes' if cwe_id in CWE_TOP25 else 'No'
        })
    if pd:
        df = pd.DataFrame(rows)
        if not df.empty:
            df.sort_values(['Project_name','Tool_name','CWE_ID'], inplace=True)
            df.to_csv(CONSOLIDATED_CSV, index=False)
            print(f'Wrote consolidated CSV -> {CONSOLIDATED_CSV}')
            print(df.head())
        else:
            print('No findings to write.')
    else:
        # fallback: write CSV manually
        if rows:
            keys = rows[0].keys()
            with open(CONSOLIDATED_CSV, 'w', newline='') as fh:
                writer = csv.DictWriter(fh, fieldnames=keys)
                writer.writeheader()
                writer.writerows(rows)
            print(f'Wrote consolidated CSV -> {CONSOLIDATED_CSV}')
        else:
            print('No findings to write.')


def compute_coverage_and_iou():
    if not CONSOLIDATED_CHECK():
        return
    df = pd.read_csv(CONSOLIDATED_CSV)
    tool_sets = {tool: set(sub['CWE_ID']) for tool, sub in df.groupby('Tool_name')}
    tools_sorted = sorted(tool_sets.keys())
    coverage_rows = []
    for t in tools_sorted:
        unique_count = len(tool_sets[t])
        top25_covered = len([c for c in tool_sets[t] if c in CWE_TOP25])
        # Two coverage views:
        # 1) Top-25 coverage over the Top-25 universe (how many of the Top-25 this tool hits)
        cov_over_top25 = (top25_covered / max(1, len(CWE_TOP25))) * 100
        # 2) Fraction of the tool's unique CWEs that are in Top-25 (friend-style)
        cov_within_tool = (top25_covered / max(1, unique_count)) * 100
        coverage_rows.append({
            'Tool': t,
            'Unique_CWE_Count': unique_count,
            'Top25_Covered': top25_covered,
            'Top25_Coverage_over_Top25_%': round(cov_over_top25, 2),
            'Top25_Fraction_of_Tool_CWEs_%': round(cov_within_tool, 2),
        })
    coverage_df = pd.DataFrame(coverage_rows)
    coverage_df['Top25_Total'] = len(CWE_TOP25)
    print('\nTool coverage:')
    print(coverage_df.sort_values('Unique_CWE_Count', ascending=False))

    # IoU matrix
    matrix = []
    for t1 in tools_sorted:
        row = []
        for t2 in tools_sorted:
            s1, s2 = tool_sets[t1], tool_sets[t2]
            if not s1 and not s2:
                iou = 1.0
            else:
                inter = len(s1 & s2)
                union = len(s1 | s2)
                iou = inter / union if union else 0.0
            row.append(round(iou, 4))
        matrix.append(row)
    iou_df = pd.DataFrame(matrix, index=tools_sorted, columns=tools_sorted)
    print('\nPairwise IoU (Jaccard):')
    print(iou_df)

# small helper to avoid NameError if pandas absent in compute_coverage_and_iou

def CONSOLIDATED_CHECK():
    return CONSOLIDATED_CSV.exists()

# ----------------------- Repo helpers -----------------------

def clone_repos():
    for label, path in PROJECTS.items():
        repo_url = guess_github_url(label)
        target = Path(path)
        if target.exists():
            print(f"Skipping clone for {label}; target exists: {target}")
            continue
        if not repo_url:
            print(f"No guessed URL for {label}; update PROJECTS to include URLs or clone manually.")
            continue
        print(f"Cloning {repo_url} -> {target}")
        run_cmd(['git', 'clone', repo_url, str(target)])


def guess_github_url(label):
    # naive mapping based on the sample labels we used earlier
    mapping = {
        'dl-art-school': 'https://github.com/152334h/dl-art-school.git',
        'two1-python': 'https://github.com/21dotco/two1-python.git',
        'instructor': 'https://github.com/567-labs/instructor.git',
    }
    return mapping.get(label)

# ----------------------- cwe_checker runner (optional) -----------------------

def run_cwe_checker(project_label, target_path, output_filename=None):
    """Attempt to run cwe_checker if available. The tool inspects binaries; target_path should point to a binary file.
    The script makes a best-effort run; if cwe_checker is not installed, it prints the command you should run manually.
    """
    if output_filename is None:
        output_filename = f"{project_label}__cwe_checker.json"
    outpath = RAW_OUTPUT_DIR / output_filename
    if shutil_which('cwe_checker'):
        # CLI usage may vary; user should verify. We'll attempt a JSON output if supported.
        cmd = ['cwe_checker', '--output', str(outpath), str(target_path)]
        print('Running:', ' '.join(cmd))
        try:
            run_cmd(cmd, check=True)
            print('cwe_checker finished; output ->', outpath)
        except Exception as e:
            print('Failed to run cwe_checker automatically:', e)
            print('Run manually and place JSON output at', outpath)
    else:
        print('cwe_checker not found in PATH. To run it manually, install cwe_checker and then run (example):')
        print(f'  cwe_checker --output {outpath} {target_path}')
        print('Then re-run this script with the aggregate step.')


def shutil_which(name):
    from shutil import which
    return which(name) is not None

# ----------------------- Semgrep / CodeQL / SonarQube runners -----------------------

def find_executable(name: str):
    """Return absolute path to executable if available, else None.
    Checks PATH first, then local .venv/bin/ directory."""
    from shutil import which
    p = which(name)
    if p:
        return p
    # try local venv bin
    venv_bin = Path('.venv/bin')
    cand = venv_bin / name
    return str(cand) if cand.exists() and cand.is_file() else None


def run_semgrep_for_project(project_label: str, project_path: str, config: str = None, includes=None, output_filename: str = None):
    semgrep_bin = find_executable('semgrep')
    if not semgrep_bin:
        print('Semgrep not found. Install with pip or system package manager.')
        return False
    cfg = config or 'rules/custom_cwe_rules.yml'
    outname = output_filename or f"{project_label}__semgrep.json"
    outpath = RAW_OUTPUT_DIR / outname
    cmd = [semgrep_bin, '--config', cfg, '--json', '--no-git-ignore']
    if includes:
        for inc in includes:
            cmd += ['--include', inc]
    cmd += [project_path, '--output', str(outpath)]
    try:
        run_cmd(cmd, check=True)
        print('Semgrep output ->', outpath)
        return True
    except Exception as e:
        print('Semgrep failed:', e)
        return False


def run_semgrep_all(config: str = None, includes=None):
    ok = True
    for label, path in PROJECTS.items():
        incs = includes or ['*.py']
        print(f"[semgrep] Scanning {label} at {path} ...")
        ok &= run_semgrep_for_project(label, path, config=config, includes=incs)
    return ok


def run_codeql_for_project(project_label: str, project_path: str, db_dir: Path = None, queries: str = None, output_filename: str = None):
    codeql = find_executable('codeql')
    if not codeql:
        print('CodeQL CLI not found. Install CodeQL and ensure `codeql` is in PATH.')
        return False
    db_root = db_dir or Path('.codeql-db')
    db_root.mkdir(exist_ok=True)
    db = db_root / f"{project_label}-python"
    outname = output_filename or f"{project_label}__codeql.sarif"
    outpath = RAW_OUTPUT_DIR / outname
    # Default query pack for Python; can be adjusted (e.g., security-extended)
    query_pack = queries or 'codeql/python-queries'
    try:
        run_cmd([codeql, 'database', 'create', str(db), '--language=python', '--source-root', project_path, '--overwrite'], check=True)
        run_cmd([codeql, 'database', 'analyze', str(db), query_pack, '--format=sarifv2.1.0', '--output', str(outpath)], check=True)
        print('CodeQL SARIF ->', outpath)
        return True
    except Exception as e:
        print('CodeQL run failed:', e)
        print('Tip: Ensure queries are available (may require internet to download packs).')
        return False


def run_sonarqube_for_project(project_label: str, project_path: str, project_key: str = None):
    """Run sonar-scanner if available. Requires SONAR_HOST_URL and SONAR_TOKEN env vars set.
    This only sends analysis to server; retrieving CWE-tagged issues requires querying the server API separately."""
    scanner = find_executable('sonar-scanner')
    if not scanner:
        print('sonar-scanner not found. Install SonarScanner or skip SonarQube step.')
        return False
    host = os.environ.get('SONAR_HOST_URL')
    token = os.environ.get('SONAR_TOKEN')
    if not host or not token:
        print('SONAR_HOST_URL and SONAR_TOKEN must be set in environment to run sonar-scanner.')
        return False
    key = project_key or f"{project_label}"
    props_path = Path(project_path) / 'sonar-project.properties'
    props = f"""
sonar.projectKey={key}
sonar.projectName={project_label}
sonar.sources=.
sonar.language=py
sonar.host.url={host}
""".strip()
    props_path.write_text(props)
    env = os.environ.copy()
    env['SONAR_SCANNER_OPTS'] = env.get('SONAR_SCANNER_OPTS', '')
    try:
        print(f"Running SonarQube scan in {project_path} (projectKey={key}) ...")
        subprocess.run([scanner], cwd=project_path, check=True, env=env)
        print('SonarQube scan completed. Retrieve issues via server API if needed.')
        return True
    except Exception as e:
        print('SonarQube scan failed:', e)
        return False

# (custom-ast tool removed as requested)

# ----------------------- Bandit runner -----------------------

def run_bandit_for_project(project_label: str, project_path: str, output_filename: str = None):
    bandit_bin = find_executable('bandit')
    if not bandit_bin:
        print('Bandit not found. Install with pip install bandit.')
        return False
    outname = output_filename or f"{project_label}__bandit.json"
    outpath = RAW_OUTPUT_DIR / outname
    # Run bandit recursively on Python files; use JSON output
    cmd = [bandit_bin, '-r', project_path, '-f', 'json', '-o', str(outpath)]
    try:
        # Bandit returns exit code 1 when issues are found; treat 0 and 1 as success.
        print('RUN:', ' '.join(cmd))
        proc = subprocess.run(cmd, text=True)
        if proc.returncode in (0, 1) and outpath.exists():
            print('Bandit output ->', outpath)
            return True
        else:
            print(f'Bandit returned code {proc.returncode}; output exists={outpath.exists()}')
            return False
    except Exception as e:
        print('Bandit failed:', e)
        return False

# ----------------------- Dlint (flake8 plugin) runner -----------------------

def run_dlint_for_project(project_label: str, project_path: str, output_filename: str = None):
    """Run flake8 with dlint plugin and capture output.
    Requires packages: flake8, dlint. Output is plain text lines.
    """
    # Prefer flake8 in PATH, otherwise try 'python -m flake8'
    flake8_bin = find_executable('flake8')
    outname = output_filename or f"{project_label}__dlint.txt"
    outpath = RAW_OUTPUT_DIR / outname
    cmd = None
    if flake8_bin:
        cmd = [flake8_bin, '--select=DUO', project_path]
    else:
        # fallback to python -m flake8
        cmd = [sys.executable, '-m', 'flake8', '--select=DUO', project_path]
    try:
        print('RUN:', ' '.join(cmd))
        proc = subprocess.run(cmd, capture_output=True, text=True)
        # flake8 returns non-zero when violations found; we still treat it as success
        Path(outpath).write_text(proc.stdout)
        print('Dlint output ->', outpath)
        return True
    except Exception as e:
        print('Dlint (flake8) failed:', e)
        return False

# ----------------------- detect-secrets runner -----------------------

def run_detect_secrets_for_project(project_label: str, project_path: str, output_filename: str = None):
    ds_bin = find_executable('detect-secrets') or find_executable('detect-secrets-cli')
    if not ds_bin:
        print('detect-secrets not found. Install with pip install detect-secrets.')
        return False
    outname = output_filename or f"{project_label}__detect-secrets.json"
    outpath = RAW_OUTPUT_DIR / outname
    # Prefer scan mode with JSON
    cmd = [ds_bin, 'scan', project_path]
    try:
        print('RUN:', ' '.join(cmd))
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode in (0, 1):
            # 1 may mean findings in some versions
            try:
                data = json.loads(proc.stdout)
            except Exception:
                # Some versions write to stderr or non-JSON; fallback to baseline
                data = {'results': []}
            outpath.write_text(json.dumps(data))
            print('detect-secrets output ->', outpath)
            return True
        else:
            print('detect-secrets returned code', proc.returncode)
            return False
    except Exception as e:
        print('detect-secrets failed:', e)
        return False

# ----------------------- CLI -----------------------

def cmd_prepare(args):
    RAW_OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    print('Prepared', RAW_OUTPUT_DIR)


def cmd_clone(args):
    clone_repos()


def cmd_run_cwechecker(args):
    project = args.project
    target = args.target
    if project not in PROJECTS:
        print('Unknown project label. Update PROJECTS mapping or pass a correct label.')
        return
    run_cwe_checker(project, target, args.output)


def cmd_aggregate(args):
    records = collect_all_findings()
    print(f'Total normalized findings: {len(records)}')
    aggregate_and_write_csv(records)


def cmd_report(args):
    if not CONSOLIDATED_CSV.exists():
        print('No consolidated CSV found; run aggregate first.')
        return
    if not pd:
        print('Pandas not installed; install pandas to get nicer reports (pip install pandas)')
    df = pd.read_csv(CONSOLIDATED_CSV)
    # Optional: restrict report to selected tools (comma-separated in REPORT_TOOLS)
    selected_env = os.environ.get('REPORT_TOOLS')
    selected_tools = [t.strip() for t in selected_env.split(',')] if selected_env else None
    present_tools = sorted(df['Tool_name'].unique())
    if selected_tools:
        tools_sorted = selected_tools
        missing = [t for t in tools_sorted if t not in present_tools]
    else:
        tools_sorted = present_tools
        missing = [t for t in TOOLS if t not in present_tools]
    if missing:
        print('Note: no findings/outputs for tools ->', ', '.join(missing))
    # Build tool sets and include empty sets for selected-but-missing tools
    grouped = {tool: set(sub['CWE_ID']) for tool, sub in df.groupby('Tool_name')}
    tool_sets = {t: grouped.get(t, set()) for t in tools_sorted}
    print('\nTool coverage:')
    for t in tools_sorted:
        unique_count = len(tool_sets[t])
        top25_covered = len([c for c in tool_sets[t] if c in CWE_TOP25])
        cov_over_top25 = (top25_covered / max(1, len(CWE_TOP25))) * 100
        cov_within_tool = (top25_covered / max(1, unique_count)) * 100
        print(f"- {t}: unique CWEs={unique_count}, top25_covered={top25_covered}, "
              f"Top25_over_Top25={cov_over_top25:.2f}%, Top25_fraction_of_tool={cov_within_tool:.2f}%")
    # IoU
    print('\nPairwise IoU:')
    for t1 in tools_sorted:
        for t2 in tools_sorted:
            s1, s2 = tool_sets[t1], tool_sets[t2]
            if not s1 and not s2:
                iou = 1.0
            else:
                inter = len(s1 & s2)
                union = len(s1 | s2) if (s1 or s2) else 1
                iou = inter / union if union else 0.0
            print(f'{t1} vs {t2}: IoU={iou:.3f}')


def cmd_help(args):
    print(__doc__)


def build_markdown_report():
    if not CONSOLIDATED_CHECK():
        print('No consolidated CSV to report on. Run aggregate first.')
        return False
    if not pd:
        print('pandas is required to build the markdown report. Install pandas and retry.')
        return False
    df = pd.read_csv(CONSOLIDATED_CSV)
    # Optional: restrict report to selected tools via env REPORT_TOOLS
    selected_env = os.environ.get('REPORT_TOOLS')
    selected_tools = [t.strip() for t in selected_env.split(',')] if selected_env else None
    present_tools = sorted(df['Tool_name'].unique())
    if selected_tools:
        tools_sorted = selected_tools
        missing = [t for t in tools_sorted if t not in present_tools]
    else:
        tools_sorted = present_tools
        missing = [t for t in TOOLS if t not in present_tools]
    # Filter dataframe to only selected tools for the report content
    df_sel = df[df['Tool_name'].isin(tools_sorted)] if tools_sorted else df.copy()
    grouped = {tool: set(sub['CWE_ID']) for tool, sub in df_sel.groupby('Tool_name')}
    tool_sets = {t: grouped.get(t, set()) for t in tools_sorted}
    coverage_rows = []
    for t in tools_sorted:
        unique_count = len(tool_sets[t])
        top25_covered = len([c for c in tool_sets[t] if c in CWE_TOP25])
        cov_over_top25 = (top25_covered / max(1, len(CWE_TOP25))) * 100
        cov_within_tool = (top25_covered / max(1, unique_count)) * 100
        coverage_rows.append({
            'Tool': t,
            'Unique_CWE_Count': unique_count,
            'Top25_Covered': top25_covered,
            'Top25_Coverage_over_Top25_%': round(cov_over_top25, 2),
            'Top25_Fraction_of_Tool_CWEs_%': round(cov_within_tool, 2),
        })
    coverage_df = pd.DataFrame(coverage_rows)
    coverage_df['Top25_Total'] = len(CWE_TOP25)
    # IoU matrix (symmetric table like the screenshot)
    iou_matrix = []
    for t1 in tools_sorted:
        row_vals = []
        for t2 in tools_sorted:
            s1, s2 = tool_sets[t1], tool_sets[t2]
            if not s1 and not s2:
                iou = 1.0
            else:
                inter = len(s1 & s2)
                union = len(s1 | s2) if (s1 or s2) else 1
                iou = inter / union if union else 0.0
            row_vals.append(iou)
        iou_matrix.append(row_vals)
    iou_df = pd.DataFrame(iou_matrix, index=tools_sorted, columns=tools_sorted)
    # Generate plots (coverage bars and IoU heatmap)
    plot_paths = []
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import seaborn as sns
        plots_dir = Path('plots')
        plots_dir.mkdir(exist_ok=True)
        # Coverage bar: Top25_Coverage_over_Top25_%
        if not coverage_df.empty:
            cov1 = coverage_df.sort_values('Top25_Coverage_over_Top25_%', ascending=False)
            plt.figure(figsize=(6, 3.5))
            sns.barplot(x='Tool', y='Top25_Coverage_over_Top25_%', data=cov1, palette='Blues_d')
            plt.title('Top-25 Coverage over Top-25 (%)')
            plt.ylabel('% of Top-25 Covered')
            plt.xlabel('Tool')
            plt.tight_layout()
            p1 = plots_dir / 'coverage_over_top25.png'
            plt.savefig(p1, dpi=150)
            plt.close()
            plot_paths.append(str(p1))
            # Coverage bar: Top25_Fraction_of_Tool_CWEs_%
            cov2 = coverage_df.sort_values('Top25_Fraction_of_Tool_CWEs_%', ascending=False)
            plt.figure(figsize=(6, 3.5))
            sns.barplot(x='Tool', y='Top25_Fraction_of_Tool_CWEs_%', data=cov2, palette='Greens_d')
            plt.title('Top-25 Fraction of Tool CWEs (%)')
            plt.ylabel('% of Tool\'s Unique CWEs in Top-25')
            plt.xlabel('Tool')
            plt.tight_layout()
            p2 = plots_dir / 'coverage_fraction_of_tool.png'
            plt.savefig(p2, dpi=150)
            plt.close()
            plot_paths.append(str(p2))
        # IoU heatmap
        if not iou_df.empty:
            plt.figure(figsize=(5, 4))
            sns.heatmap(iou_df.astype(float), annot=True, fmt='.2f', cmap='Oranges', cbar=True)
            plt.title('IoU (Jaccard) between Tools')
            plt.ylabel('Tool')
            plt.xlabel('Tool')
            plt.tight_layout()
            p3 = plots_dir / 'iou_heatmap.png'
            plt.savefig(p3, dpi=150)
            plt.close()
            plot_paths.append(str(p3))
    except Exception as e:
        print('Plot generation skipped:', e)

    # Per-project summary
    proj_grp = df_sel.groupby(['Project_name','Tool_name','CWE_ID'], as_index=False)['Number_of_Findings'].sum()

    # Compose markdown
    lines = []
    lines.append('# Lab 6: CWE-based SAST Tool Comparison')
    lines.append('')
    lines.append('## Projects analyzed')
    for label, path in PROJECTS.items():
        lines.append(f'- {label}: `{path}`')
    lines.append('')
    lines.append('## Tools selected (Python + CWE)')
    descriptions = {
        'codeql': 'CodeQL: SARIF with CWE tags for Python rules',
        'semgrep': 'Semgrep: Python rules with CWE metadata (custom and registry)',
        'sonarqube': 'SonarQube: Can export JSON/SARIF mappings to CWE (if configured)',
        'bandit': 'Bandit: Python security linter with CWE-related mappings',
        'detect-secrets': 'detect-secrets: Hard-coded credentials mapped to CWE-798',
    }
    for t in tools_sorted:
        lines.append(f"- {descriptions.get(t, t)}")
    lines.append('')
    lines.append('## Consolidated findings (by project, tool, CWE)')
    if not proj_grp.empty:
        head = ['Project_name','Tool_name','CWE_ID','Number_of_Findings']
        lines.append('| ' + ' | '.join(head) + ' |')
        lines.append('| ' + ' | '.join(['---']*len(head)) + ' |')
        for _, r in proj_grp.sort_values(head).iterrows():
            lines.append('| ' + ' | '.join(str(r[c]) for c in head) + ' |')
    else:
        lines.append('_No findings present in consolidated CSV._')
    lines.append('')
    lines.append('## Coverage per tool')
    if not coverage_df.empty:
        # Include both coverage perspectives to align with lab expectations.
        head = [
            'Tool',
            'Unique_CWE_Count',
            'Top25_Covered',
            'Top25_Total',
            'Top25_Coverage_over_Top25_%',
            'Top25_Fraction_of_Tool_CWEs_%',
        ]
        lines.append('| ' + ' | '.join(head) + ' |')
        lines.append('| ' + ' | '.join(['---']*len(head)) + ' |')
        for _, r in coverage_df.sort_values('Unique_CWE_Count', ascending=False).iterrows():
            lines.append('| ' + ' | '.join(str(r[c]) for c in head) + ' |')
    else:
        lines.append('_No coverage data._')
    lines.append('')
    if plot_paths:
        lines.append('### Coverage plots')
        for p in plot_paths:
            if p.endswith('coverage_over_top25.png'):
                lines.append(f'![Top-25 Coverage]({p})')
        for p in plot_paths:
            if p.endswith('coverage_fraction_of_tool.png'):
                lines.append(f'![Top-25 Fraction of Tool CWEs]({p})')
        lines.append('')
    lines.append('## Pairwise IoU (Jaccard)')
    if not iou_df.empty:
        # Header row: blank top-left cell, then tool names as columns
        header_cells = [''] + list(iou_df.columns)
        lines.append('| ' + ' | '.join(header_cells) + ' |')
        lines.append('| ' + ' | '.join(['---'] * len(header_cells)) + ' |')
        # Body rows: row label followed by IoU values
        for row_label, row in iou_df.iterrows():
            vals = [f"{v:.6f}" for v in row.tolist()]
            lines.append('| ' + row_label + ' | ' + ' | '.join(vals) + ' |')
    else:
        lines.append('_No IoU data._')
    lines.append('')
    # Embed IoU heatmap plot if present
    for p in plot_paths:
        if p.endswith('iou_heatmap.png'):
            lines.append('### IoU heatmap')
            lines.append(f'![IoU Heatmap]({p})')
            lines.append('')
    if missing:
        lines.append('> Note: No outputs found for these tools in this run: ' + ', '.join(missing))
        lines.append('')
    lines.append('## Interpretation (fill in)')
    lines.append('- Discuss which tools cover more unique CWEs on these Python repos and why.')
    lines.append('- Discuss overlap (IoU) and complementary detection behavior.')
    lines.append('- Note any rules tuned (e.g., custom Semgrep rules) and implications.')
    lines.append('')
    lines.append('## Threats to validity (fill in)')
    lines.append('- Dataset selection, config differences, false positives/negatives, missing CWE mappings, etc.')
    lines.append('')
    lines.append('## References')
    lines.append('- CWE Top 25 (replace placeholder list with official file).')
    lines.append('- Tool docs (CodeQL, Semgrep, SonarQube).')
    out_path = Path('report.md')
    out_path.write_text('\n'.join(lines))
    print('Wrote markdown report ->', out_path)
    return True


def run_all_pipeline():
    print('--- Running full Lab 6 pipeline (no arguments mode) ---')
    # 1) Prepare and clone
    cmd_prepare(None)
    cmd_clone(None)
    # Clear stale outputs not matching current projects and old CSV to avoid mixing datasets
    for f in RAW_OUTPUT_DIR.iterdir():
        if not f.is_file():
            continue
        try:
            proj, rest = f.name.split('__', 1)
        except ValueError:
            f.unlink(missing_ok=True)
            continue
        if proj not in PROJECTS:
            f.unlink(missing_ok=True)
    if CONSOLIDATED_CSV.exists():
        CONSOLIDATED_CSV.unlink()
    # 2) Semgrep (Python rules)
    print('\n[1/4] Semgrep scanning (Python) ...')
    run_semgrep_all(includes=['*.py'])
    # 3) CodeQL (if available)
    print('\n[2/4] CodeQL scanning (if codeql CLI available) ...')
    for lbl, path in PROJECTS.items():
        run_codeql_for_project(lbl, path)
    # 4) SonarQube (if configured)
    print('\n[3/4] SonarQube scanning (if sonar-scanner and env are set) ...')
    for lbl, path in PROJECTS.items():
        run_sonarqube_for_project(lbl, path)
    # 4.5) (custom-ast removed)
    # 4.6) Bandit scanner
    print('\n[3.6/4] Bandit scanning ...')
    for lbl, path in PROJECTS.items():
        run_bandit_for_project(lbl, path)
    # 4.7) detect-secrets scanner
    print('\n[3.7/4] detect-secrets scanning ...')
    for lbl, path in PROJECTS.items():
        run_detect_secrets_for_project(lbl, path)
    # 5) Aggregate and report
    print('\n[4/4] Aggregating findings and generating reports ...')
    cmd_aggregate(None)
    cmd_report(None)
    build_markdown_report()


def main():
    parser = argparse.ArgumentParser(description='Assignment 6 automation script')
    sub = parser.add_subparsers(dest='cmd')
    sub_prepare = sub.add_parser('prepare')
    sub_prepare.set_defaults(func=cmd_prepare)
    sub_clone = sub.add_parser('clone')
    sub_clone.set_defaults(func=cmd_clone)
    p_run = sub.add_parser('run-cwechecker')
    p_run.add_argument('--project', required=True)
    p_run.add_argument('--target', required=True, help='Path to binary to scan')
    p_run.add_argument('--output', required=False)
    p_run.set_defaults(func=cmd_run_cwechecker)
    sub_agg = sub.add_parser('aggregate')
    sub_agg.set_defaults(func=cmd_aggregate)
    sub_report = sub.add_parser('report')
    sub_report.set_defaults(func=cmd_report)
    sub_report_md = sub.add_parser('report-md')
    sub_report_md.set_defaults(func=lambda a: build_markdown_report())
    sub_help = sub.add_parser('doc')
    sub_help.set_defaults(func=cmd_help)

    # scanners
    p_sgrep = sub.add_parser('scan-semgrep')
    p_sgrep.add_argument('--config', required=False, help='Semgrep config (default: rules/custom_cwe_rules.yml)')
    p_sgrep.add_argument('--include', action='append', help='Semgrep include patterns (default: *.py). Can be repeated.')
    p_sgrep.set_defaults(func=lambda a: run_semgrep_all(config=a.config, includes=a.include))

    p_cql = sub.add_parser('scan-codeql')
    p_cql.add_argument('--queries', required=False, help='CodeQL queries pack (default: codeql/python-queries)')
    p_cql.set_defaults(func=lambda a: all(run_codeql_for_project(lbl, path, queries=a.queries) for lbl, path in PROJECTS.items()))

    p_sonar = sub.add_parser('scan-sonarqube')
    p_sonar.set_defaults(func=lambda a: all(run_sonarqube_for_project(lbl, path) for lbl, path in PROJECTS.items()))

    # (custom-ast CLI removed)

    p_bandit = sub.add_parser('scan-bandit')
    p_bandit.set_defaults(func=lambda a: all(run_bandit_for_project(lbl, path) for lbl, path in PROJECTS.items()))

    p_ds = sub.add_parser('scan-detect-secrets')
    p_ds.set_defaults(func=lambda a: all(run_detect_secrets_for_project(lbl, path) for lbl, path in PROJECTS.items()))

    # dlint scanner
    p_dlint = sub.add_parser('scan-dlint')
    p_dlint.set_defaults(func=lambda a: all(run_dlint_for_project(lbl, path) for lbl, path in PROJECTS.items()))

    args = parser.parse_args()
    if not args.cmd:
        # Run full pipeline by default (no args)
        run_all_pipeline()
        return
    args.func(args)


if __name__ == '__main__':
    main()
