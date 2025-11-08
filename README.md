# 🧬 Cancer Risk Factors — Clean Open Dataset

**Author:** [Tarek Masryo](https://github.com/tarekmasryo) · [Kaggle](https://www.kaggle.com/datasets/tarekmasryo/cancer-risk-factors-dataset) 

---

## 📘 Overview

**Dataset summary:**  
**Rows:** 2,000 | **Columns:** 21 | **Missing Values:** 0  

This dataset provides a **clean and well-structured view** of major **cancer risk factors** at the patient level.  
Each record represents an individual described through **lifestyle**, **environmental**, and **genetic** indicators associated with cancer development.


It is ideal for:
- Educational use in **data science, EDA, and ML pipelines**  
- Testing **classification algorithms** (e.g., predict `Cancer_Type` or `Risk_Level`)  
- Demonstrating **data cleaning, feature importance, and leakage detection**

---

## 🧩 Schema Summary

| Column | Description | Type | Example |
|--------|--------------|------|----------|
| `Patient_ID` | Unique patient identifier | string | LU0001 |
| `Cancer_Type` | Cancer category (target) | categorical | Lung |
| `Age` | Age in years | int | 61 |
| `Gender` | Encoded gender (0=Female, 1=Male) | int | 1 |
| `Smoking`, `Alcohol_Use`, `Obesity` | Lifestyle risk indicators (0–10 scale) | int | 7 |
| `Family_History` | Family cancer history (0/1) | int | 0 |
| `Diet_Red_Meat`, `Diet_Salted_Processed`, `Fruit_Veg_Intake` | Nutritional risk factors (0–10 scale) | int | 4 |
| `Physical_Activity`, `Physical_Activity_Level` | Activity indicators (0–10 scale) | int | 5 |
| `Air_Pollution`, `Occupational_Hazards` | Environmental exposure (0–10 scale) | int | 6 |
| `BRCA_Mutation`, `H_Pylori_Infection` | Medical/genetic risk factors (0/1) | int | 0 |
| `Calcium_Intake` | Dietary factor (0–10 scale) | int | 5 |
| `BMI` | Body Mass Index | float | 28.4 |
| `Overall_Risk_Score` | Derived composite score [0–1] | float | 0.42 |
| `Risk_Level` | Categorical risk label (Low/Medium/High) | categorical | Medium |

---

## 🧪 Data Insights

- No missing or duplicate values  
- Balanced representation across five cancer types: Breast, Lung, Colon, Skin, and Prostate  
- Variables scaled on a **0–10 risk intensity** system  
- `Overall_Risk_Score` and `Risk_Level` are **derived features** — exclude from training if predicting risk  

---

## 💻 Quick Start

```bash
# Download dataset
git clone https://github.com/TarekMasryo/cancer-risk-factors-data.git
cd cancer-risk-factors-data

# Install dependencies
pip install -r requirements.txt

# Open quick example
jupyter notebook examples/quick_analysis.ipynb





