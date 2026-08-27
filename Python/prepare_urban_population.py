import pandas as pd

# File paths
input_file = "Data/Raw/un_urban_population.xlsx"
output_file = "Data/Processed/un_urban_population.csv"

# Read the Urban sheet
df = pd.read_excel(
    input_file,
    sheet_name="Urban"
)

# Make all column names strings
df.columns = df.columns.astype(str)

# Keep only actual countries/areas
df = df[df["LocTypeName"] == "Country/Area"].copy()

# Keep only the study period
years = [str(year) for year in range(2000, 2022)]

# Select the columns we need
columns_to_keep = [
    "Location",
    "ISO3_Code"
] + years

df = df[columns_to_keep]

# Rename identifier columns
df = df.rename(columns={
    "Location": "location",
    "ISO3_Code": "code"
})

# Convert from wide format to long format
df = df.melt(
    id_vars=["location", "code"],
    var_name="year",
    value_name="urban_population_pct"
)

# Convert year to integer
df["year"] = df["year"].astype(int)

# Sort the data
df = df.sort_values(["location", "year"])

# Save the prepared dataset
df.to_csv(output_file, index=False)

# Report results
print(f"Created: {output_file}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Years: {df['year'].min()}–{df['year'].max()}")
print(f"Countries: {df['code'].nunique()}")
print(f"Missing values: {df['urban_population_pct'].isna().sum()}")