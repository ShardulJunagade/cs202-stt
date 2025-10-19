# Reads ./cwe_findings_consolidated.csv and computes per-tool unique CWE sets,
# Top-25 coverage metrics, and saves plots to ./plots/
import csv
from collections import defaultdict
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

CSV = "cwe_findings_consolidated.csv"
PLOTS_DIR = "plots"
os.makedirs(PLOTS_DIR, exist_ok=True)

df = pd.read_csv(CSV, dtype=str)

# Filter: remove CodeQL from analysis by default; optionally limit to REPORT_TOOLS via env var.
import os
report_tools = os.environ.get("REPORT_TOOLS")  # e.g. "semgrep,bandit,dlint"
if report_tools:
    wanted = {t.strip().lower() for t in report_tools.split(",") if t.strip()}
    df = df[df['Tool_name'].str.lower().isin(wanted)]
else:
    # exclude codeql by default
    df = df[df['Tool_name'].str.lower() != 'codeql']

# Normalize columns and cleanup
df['CWE_ID'] = df['CWE_ID'].fillna('').str.strip().replace({'': None})
df['Is_In_CWE_Top_25?'] = df['Is_In_CWE_Top_25?'].fillna('No')

# Build unique CWE sets per tool
tool_cwes = {}
for tool, g in df.groupby('Tool_name'):
    cwes = set(g['CWE_ID'].dropna().unique())
    tool_cwes[tool] = set(sorted(cwes))

# Top-25 set from CSV flags
top25_set = set(df.loc[df['Is_In_CWE_Top_25?'].str.lower() == 'yes', 'CWE_ID'].dropna().unique())

# Compute metrics
rows = []
for tool, cwes in sorted(tool_cwes.items()):
    unique_count = len(cwes)
    top25_covered = len(cwes & top25_set)
    pct_over_25 = (top25_covered / 25.0) * 100.0
    pct_fraction = (top25_covered / unique_count * 100.0) if unique_count > 0 else 0.0
    rows.append({
        'tool': tool,
        'unique_cwes': unique_count,
        'top25_covered': top25_covered,
        'top25_over_25_pct': pct_over_25,
        'top25_fraction_of_tool_pct': pct_fraction
    })

summary = pd.DataFrame(rows).set_index('tool')
summary.to_csv(os.path.join(PLOTS_DIR, "tool_coverage_summary.csv"))

# Plot: Top-25 over 25 (%)
plt.figure(figsize=(6,4))
sns.barplot(x=summary.index, y=summary['top25_over_25_pct'], palette="rocket")
plt.ylabel("Top-25 covered (% of 25)")
# plt.ylim(0, 100)
plt.title("Top-25 Coverage (over 25) per Tool")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "coverage_over_top25.png"))
plt.close()

# Plot: Top-25 fraction of tool (%)
plt.figure(figsize=(6,4))
sns.barplot(x=summary.index, y=summary['top25_fraction_of_tool_pct'], palette="mako")
plt.ylabel("Top-25 CWEs / Tool Unique CWEs (%)")
plt.ylim(0, 100)
plt.title("Top-25 Fraction of Tool CWEs (%)")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "coverage_fraction_of_tool.png"))
plt.close()

# IoU matrix (Jaccard) between tools
tools = list(summary.index)
n = len(tools)
iou = np.zeros((n, n))
for i, ti in enumerate(tools):
    for j, tj in enumerate(tools):
        a = tool_cwes.get(ti, set())
        b = tool_cwes.get(tj, set())
        if not a and not b:
            iou[i, j] = 1.0
        else:
            union = a | b
            inter = a & b
            iou[i, j] = len(inter) / len(union) if union else 0.0

plt.figure(figsize=(6,5))
sns.heatmap(iou, annot=True, fmt=".2f", xticklabels=tools, yticklabels=tools, cmap="OrRd", vmin=0, vmax=1)
plt.title("IoU (Jaccard) between Tools")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "iou_heatmap.png"))
plt.close()

# --- add per-project summaries & plots ---
projects = sorted(df['Project_name'].dropna().unique())
os.makedirs(os.path.join(PLOTS_DIR, "per_project"), exist_ok=True)

for proj in projects:
    dfp = df[df['Project_name'] == proj]

    # --- ensure a consistent set of tools is used per project ---
    env_report = os.environ.get("REPORT_TOOLS")
    if env_report:
        desired_tools = [t.strip() for t in env_report.split(",") if t.strip()]
    else:
        # use all tools present in the (filtered) CSV so CodeQL has already been excluded if desired
        desired_tools = sorted(df['Tool_name'].dropna().unique())

    # build tool->set for this project, include missing tools with empty sets
    tool_cwes_p = {}
    for t in desired_tools:
        grp = dfp[dfp['Tool_name'] == t]
        cwes = set(grp['CWE_ID'].dropna().unique())
        tool_cwes_p[t] = cwes

    # summary rows per-project
    rows_p = []
    top25_set_p = set(dfp.loc[dfp['Is_In_CWE_Top_25?'].str.lower() == 'yes', 'CWE_ID'].dropna().unique())
    for tool, cwes in sorted(tool_cwes_p.items()):
        unique_count = len(cwes)
        top25_covered = len(cwes & top25_set_p)
        pct_over_25 = (top25_covered / 25.0) * 100.0
        pct_fraction = (top25_covered / unique_count * 100.0) if unique_count > 0 else 0.0
        rows_p.append({'tool': tool, 'unique_cwes': unique_count,
                       'top25_covered': top25_covered,
                       'top25_over_25_pct': pct_over_25,
                       'top25_fraction_of_tool_pct': pct_fraction})
    if rows_p:
        summary_p = pd.DataFrame(rows_p).set_index('tool')
        summary_p.to_csv(os.path.join(PLOTS_DIR, "per_project", f"{proj}_tool_coverage_summary.csv"))
        # per-project IoU heatmap
        tools_p = list(summary_p.index)
        n = len(tools_p)
        iou_p = np.zeros((n, n))
        for i, ti in enumerate(tools_p):
            for j, tj in enumerate(tools_p):
                a = tool_cwes_p.get(ti, set())
                b = tool_cwes_p.get(tj, set())
                if not a and not b:
                    iou_p[i, j] = 1.0
                else:
                    union = a | b
                    inter = a & b
                    iou_p[i, j] = len(inter) / len(union) if union else 0.0
        plt.figure(figsize=(4+0.5*n,4+0.5*n))
        sns.heatmap(iou_p, annot=True, fmt=".2f", xticklabels=tools_p, yticklabels=tools_p,
                    cmap="OrRd", vmin=0, vmax=1)
        plt.title(f"IoU (Jaccard) - {proj}")
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, "per_project", f"{proj}_iou_heatmap.png"))
        plt.close()

print("Summary written to", os.path.join(PLOTS_DIR, "tool_coverage_summary.csv"))
print("Plots written to", PLOTS_DIR)