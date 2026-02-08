# 🧬 Cancer Risk Factors — Clean Open Dataset

**Author:** [Tarek Masryo](https://github.com/tarekmasryo) · [Kaggle](https://www.kaggle.com/datasets/tarekmasryo/cancer-risk-factors-dataset)

---

## 📘 Overview

**Dataset summary:**  
**Rows:** 2,000 | **Columns:** 21 | **Missing values:** 0 | **Duplicate rows:** 0

Patient-level tabular dataset covering major **cancer risk factors** across:

- **Lifestyle** (smoking, alcohol use, diet, physical activity)
- **Environment** (air pollution, occupational hazards)
- **Medical / genetic indicators** (family history, BRCA mutation, H. pylori)

Targets you can model:
- `Cancer_Type` (multiclass)
- `Risk_Level` (Low/Medium/High) — **derived** (see leakage note)

---

## 📦 What’s inside

- `data/cancer-risk-factors.csv` — primary table (2,000 × 21)
- `docs/data_dictionary.md` — column definitions
- `examples/quick_analysis.ipynb` — quick EDA + baseline starter

---

## 🧩 Schema summary

| Column | Description | Type | Example |
|--------|-------------|------|---------|
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

## 🧪 Notes (leakage)

`Overall_Risk_Score` and `Risk_Level` are **derived features**.  
If you're training a model to predict risk, exclude derived columns from the feature set.

---

## 💻 Quick start

```bash
# Download
git clone https://github.com/tarekmasryo/cancer-risk-factors-data.git
cd cancer-risk-factors-data

# Install dependencies
pip install -r requirements.txt

# Open example notebook
jupyter notebook examples/quick_analysis.ipynb
```

---

## ✅ Data quality checks

```bash
python scripts/validate_dataset.py
python scripts/make_checksums.py --check
```

To regenerate checksums after a legitimate file update:

```bash
python scripts/make_checksums.py
```

---

## 🪪 License

CC BY 4.0 — see `LICENSE`.

---

## 🧾 Citation

See `CITATION.cff`.
