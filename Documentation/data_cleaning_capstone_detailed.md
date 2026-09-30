# Data Cleaning and Preparation

## 1. Project data

The capstone combines four datasets covering **2000–2021**:

| Dataset | Source | Main variable used |
|---|---|---|
| NCD mortality | WHO | Age-standardized NCD mortality rate per 100,000 population |
| GDP per capita | World Bank | GDP per capita, PPP (constant 2021 international $) |
| Health expenditure | WHO  | Current health expenditure per capita, PPP (current international $) |
| Urban population | United Nations | Urban population as % of total population |

The purpose of the cleaning process was to put all four sources into a common **country–year structure**, using ISO3 country codes and year as the main join keys.

---

## 2. Raw NCD mortality data

### What the raw file looked like

The WHO file contained **4,070 observations and 34 columns**. It was already relatively close to the structure needed for the project. The dataset contained the indicator:

> Age-standardized NCD mortality rate (per 100,000 population)

It included country names and ISO3 country codes, years, sex information, the numeric mortality value, and additional WHO metadata.

### Cleaning

For the NCD dataset, the important steps were:

1. Identify the correct WHO indicator: **age-standardized NCD mortality rate**.
2. Use the country identifier and ISO3 code to identify countries.
3. Use the year (`Period`) as the time variable.
4. Use the numeric mortality value (`FactValueNumeric`) as the NCD mortality rate.
5. Keep the observations for the study period **2000–2021**.
6. Standardize the final field names so that they could be joined with the other datasets.
7. Keep country/year observations rather than aggregating them, because the project needed country-level trends over time.

The final analytical variable was named:

`ncd_mortality_rate`

### Important issue

The WHO source contained considerably more information than was needed for the analysis. A major part of the preparation was therefore distinguishing the actual mortality measure from the many metadata and descriptive fields in the download.

---

## 3. Raw GDP per capita data

### What the raw file looked like

The World Bank download was in a **wide format**. Country information occupied the first columns, while each year was a separate column.

The raw download contained **265 country/area records** and years extending well beyond the project's 2000–2021 study period.

### Cleaning

The Python preparation script handled the World Bank file as follows:

1. Read the CSV while skipping the first **four metadata rows**.
2. Kept only:
   - Country Name
   - Country Code
   - Indicator Name
   - Indicator Code
   - years **2000–2021**
3. Reshaped the data from **wide to long format** using `melt()`.
4. Changed the year field from text to an integer.
5. Renamed:
   - `Country Name` → `location`
   - `Country Code` → `code`
6. Sorted the observations by country and year.
7. Saved the cleaned data as a CSV.

The resulting structure was one row per **country-year**, with the GDP variable named:

`gdp_per_capita`

This transformation was important because the other prepared datasets needed to be joined using a common country/year structure.

---

## 4. Raw health expenditure data

### What the raw file looked like

The WHO health expenditure download was an Excel workbook with several sheets:

- `Data`
- `Codebook`
- `Metadata`
- `Version`

The `Data` sheet contained **4,612 rows and 4,120 columns**. It included many different health-financing variables, far more than were required for the project.

The variable selected for this project was:

`che_ppp_pc`

This represents **current health expenditure per capita in PPP/current international dollars**.

### Cleaning

The Python preparation script:

1. Opened the `Data` sheet.
2. Selected only the fields needed for the project:
   - `location`
   - `code`
   - `region`
   - `income`
   - `year`
   - `che_ppp_pc`
3. Restricted the data to **2000–2021**.
4. Exported the result as a CSV.

The cleaned health expenditure data therefore had a much simpler country-year structure.

The analytical variable was later named:

`health_expenditure_per_capita`

### Problem encountered

This was one of the more complicated raw datasets because the workbook contained **thousands of columns** and multiple sheets. It was important to use the codebook to identify the correct expenditure measure rather than accidentally selecting another health-spending variable.

The original source also contained data beyond 2021, but these were deliberately excluded because the NCD mortality analysis ends in 2021.

---

## 5. Raw urban population data

### What the raw file looked like

The UN urban population workbook contained several sheets:

- `info`
- `Rural`
- `Urban`
- `NOTES`

The `Urban` sheet contained **327 rows and 111 columns**. Importantly, it did not contain only countries. It also included aggregates such as regions, income groups, and other groupings.

### Cleaning

The Python preparation script:

1. Opened the `Urban` sheet.
2. Converted all column names to strings.
3. Kept only rows where:
   `LocTypeName == "Country/Area"`
4. Selected:
   - `Location`
   - `ISO3_Code`
   - years **2000–2021**
5. Renamed:
   - `Location` → `location`
   - `ISO3_Code` → `code`
6. Reshaped the data from **wide to long format**.
7. Converted year to an integer.
8. Sorted by country and year.
9. Saved the cleaned dataset as a CSV.

The final analytical variable was:

`urban_population_pct`

This represents urban population as a percentage of total population.

### Problem encountered

The biggest issue was that the workbook contained **non-country rows**. If these rows had been included, regional and income-group aggregates could have been treated as if they were countries.

Filtering on `LocTypeName == "Country/Area"` solved this problem.

---

# 6. Standardizing the datasets

After preparing the individual sources, the datasets needed a common structure before they could be joined.

The most important standardization decisions were:

### Country identifier

I used the **ISO3 country code** as the primary country key.

For example:

- Korea → `KOR`
- Japan → `JPN`
- Germany → `DEU`

This was more reliable than joining on country names because different organizations can use slightly different country-name conventions.

### Time identifier

All datasets were restricted to:

**2000–2021**

and the year field was converted to an integer.

### Data structure

The datasets were converted to a common **long format**:

> one row = one country in one year

This gave us the same basic structure across the four sources:

`country + code + year + variable`

---

# 7. Joining the datasets

The cleaned datasets were joined at the **country-year level**.

The conceptual structure was:

```text
WHO NCD mortality
        |
        | country code + year
        |
World Bank GDP
        |
        | country code + year
        |
WHO health expenditure
        |
        | country code + year
        |
UN urban population
        |
        v
NCD analytical country-year dataset
```

The join therefore matched observations using:

**ISO3 country code + year**

This allowed the four variables to appear on the same country-year observation.

The resulting analytical dataset contains:

| Variable | Meaning |
|---|---|
| `country` | Country name |
| `code` | ISO3 country code |
| `year` | Year |
| `ncd_mortality_rate` | Age-standardized NCD mortality rate |
| `gdp_per_capita` | GDP per capita |
| `health_expenditure_per_capita` | Health expenditure per capita |
| `urban_population_pct` | Urban population % |

---

# 8. Final dataset 1: `ncd_analytical_country_year.csv`

This dataset is the **country-year analytical dataset**.

It contains:

- **3,949 rows**
- **7 columns**
- **183 countries**
- years from **2000 to 2021**

Each row represents one country in one year.

### Why there are 3,949 rather than 183 × 22 observations

A completely balanced dataset would contain:

`183 countries × 22 years = 4,026 observations`

The final dataset has fewer observations because some countries do not have complete data for every year and I did **not invent or impute missing observations**.

There are also no duplicate country-year combinations in the final dataset.

### What this dataset is used for

This dataset is primarily used for:

- country trends over time
- global/yearly comparisons
- maps
- rankings
- Tableau visualizations
- examining how NCD mortality and the explanatory variables change over time

---

# 9. Creating the country-change dataset

For the statistical analysis, I created a second dataset from the country-year data.

Instead of keeping every year, I compared each country's **2000 value with its 2021 value**.

For each country, I calculated:

### NCD mortality percentage change

```text
((NCD mortality 2021 - NCD mortality 2000)
 / NCD mortality 2000) × 100
```

### GDP percentage change

```text
((GDP 2021 - GDP 2000)
 / GDP 2000) × 100
```

### Health expenditure percentage change

```text
((Health expenditure 2021 - Health expenditure 2000)
 / Health expenditure 2000) × 100
```

### Urbanization change

Urbanization was handled differently.

Because urban population is already expressed as a percentage, I calculated a **percentage-point change**:

```text
Urban population 2021 - Urban population 2000
```

For example:

> 50% urban in 2000 → 60% urban in 2021 = **+10 percentage points**

This is not the same as saying urbanization increased by 10%.

---

# 10. Final dataset 2: `ncd_analytical_country_change.csv`

The resulting dataset contains:

- **171 countries**
- **14 columns**
- one row per country
- 2000 and 2021 values
- calculated changes between 2000 and 2021

The columns are:

```text
country
code
ncd_mortality_2000
ncd_mortality_2021
ncd_mortality_pct_change
gdp_2000
gdp_2021
gdp_pct_change
health_expenditure_2000
health_expenditure_2021
health_expenditure_pct_change
urban_population_2000
urban_population_2021
urban_population_pct_point_change
```

---

# 11. Why the final datasets contain different numbers of countries

This initially looks like a problem because the country-year dataset contains **183 countries**, while the country-change dataset contains **171**.

However, this is intentional.

### Country-year dataset

The country-year dataset is used for descriptive analysis. A country can be included if it has enough country-year data to contribute observations to the time-series analysis, even if it does not have a complete 2000–2021 record.

### Country-change dataset

The country-change dataset requires a valid value in **both 2000 and 2021** for the variables needed in the analysis.

If a country is missing either endpoint, its 2000→2021 change cannot be calculated reliably.

Therefore:

> **183 countries are available in the country-year dataset, while 171 countries have the complete endpoint data required for the country-change analysis.**

This is a consequence of data availability rather than an arbitrary decision to remove countries.

---

# 12. Missing data and data-quality checks

Missing data were an important issue because the four sources did not have identical country coverage.

Rather than filling missing values with estimates, the project retained the available observations and allowed the final joins and endpoint requirements to determine the analytical sample.

Several quality checks were performed:

- country identifiers were standardized using ISO3 codes
- all datasets were restricted to 2000–2021
- year fields were converted to a consistent numeric format
- non-country aggregate rows were removed from the urbanization data
- duplicate country-year observations were checked
- the final country-change dataset was checked for duplicate countries
- missing values were checked before statistical analysis

The final `ncd_analytical_country_change.csv` contains **171 countries with no missing values in the variables required for the analysis**.

---

# 13. Main problems encountered

### 1. Different file formats

The four sources were not delivered in the same format:

- WHO NCD mortality: CSV
- World Bank GDP: CSV with metadata rows and years in columns
- WHO health expenditure: Excel workbook with multiple sheets and thousands of columns
- UN urban population: Excel workbook with multiple sheets and aggregate rows

Each source therefore required a slightly different preparation process.

### 2. Wide versus long data

The GDP and urban population datasets were initially in **wide format**, with one column for each year.

For example:

```text
country | code | 2000 | 2001 | 2002 | ... | 2021
```

For analysis, we needed:

```text
country | code | year | value
```

We therefore used a wide-to-long transformation (`melt`) for these datasets.

### 3. Non-country observations

The urban population workbook included regions, income groups, and other aggregates alongside countries.

These had to be removed so that the analysis represented actual countries/areas rather than accidentally treating regional aggregates as countries.

### 4. Large and complicated health expenditure workbook

The WHO health expenditure file contained thousands of columns and multiple sheets. Selecting the correct variable was therefore an important step.

The `che_ppp_pc` field was chosen as the health expenditure measure for the project.

### 5. Different country coverage

Not every source had data for every country and every year.

This created an incomplete country-year panel and reduced the number of countries that could be included in the 2000→2021 change analysis.

### 6. Country matching

Country names are not always identical between international organizations.

Using ISO3 codes gave us a much more consistent way to match the datasets.

### 7. Study-period consistency

Some sources contained years before 2000 and after 2021. These were deliberately removed so that all variables matched the project's study period.

---

# 14. What the cleaning process taught me

The main lesson was that **data analysis starts before statistical analysis**.

The biggest challenge was not simply loading the files into Python. It was making sure that:

1. the correct variable was selected from each source;
2. countries were identified consistently;
3. the same years were being compared;
4. regional aggregates were not mistaken for countries;
5. the datasets had compatible structures;
6. missing observations were handled transparently;
7. the final analytical sample matched the research question.

The cleaning process also made an important distinction between the two analytical datasets:

> **`ncd_analytical_country_year.csv` is designed to understand trends over time, while `ncd_analytical_country_change.csv` is designed to test whether changes in GDP, health expenditure, and urbanization are associated with changes in NCD mortality between 2000 and 2021.**

This separation will make the Tableau visualizations and statistical analysis much clearer.
