import pandas as pd

# =========================================================
# NCD Mortality Capstone — Dataset Inspection
# =========================================================

# ---------------------------------------------------------
# 1. Load analytical dataset
# ---------------------------------------------------------

file_path = "Data/Processed/ncd_analytical_country_change.csv"

df = pd.read_csv(file_path)

# ---------------------------------------------------------
# 2. Basic dataset information
# ---------------------------------------------------------

print("\n=== DATASET SHAPE ===")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n=== COLUMN NAMES ===")
for column in df.columns:
    print(column)

# ---------------------------------------------------------
# 3. Data types
# ---------------------------------------------------------

print("\n=== DATA TYPES ===")
print(df.dtypes)

# ---------------------------------------------------------
# 4. First observations
# ---------------------------------------------------------

print("\n=== FIRST 10 ROWS ===")
print(df.head(10).to_string(index=False))

# ---------------------------------------------------------
# 5. Missing values
# ---------------------------------------------------------

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# ---------------------------------------------------------
# 6. Descriptive statistics
# ---------------------------------------------------------

print("\n=== DESCRIPTIVE STATISTICS ===")
print(df.describe().round(2).to_string())