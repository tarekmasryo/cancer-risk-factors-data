# Data Dictionary — Cancer Risk Factors (2025)

**File:** `cancer-risk-factors.csv`

| Column | Type | Description |
|:-------|:-----|:------------|
| Patient_ID | str | Unique patient identifier |
| Cancer_Type | str | Cancer type (Breast, Lung, Colon, Prostate, Skin) |
| Age | int | Patient age (years) |
| Gender | int | Encoded gender (0 = Female, 1 = Male) |
| Smoking | int | Smoking frequency/intensity (0–10 scale) |
| Alcohol_Use | int | Alcohol consumption level (0–10 scale) |
| Obesity | int | Obesity level / BMI category (0–10 scale) |
| Family_History | int | Family history of cancer (0/1) |
| Diet_Red_Meat | int | Frequency of red meat consumption (0–10 scale) |
| Diet_Salted_Processed | int | Processed/salty food intake frequency (0–10 scale) |
| Fruit_Veg_Intake | int | Fruit and vegetable consumption (0–10 scale) |
| Physical_Activity | int | Physical activity frequency (0–10 scale) |
| Air_Pollution | int | Exposure to polluted environments (0–10 scale) |
| Occupational_Hazards | int | Work-related exposure to carcinogens (0–10 scale) |
| BRCA_Mutation | int | Genetic BRCA mutation presence (0/1) |
| H_Pylori_Infection | int | Presence of H. pylori infection (0/1) |
| Calcium_Intake | int | Dietary calcium intake (0–10 scale) |
| BMI | float | Body Mass Index (15–40 typical range) |
| Overall_Risk_Score | float | Derived composite score of all risk factors (0–1) |
| Physical_Activity_Level | int | Composite score of physical activity (0–10 scale) |
| Risk_Level | str | Categorized risk group: Low, Medium, or High |
