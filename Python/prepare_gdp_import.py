import pandas as pd

input_file = "Data/Raw/worldbank_gdp_per_capita.csv"
output_file = "Data/Processed/worldbank_gdp_per_capita_import.csv"

# Read the World Bank file, skipping the two metadata rows
df = pd.read_csv(input_file, skiprows=4)

# Keep only the columns needed for the capstone
years = [str(year) for year in range(2000, 2022)]

columns_to_keep = [
    "Country Name",
    "Country Code",
    "Indicator Name",
    "Indicator Code",
] + years

df = df[columns_to_keep]

# Save the prepared import file
df.to_csv(output_file, index=False)

print(f"Created: {output_file}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")