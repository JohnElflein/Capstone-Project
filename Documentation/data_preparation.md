# Data Preparation

## Project

**Working title:** Global Non-Communicable Disease (NCD) Mortality: The Relationship Between Economic Development, Healthcare Spending, and Urbanization, 2000–2021

**Research question:** How has NCD mortality changed across countries between 2000 and 2021, and how are economic development, healthcare expenditure, and urbanization associated with these changes?

## Data Sources

The project uses three main data sources:

- **World Health Organization (WHO):** NCD mortality and health expenditure
- **World Bank:** GDP per capita
- **United Nations (UN):** Urban population

The analysis period is **2000–2021**.

## Variables

### Outcome variable

**NCD mortality rate**

The NCD mortality data were taken from the WHO dataset. The relevant mortality measure is represented by `FactValueNumeric`, with country identified using `SpatialDimValueCode` and year using `Period`.

The analysis uses the `Both sexes` category.

### Independent variables

**GDP per capita**

The World Bank indicator selected is:

> GDP per capita, PPP (constant 2021 international $)

Indicator code: `NY.GDP.PCAP.PP.KD`

**Health expenditure per capita**

The WHO health expenditure variable selected is:

> Current Health Expenditure (CHE), in current international $ (PPP) per capita

Variable code: `che_ppp_pc`

**Urban population**

The UN urban population dataset provides urban population as a percentage of the population. The prepared variable is `urban_population_pct`.

## Data Preparation

The raw datasets were kept in `Data/Raw/`. Python scripts in `python/` were used to prepare the datasets for analysis.

### GDP

The original World Bank data contained metadata rows and annual columns from 1960 onward.

The preparation process:

1. Removed the metadata rows.
2. Selected the years 2000–2021.
3. Reshaped the annual columns into a country-year structure.
4. Kept country name and country code.
5. Converted GDP values to numeric values.
6. Created the processed dataset:

`Data/Processed/worldbank_gdp_per_capita.csv`

The resulting dataset contains **5,830 rows**, representing **265 countries/areas across 22 years**.

There are **471 missing GDP values** in the source data.

### Health expenditure

The WHO health expenditure workbook was prepared using the `che_ppp_pc` variable.

The resulting dataset:

`Data/Processed/who_health_expenditure.csv`

contains:

- **4,200 rows**
- **195 countries**
- **2000–2021**
- **1 missing value**

The missing value was identified as Venezuela (`VEN`) in 2018.

### Urban population

The UN workbook's `Urban` sheet was used.

The dataset contains different types of geographic and analytical aggregates, so records classified as `Country/Area` were retained.

The annual columns were converted to numeric years and the years 2000–2021 were selected.

The resulting dataset:

`Data/Processed/un_urban_population.csv`

contains:

- **5,214 rows**
- **237 countries**
- **2000–2021**
- **0 missing values**

### NCD mortality

The WHO NCD mortality dataset was retained in:

`s_johnelflein.who_ncd_mortality`

The relevant fields used in the analytical dataset include:

- `Location`
- `SpatialDimValueCode`
- `Period`
- `FactValueNumeric`

The data were restricted to the required period and the `Both sexes` category.

## SQL Integration and Validation

The prepared datasets were imported into the existing PostgreSQL schema:

`s_johnelflein`

The main tables used were:

- `s_johnelflein.who_ncd_mortality`
- `s_johnelflein.worldbank_gdp_per_capita`
- `s_johnelflein.who_health_expenditure`
- `s_johnelflein.un_urban_population`

SQL checks were used throughout the preparation process to verify:

- Row counts
- Year coverage
- Country counts
- Missing values
- Country-code matching
- Duplicate country-year records
- Data types
- Completeness at the beginning and end of the analysis period

The checks confirmed that the datasets had the expected structure and values.

## Complete Analytical Sample

The four datasets do not contain the same number of countries.

After joining the datasets by country code and year and requiring complete observations for all four variables in both 2000 and 2021, the final complete-case sample contains:

**171 countries**

The resulting analytical datasets are:

`Data/Processed/ncd_analytical_country_year.csv`

and

`Data/Processed/ncd_analytical_country_change.csv`

### Country-year analytical dataset

The country-year dataset contains:

- Country
- Country code
- Year
- NCD mortality rate
- GDP per capita
- Health expenditure per capita
- Urban population percentage

### Country-change analytical dataset

The country-change dataset contains one row per country and compares 2000 with 2021.

It includes:

- NCD mortality in 2000 and 2021
- Percentage change in NCD mortality
- GDP per capita in 2000 and 2021
- Percentage change in GDP per capita
- Health expenditure per capita in 2000 and 2021
- Percentage change in health expenditure
- Urban population percentage in 2000 and 2021
- Percentage-point change in urban population

The final country-change dataset contains **171 rows and 14 columns** and has **no missing values**.

## Data Preparation Decisions

The analysis uses complete cases so that comparisons and statistical analyses are based on countries with observations for all four variables at both endpoints of the study period.

Country codes are used as the primary key for joining datasets because country names differ between the source datasets.

The analysis consistently focuses on **2000–2021**.

## Next Stage

The next stage is statistical analysis in Python.

The analysis will investigate the relationships between NCD mortality and:

1. GDP per capita
2. Health expenditure per capita
3. Urban population

The planned analysis will include descriptive statistics, correlation analysis, hypothesis testing, and regression analysis.