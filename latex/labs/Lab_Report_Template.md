# Lab Assignment <N> Report

- Course: CS202 – Software Tools and Techniques for CSE
- Lab Topic: <Title>
- Name: <Your Name>
- Roll Number: <Roll Number>
- Date: <DD Month YYYY>

---

Repository/Notebook Link(s): <optional>

[Insert Image: Environment Overview] -> ../images/lab<N>/1.png
<!-- Optional placeholder image tag: replace path when available -->
<!-- ![Environment Overview](../images/lab<N>/1.png) -->

## 1. Introduction, Setup, and Tools

### 1.1 Introduction
Briefly state what this lab aims to explore, why it matters, and what you specifically did.

### 1.2 Environment and Tools
- OS: <e.g., Windows 11>
- Terminal: <e.g., PowerShell 7>
- Editor: <e.g., VS Code>
- Python: <version>
- Key packages: <list>
- Models (if any): <list>
- Hardware (optional): <e.g., GPU model>

[Insert Image: Environment Details] -> ../images/lab<N>/2.png
<!-- ![Environment Details](../images/lab<N>/2.png) -->

---

## 2. Methodology and Execution

Notebook links (if used):
- lab<N>/<notebook_1>.ipynb
- lab<N>/<notebook_2>.ipynb

### 2.1 Dataset/Repository Selection and Criteria (or Starting Point)
Explain how you chose datasets/repos (or what prior dataset you started with). Include:
- Inclusion/exclusion criteria or prior artifacts used
- Rationale (activity, popularity, language, variety, etc.)

[Insert Image: Repository Selection / Data Overview] -> ../images/lab<N>/3.png
<!-- ![Repository Selection / Data Overview](../images/lab<N>/3.png) -->

### 2.2 Data Collection / Extraction Pipeline
Describe how you gathered the data (e.g., commit traversal, diff extraction, metric runs). Mention edge cases and filtering rules.
- Steps
- Flags/options used (e.g., ignore whitespace, ignore blank lines)
- Columns captured in intermediate CSV(s)

[Insert Image: Code Snippet – Extraction] -> ../images/lab<N>/4.png
<!-- ![Code Snippet – Extraction](../images/lab<N>/4.png) -->

[Insert Image: Sample Output / Row Count] -> ../images/lab<N>/5.png
<!-- ![Sample Output / Row Count](../images/lab<N>/5.png) -->

### 2.3 Processing / Computation
Document computations performed (e.g., structural metrics, semantic similarity, diff variants, categorization logic).
- What was computed
- How (libraries, models, formulas)
- Any exception handling / fallbacks

[Insert Image: Code Snippet – Computation] -> ../images/lab<N>/6.png
<!-- ![Code Snippet – Computation](../images/lab<N>/6.png) -->

[Insert Image: Table Preview – Computed Columns] -> ../images/lab<N>/7.png
<!-- ![Table Preview – Computed Columns](../images/lab<N>/7.png) -->

### 2.4 Analysis / Classification
Explain thresholds/criteria used for classification or comparison, and how agreement/mismatch is defined.

[Insert Image: Code Snippet – Classification / Comparison] -> ../images/lab<N>/8.png
<!-- ![Code Snippet – Classification / Comparison](../images/lab<N>/8.png) -->

[Insert Image: Distributions / Summary Plots] -> ../images/lab<N>/9.png
<!-- ![Distributions / Summary Plots](../images/lab<N>/9.png) -->

### 2.5 Category-wise Breakdown (optional)
If applicable, show results split by file type or category (e.g., source, tests, README, LICENSE, other).

[Insert Image: Bar Chart – Category Mismatches] -> ../images/lab<N>/10.png
<!-- ![Bar Chart – Category Mismatches](../images/lab<N>/10.png) -->

[Insert Image: Pie Chart – Category Distribution] -> ../images/lab<N>/11.png
<!-- ![Pie Chart – Category Distribution](../images/lab<N>/11.png) -->

### 2.6 Optional: Evaluation of "Which is Better?"
If relevant, describe how you’d objectively evaluate competing methods/algorithms:
- Define quality metrics (readability, compactness, block preservation, etc.)
- Ground-truth/annotation plan (if any)
- Automated scoring approach

---

## 3. Results and Analysis
Summarize key metrics as a compact table.

| Metric | Value |
|--------|-------|
| <Metric 1> | <value> |
| <Metric 2> | <value> |
| <Metric 3> | <value> |

[Insert Image: Key Plots / Highlights] -> ../images/lab<N>/12.png
<!-- ![Key Plots / Highlights](../images/lab<N>/12.png) -->

---

## 4. Discussion and Conclusion

### 4.1 Challenges
Briefly list practical hurdles and how you addressed them.

### 4.2 What I Learned
Short reflection on insights and tooling takeaways.

---

## References
- <Tool/Library 1 link>
- <Model link>
- <Docs link>
- <Lab README link>

---

## Usage Notes
- Replace <N> with the lab number and update paths accordingly.
- Image convention (suggested): ../images/lab<N>/<index>.png in ascending order as they appear.
- Keep alt text descriptive and consistent with the captions (you can convert the "Insert Image" lines into actual markdown image tags once you have the images).
- Maintain consistent section numbering (1.x, 2.x, etc.).
- Include links to notebooks and CSV outputs where useful (e.g., results/final_metrics.csv).