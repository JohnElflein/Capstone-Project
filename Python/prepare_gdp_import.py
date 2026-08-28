import pandas as pd

# File paths
input_file = "Data/Raw/worldbank_gdp_per_capita.csv"
output_file = "Data/Processed/worldbank_gdp_per_capita.csv"

# Read the raw World Bank CSV
df = pd.read_csv(
    input_file,
    skiprows=4
)

# Keep only the columns we need
years = [str(year) for year in range(2000, 2022)]

df = df[
    ["Country Name", "Country Code", "Indicator Name", "Indicator Code"]
    + years
]

# Convert from wide format to long format
df = df.melt(
    id_vars=[
        "Country Name",
        "Country Code",
        "Indicator Name",
        "Indicator Code"
    ],
    var_name="year",
    value_name="gdp_per_capita"
)

# Convert year to integer
df["year"] = df["year"].astype(int)

# Rename columns
df = df.rename(columns={
    "Country Name": "location",
    "Country Code": "code"
})

# Keep only 2000–2021
df = df.sort_values(["location", "year"])

# Save
df.to_csv(output_file, index=False)

# Report
print(f"Created: {output_file}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Years: {df['year'].min()}–{df['year'].max()}")
print(f"Countries/areas: {df['code'].nunique()}")
print(f"Missing GDP values: {df['gdp_per_capita'].isna().sum()}")