#!/usr/bin/env python
"""
Dataset validation script (fast, deterministic).

Usage:
  python scripts/validate_dataset.py
  python scripts/validate_dataset.py --path data/cancer-risk-factors.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "Patient_ID",
    "Cancer_Type",
    "Age",
    "Gender",
    "Smoking",
    "Alcohol_Use",
    "Obesity",
    "Family_History",
    "Diet_Red_Meat",
    "Diet_Salted_Processed",
    "Fruit_Veg_Intake",
    "Physical_Activity",
    "Air_Pollution",
    "Occupational_Hazards",
    "BRCA_Mutation",
    "H_Pylori_Infection",
    "Calcium_Intake",
    "Overall_Risk_Score",
    "BMI",
    "Physical_Activity_Level",
    "Risk_Level",
]

SCALE_0_10 = [
    "Smoking",
    "Alcohol_Use",
    "Obesity",
    "Diet_Red_Meat",
    "Diet_Salted_Processed",
    "Fruit_Veg_Intake",
    "Physical_Activity",
    "Air_Pollution",
    "Occupational_Hazards",
    "Calcium_Intake",
    "Physical_Activity_Level",
]

BINARY_0_1 = [
    "Gender",
    "Family_History",
    "BRCA_Mutation",
    "H_Pylori_Infection",
]

ALLOWED_RISK_LEVELS = {"Low", "Medium", "High"}
ALLOWED_CANCER_TYPES = {"Breast", "Lung", "Colon", "Prostate", "Skin"}


class ValidationError(RuntimeError):
    pass


def _fail(msg: str) -> None:
    raise ValidationError(msg)


def validate(path: Path) -> None:
    if not path.exists():
        _fail(f"Missing dataset file: {path}")

    df = pd.read_csv(path)

    # Basic shape
    if df.shape[0] == 0:
        _fail("Dataset is empty (0 rows).")
    if df.shape[1] == 0:
        _fail("Dataset has 0 columns.")

    # Columns
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        _fail(f"Missing required columns: {missing_cols}")

    # Missing values
    null_total = int(df.isna().sum().sum())
    if null_total != 0:
        _fail(f"Found missing values: total_nulls={null_total}")

    # Primary key uniqueness
    if df["Patient_ID"].duplicated().any():
        dup = int(df["Patient_ID"].duplicated().sum())
        _fail(f"Patient_ID is not unique: duplicated_ids={dup}")

    # Ranges: 0–10 scales
    for col in SCALE_0_10:
        if (df[col] < 0).any() or (df[col] > 10).any():
            _fail(f"Out-of-range values in {col} (expected 0..10).")

    # Binary
    for col in BINARY_0_1:
        bad = set(df[col].unique()) - {0, 1}
        if bad:
            _fail(f"Invalid values in {col} (expected 0/1). Found: {sorted(bad)}")

    # Age sanity
    if (df["Age"] < 0).any() or (df["Age"] > 120).any():
        _fail("Out-of-range values in Age (expected 0..120).")

    # BMI sanity
    if (df["BMI"] <= 0).any() or (df["BMI"] > 80).any():
        _fail("Out-of-range values in BMI (expected (0..80]).")

    # Derived score sanity
    if (df["Overall_Risk_Score"] < 0).any() or (df["Overall_Risk_Score"] > 1).any():
        _fail("Out-of-range values in Overall_Risk_Score (expected 0..1).")

    # Categoricals
    bad_risk = set(df["Risk_Level"].unique()) - ALLOWED_RISK_LEVELS
    if bad_risk:
        _fail(f"Unexpected Risk_Level values: {sorted(bad_risk)}")

    bad_cancer = set(df["Cancer_Type"].unique()) - ALLOWED_CANCER_TYPES
    if bad_cancer:
        _fail(f"Unexpected Cancer_Type values: {sorted(bad_cancer)}")

    # Report
    print("✅ Validation passed")
    print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    print("Cancer_Type distribution:")
    print(df["Cancer_Type"].value_counts().to_string())
    print("Risk_Level distribution:")
    print(df["Risk_Level"].value_counts().to_string())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        type=str,
        default="data/cancer-risk-factors.csv",
        help="Path to the primary dataset file.",
    )
    args = parser.parse_args()

    try:
        validate(Path(args.path))
        return 0
    except ValidationError as e:
        print(f"❌ Validation failed: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
