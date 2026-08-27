import pandas as pd

# File paths
input_file = "Data/Raw/who_health_expenditure.xlsx"
output_file = "Data/Processed/who_health_expenditure_import.csv"

# Read the Data sheet
df = pd.read_excel(
    input_file,
    sheet_name="Data"
)

# Keep only the variables needed for the capstone
columns_to_keep = [
    "location",
    "code",
    "region",
    "income",
    "year",
    "che_ppp_pc"
]

df = df[columns_to_keep]

# Keep the study period
df = df[
    (df["year"] >= 2000) &
    (df["year"] <= 2021)
]

# Save the prepared dataset
df.to_csv(output_file, index=False)

print(f"Created: {output_file}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Years: {df['year'].min()}–{df['year'].max()}")
print(f"Countries: {df['code'].nunique()}")