#  Iris Data Analysis — Week 1

<div align="center">

### 📊 Data Acquisition • 🧹 Data Cleaning • 🔎 EDA • 📈 Visualization

**A complete beginner-to-professional Data Science workflow using Python**

<br>

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge\&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge\&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge\&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-EDA-4c72b0?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge\&logo=jupyter)

<br>

[📂 Repository](https://github.com/Vikas-Yadav-6696/week1-iris-data-analysis)
  •  
[📊 UCI Dataset](https://archive.ics.uci.edu/dataset/53/iris)

</div>

---

## 🚀 Project Overview

Welcome to my **Week 1 Data Science Internship Project**!

This project demonstrates the complete process of taking a public dataset from **raw data → data quality checking → cleaning → exploratory analysis → visualization → insights**.

The project uses the classic **Iris Dataset** from the **UCI Machine Learning Repository**.

> 💡 **Goal:** Build a clean, reproducible and well-documented data-analysis pipeline that can serve as the foundation for future machine-learning projects.

---

## 📌 Project Highlights

| 📌 Component           | Details                         |
| ---------------------- | ------------------------------- |
| 📊 Dataset             | Iris Dataset                    |
| 🏛️ Source             | UCI Machine Learning Repository |
| 🔢 Original Records    | **150**                         |
| 🌸 Species             | **3**                           |
| 📏 Numerical Features  | **4**                           |
| 🧹 Missing Values      | **5 simulated & handled**       |
| ♻️ Duplicate Records   | **Detected & removed**          |
| 📦 Final Clean Dataset | **149 rows × 5 columns**        |
| 📈 Visualizations      | **4**                           |
| 🐍 Language            | **Python**                      |
| 📓 Notebook            | **Jupyter**                     |

---

## 🎯 Objectives

This project focuses on the core foundations of a Data Science workflow:

* 📥 Acquire a publicly available dataset
* 🔍 Inspect dataset structure and quality
* 🧹 Identify and handle missing values
* ♻️ Detect and remove duplicate records
* 🔄 Standardize data types
* 📊 Generate descriptive statistics
* 📈 Perform Exploratory Data Analysis
* 🎨 Create meaningful visualizations
* 💡 Extract useful insights
* 📝 Document the complete workflow

---

#  Dataset

### Iris Dataset

**Source:** UCI Machine Learning Repository
**Dataset ID:** 53

🔗 **Official Dataset:**
https://archive.ics.uci.edu/dataset/53/iris

The original dataset contains:

* **150 observations**
* **4 numerical features**
* **3 Iris species**
* **50 observations per species**

### 📋 Features

| Feature           | Description        | Type        |
| ----------------- | ------------------ | ----------- |
| 🌿 `sepal_length` | Sepal length in cm | Numerical   |
| 🌿 `sepal_width`  | Sepal width in cm  | Numerical   |
| 🌺 `petal_length` | Petal length in cm | Numerical   |
| 🌺 `petal_width`  | Petal width in cm  | Numerical   |
| 🏷️ `species`     | Iris species       | Categorical |

###  Species

```text
Iris Setosa
Iris Versicolor
Iris Virginica
```

> ⚠️ **Data Quality Simulation:**
> The original UCI dataset is clean and contains no missing values. For this internship task, I created a working copy with **5 controlled missing numerical values** and **duplicate records** so that the complete cleaning workflow could be demonstrated.

---

# 🛠️ Tech Stack

<div align="center">

| Technology              | Purpose                        |
| ----------------------- | ------------------------------ |
| 🐍 **Python**           | Core programming language      |
| 🐼 **Pandas**           | Data manipulation              |
| 🔢 **NumPy**            | Numerical operations           |
| 📊 **Matplotlib**       | Visualization                  |
| 🎨 **Seaborn**          | Statistical visualization      |
| 🤖 **Scikit-learn**     | Dataset loading & ML utilities |
| 📓 **Jupyter Notebook** | Interactive analysis           |

</div>

---

# 🔄 Data Science Workflow

```text
                🌐 PUBLIC DATASET
                       │
                       ▼
                📥 DATA ACQUISITION
                       │
                       ▼
                🔍 DATA INSPECTION
                       │
                       ▼
             ⚠️ DATA QUALITY CHECK
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       Missing Values       Duplicate Rows
             │                   │
             ▼                   ▼
      Median Imputation     Remove Duplicates
             │                   │
             └─────────┬─────────┘
                       ▼
                🧹 CLEAN DATA
                       │
                       ▼
                📊 DESCRIPTIVE EDA
                       │
                       ▼
                📈 VISUALIZATION
                       │
                       ▼
                  💡 INSIGHTS
                       │
                       ▼
              🚀 FUTURE ML MODELS
```

---

# 🧹 Data Cleaning

## 1️⃣ Missing Values

Five missing numerical values were intentionally introduced to simulate a real-world data-quality problem.

Missing values were handled using **median imputation**.

```python
for column in numeric_columns:
    df[column] = df[column].fillna(
        df[column].median()
    )
```

### Why Median?

Median imputation is useful because it is less sensitive to extreme values than mean imputation.

---

## 2️⃣ Duplicate Detection

Duplicates were identified using:

```python
df.duplicated().sum()
```

Duplicates were removed using:

```python
df = df.drop_duplicates()
```

This prevents repeated observations from affecting statistics and future machine-learning models.

---

## 3️⃣ Data Type Standardization

Numerical columns were converted to numeric values and the species column was treated as categorical data.

```python
df["species"] = df["species"].astype("category")
```

---

# 📊 Exploratory Data Analysis

The project contains **four main visualizations**.

---

## 📉 1. Missing Values

Shows the simulated missing values before cleaning and confirms that the cleaning process removes them.

📁 File:

```text
reports/figures/01_missing_values.png
```

---

## 🌸 2. Species Distribution

The original dataset contains:

```text
Setosa       → 50
Versicolor   → 50
Virginica    → 50
```

After duplicate removal, the final working dataset contains:

```text
149 observations
```

📁 File:

```text
reports/figures/02_class_distribution.png
```

---

## 🌺 3. Petal Length vs Petal Width

This visualization explores the relationship between petal length and petal width.

### Observation

Setosa forms a relatively distinct cluster, while Versicolor and Virginica show more overlap.

📁 File:

```text
reports/figures/03_petal_scatter.png
```

---

## 🔥 4. Correlation Heatmap

The correlation heatmap shows relationships between numerical variables.

The petal measurements show particularly strong positive relationships.

📁 File:

```text
reports/figures/04_correlation_heatmap.png
```

---

# 💡 Key Insights

### 🌸 Insight 1 — Balanced Original Dataset

The original dataset contains **50 observations per species**, giving all three classes equal representation.

### 🧹 Insight 2 — Data Cleaning Matters

The simulated missing values and duplicate records demonstrate how preprocessing can improve data quality before analysis.

### 🌺 Insight 3 — Petal Features Are Important

Petal length and petal width show strong relationships and provide useful visual separation between species.

### 🔎 Insight 4 — Setosa Is Distinct

Setosa is visually separated from the other species in petal measurements.

### 🔄 Insight 5 — Versicolor & Virginica Overlap

Versicolor and Virginica have greater overlap, suggesting that multiple features may be useful for future classification.

---

# 📁 Project Structure

```text
week1-iris-data-analysis/
│
├── 📂 data/
│   ├── 📂 raw/
│   │   └── README.md
│   └── 📂 processed/
│       └── iris_cleaned.csv
│
├── 📂 notebooks/
│   └── Week_1_Iris_Data_Acquisition_Cleaning_EDA_FINAL.ipynb
│
├── 📂 src/
│   └── week1_eda.py
│
├── 📂 reports/
│   └── 📂 figures/
│       ├── 01_missing_values.png
│       ├── 02_class_distribution.png
│       ├── 03_petal_scatter.png
│       └── 04_correlation_heatmap.png
│
├── 📂 docs/
│   └── Week_1_Data_Acquisition_Cleaning_EDA_Report.docx
│
├── 📄 requirements.txt
├── 📄 PROJECT_INFO.md
├── 📄 LICENSE
├── 📄 .gitignore
└── 📄 README.md
```

---

# ▶️ Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Vikas-Yadav-6696/week1-iris-data-analysis.git
```

```bash
cd week1-iris-data-analysis
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Analysis

### Python Script

```bash
python src/week1_eda.py
```

### Jupyter Notebook

```bash
jupyter notebook
```

Then open:

```text
notebooks/
└── Week_1_Iris_Data_Acquisition_Cleaning_EDA_FINAL.ipynb
```

Run the cells from top to bottom to reproduce the analysis.

---

# 📦 Project Outputs

### 🧹 Cleaned Dataset

```text
data/processed/iris_cleaned.csv
```

### 📈 Visualizations

```text
reports/figures/
├── 01_missing_values.png
├── 02_class_distribution.png
├── 03_petal_scatter.png
└── 04_correlation_heatmap.png
```

### 📓 Notebook

```text
notebooks/
└── Week_1_Iris_Data_Acquisition_Cleaning_EDA_FINAL.ipynb
```

### 📄 Report

```text
docs/
└── Week_1_Data_Acquisition_Cleaning_EDA_Report.docx
```

---

# 🚀 Future Scope

This cleaned dataset can be used for future machine-learning experiments such as:

```text
🤖 Logistic Regression
📍 K-Nearest Neighbors
🌳 Decision Tree
⚡ Support Vector Machine
📏 Feature Scaling
🧩 PCA
🔁 Cross-Validation
📊 Confusion Matrix
🎯 Precision / Recall / F1
🏆 Model Comparison
```

---

# 📄 Documentation

The complete internship report is available here:

```text
docs/
└── Week_1_Data_Acquisition_Cleaning_EDA_Report.docx
```

The report includes:

* Dataset acquisition
* Data-quality assessment
* Cleaning methodology
* Python code
* Summary statistics
* Visualizations
* EDA findings
* Future analysis

---

# 👨‍💻 Author

<div align="center">

## **Vikas Yadav**

🎓 Data Science Internship — Week 1

🐍 Python • 📊 Data Science • 🔎 EDA • 🤖 Machine Learning

<br>

[![GitHub](https://img.shields.io/badge/GitHub-Vikas--Yadav--6696-black?style=for-the-badge\&logo=github)](https://github.com/Vikas-Yadav-6696)

[![Repository](https://img.shields.io/badge/Project-Iris%20Data%20Analysis-blue?style=for-the-badge\&logo=github)](https://github.com/Vikas-Yadav-6696/week1-iris-data-analysis)

</div>

---

# 📚 References

1. **UCI Machine Learning Repository — Iris Dataset**
   https://archive.ics.uci.edu/dataset/53/iris

2. Fisher, R. A. (1936).
   *The use of multiple measurements in taxonomic problems.*

3. Pedregosa et al. (2011).
   *Scikit-learn: Machine Learning in Python.*

---

# ⭐ Project Status

<div align="center">

### ✅ COMPLETED

**Week 1 — Data Acquisition, Cleaning & Exploratory Data Analysis**

---

📥 Data Acquisition
↓
🧹 Data Cleaning
↓
📊 Exploratory Analysis
↓
📈 Visualization
↓
💡 Insights
↓
🚀 Ready for Machine Learning

<br>

**Thanks for visiting this project! 🌸**

</div>
