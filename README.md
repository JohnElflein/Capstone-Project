
# Global Non-Communicable Disease (NCD) Mortality: 2000–2021

## Project Overview

This project investigates changes in non-communicable disease (NCD) mortality across countries between 2000 and 2021 and examines how these changes are associated with economic development, healthcare expenditure, and urbanization.

The project was developed as the capstone project for the **Spiced Academy Data Analytics Program**.

The analysis combines data from the **World Health Organization (WHO)**, **World Bank**, and **United Nations (UN)** and uses SQL, Python, and Tableau to prepare, analyze, and visualize the data.

---

## Research Question

> **How has NCD mortality changed across countries between 2000 and 2021, and how are economic development, healthcare expenditure, and urbanization associated with these changes?**

### Hypotheses

The overall hypothesis is:

> Economic development, healthcare expenditure, and urbanization are significantly associated with changes in NCD mortality across countries between 2000 and 2021.

The analysis examines three specific hypotheses:

**H1 — GDP per capita**

- H₀: Change in GDP per capita is not significantly associated with change in NCD mortality.
- H₁: Change in GDP per capita is significantly associated with change in NCD mortality.

**H2 — Health expenditure**

- H₀: Change in health expenditure per capita is not significantly associated with change in NCD mortality.
- H₁: Change in health expenditure per capita is significantly associated with change in NCD mortality.

**H3 — Urbanization**

- H₀: Change in urban population is not significantly associated with change in NCD mortality.
- H₁: Change in urban population is significantly associated with change in NCD mortality.

---

## Key Findings

The analysis produced several main findings:

- Average NCD mortality across countries declined between 2000 and 2021.
- The average country-level NCD mortality rate decreased from approximately **643.7 to 531.2 deaths per 100,000**, a decline of **17.5%**.
- The magnitude and direction of change varied substantially between countries.
- Urbanization showed the strongest and most consistent association with changes in NCD mortality.
- GDP per capita was negatively associated with NCD mortality change in the primary regression model, but this association was no longer statistically significant in the sensitivity analysis.
- Health expenditure per capita was not statistically significant in either the primary or sensitivity model.
- The primary multiple regression model explained **11.5% of the variation** in country-level NCD mortality changes.

These findings indicate **associations rather than causal effects**.

---

## Data Sources

| Variable | Source | Indicator / Measure |
|---|---|---|
| NCD mortality | World Health Organization (WHO) | Age-standardized NCD mortality rate per 100,000 |
| GDP per capita | World Bank | GDP per capita, PPP, constant 2021 international $ |
| Health expenditure | WHO Global Health Expenditure Database | Current health expenditure per capita, PPP |
| Urbanization | United Nations | Urban population as % of total population |

### NCD Mortality

NCD mortality data are from the **WHO Global Health Estimates (GHE) 2021**.

The mortality measure is an **age-standardized NCD mortality rate per 100,000 population**, which allows comparisons between countries with different population age structures.

The WHO GHE data provide comparable estimates across countries and years. The estimates are not necessarily identical to official national estimates.

### GDP per Capita

GDP per capita data are from the **World Bank**:

`NY.GDP.PCAP.PP.KD`

This measure represents GDP per capita based on purchasing power parity (PPP) in constant 2021 international dollars.

### Health Expenditure

Health expenditure data are from the **WHO Global Health Expenditure Database**:

`SH.XPD.CHEX.PP.CD`

The measure represents current health expenditure per capita based on purchasing power parity.

### Urbanization

Urbanization is measured using the **urban population as a percentage of total population**, sourced from the United Nations World Urbanization Prospects.

---

## Study Period

The analysis covers the period:

**2000–2021**

The mortality analysis ends in 2021 because this is the latest year available in the WHO mortality dataset used for the project.

---

## Methodology

The project follows a data pipeline consisting of:

1. Data collection
2. Data cleaning
3. Data validation
4. Data integration
5. Exploratory analysis
6. Statistical analysis
7. Data visualization
8. Tableau dashboard and story development

### Data Preparation

The datasets were cleaned and transformed using Python and SQL.

The preparation process included:

- Selecting the relevant indicators
- Standardizing country identifiers
- Selecting the 2000–2021 study period
- Reshaping datasets from wide to long format where necessary
- Checking for missing values
- Checking for duplicate country-year observations
- Validating country coverage across datasets
- Joining the datasets using standardized country codes
- Creating analytical datasets for visualization and statistical analysis

Detailed data preparation documentation is available in:

`Documentation/data_cleaning_capstone_detailed.md`

and

`Documentation/data_preparation.md`

---

## Analytical Datasets

Two main analytical datasets were created.

### Country-Year Dataset

`ncd_analytical_country_year.csv`

This dataset contains one observation per country and year.

It is primarily used for:

- Time-series analysis
- Global and country-level trends
- Country comparisons
- Maps
- Regional comparisons
- Tableau visualizations

The dataset contains up to 22 observations per country for the 2000–2021 period.

Some countries have incomplete time series because the required data were not available for every year.

### Country-Change Dataset

`ncd_analytical_country_change.csv`

This dataset contains one observation per country and summarizes the change between 2000 and 2021.

It is used for the main hypothesis-testing analysis.

The final statistical analysis contains **171 countries** with complete observations for all variables required in the regression analysis.

Using one observation per country avoids treating repeated country-year observations as independent observations in an ordinary cross-sectional regression.

---

### Measuring Change

For NCD mortality, GDP per capita, and health expenditure per capita, percentage change between 2000 and 2021 was calculated as:

**Percentage Change = ((Value in 2021 − Value in 2000) / Value in 2000) × 100**

For urbanization, change was measured in **percentage points**:

**Urbanization Change = Urban Population in 2021 − Urban Population in 2000**

This distinction is important because urbanization is already expressed as a percentage of the population.

---

## Exploratory Analysis

Initial exploratory analysis examined the relationships between NCD mortality and the three explanatory variables.

### Country-Year Analysis

Simple regressions using country-year observations showed negative associations between NCD mortality and:

- Log GDP per capita
- Log health expenditure per capita
- Urban population percentage

A multiple country-year model also showed significant associations for health expenditure and urbanization.

However, country-year observations are repeated measurements from the same countries and therefore are not independent. For this reason, the country-year regression was treated as **exploratory rather than the primary hypothesis-testing model**.

---

## Statistical Analysis

The primary hypothesis-testing analysis uses the country-change dataset.

A multiple linear regression model was used to examine the association between:

**Dependent variable**

- Change in NCD mortality, 2000–2021 (%)

**Independent variables**

- Change in GDP per capita, 2000–2021 (%)
- Change in health expenditure per capita, 2000–2021 (%)
- Change in urban population, 2000–2021 (percentage points)

The model estimates the association between each explanatory variable and NCD mortality change while accounting for the other variables in the model.

### Primary Regression Model

The primary model included **171 countries**.

- R² = **0.115**
- Adjusted R² = **0.099**
- F-test p-value = **0.00043** using heteroscedasticity-robust inference

| Variable | Coefficient | Robust p-value | Interpretation |
|---|---:|---:|---|
| GDP per capita change | -0.0645 | 0.024 | Negative association |
| Health expenditure change | 0.0094 | 0.313 | Not statistically significant |
| Urbanization change | 0.7160 | <0.001 | Positive association |

The coefficients were estimated using heteroscedasticity-robust standard errors (HC3).

### Interpretation of Coefficients

The GDP coefficient of **-0.0645** means that a one percentage-point greater increase in GDP per capita was associated with a **0.0645 percentage-point lower change in NCD mortality**, holding the other variables constant.

The urbanization coefficient of **0.7160** means that a one percentage-point greater increase in urban population share was associated with a **0.716 percentage-point greater change in NCD mortality**, holding the other variables constant.

These coefficients describe statistical associations and should not be interpreted as causal effects.

---

## Sensitivity Analysis

A sensitivity analysis was conducted to examine whether influential observations had a substantial effect on the regression results.

**Cook's distance** was used to identify observations with relatively high influence on the fitted regression model.

Using the common threshold:

**4/n**

with 171 observations, the threshold was approximately:

**0.0234**

Eight observations exceeded this threshold.

These observations were excluded from a separate sensitivity model rather than being automatically removed from the primary analysis.

### Sensitivity Model

After excluding the eight influential observations:

- n = **163**
- R² = **0.118**
- Adjusted R² = **0.102**

| Variable | Coefficient | Robust p-value | Interpretation |
|---|---:|---:|---|
| GDP per capita change | -0.0380 | 0.089 | Not statistically significant |
| Health expenditure change | 0.0028 | 0.647 | Not statistically significant |
| Urbanization change | 0.6605 | <0.001 | Positive and statistically significant |

### Sensitivity Analysis Interpretation

The urbanization association remained statistically significant and similar in magnitude after excluding influential observations.

The GDP association changed from statistically significant in the primary model to non-significant in the sensitivity analysis.

This indicates that the GDP finding is **sensitive to influential observations and should therefore not be considered robust**.

Health expenditure remained non-significant.

---

## Hypothesis Results

### H1 — GDP per Capita

The primary model found a statistically significant negative association between GDP per capita change and NCD mortality change.

However, this association was no longer statistically significant in the sensitivity analysis.

**Conclusion:** The results provide limited and non-robust support for H1.

### H2 — Health Expenditure

Health expenditure per capita was not statistically significant in either the primary or sensitivity model.

**Conclusion:** The analysis does not provide statistical support for H2.

### H3 — Urbanization

Urbanization showed a positive and statistically significant association with NCD mortality change in both the primary and sensitivity models.

**Conclusion:** The results provide the most consistent support for H3.

---

## Overall Statistical Interpretation

The results provide **partial support for the overall research hypothesis**.

Urbanization showed the strongest and most robust association with NCD mortality change. Countries with larger increases in urban population share tended to experience larger increases—or smaller declines—in NCD mortality.

GDP growth was associated with larger declines in NCD mortality in the primary model, but this association was no longer statistically significant in the sensitivity analysis.

Health expenditure showed no statistically significant association with NCD mortality change.

The primary model explained **11.5% of the cross-country variation** in NCD mortality changes. This indicates that these three factors account for only a modest share of the differences between countries and that other factors likely contribute to the observed patterns.

Potential additional factors include:

- Smoking
- Alcohol consumption
- Obesity
- Physical activity
- Air pollution
- Demographic changes
- Healthcare-system characteristics
- Preventive healthcare
- Socioeconomic conditions

The analysis identifies **associations, not causal relationships**.

---

## Tableau Story

The results were presented through an interactive Tableau Story titled:

> **Global NCD Mortality, 2000–2021**

The story contains six main sections.

### 1. The Global Picture

Examines the overall change in average NCD mortality across countries between 2000 and 2021.

Average NCD mortality declined from:

**643.7 → 531.2 deaths per 100,000**

representing a **17.5% decrease**.

The measure is an average across countries and is **not a population-weighted global mortality rate**.

### 2. An Uneven Global Pattern

Examines differences between countries using:

- Top and bottom 10 countries by NCD mortality change
- A world map showing country-level changes

The visualization demonstrates that the overall decline was highly uneven across countries.

### 3. Exploring Factors Associated with NCD Mortality Change

Contains three scatterplots examining the relationships between NCD mortality change and:

- GDP per capita change
- Health expenditure per capita change
- Urbanization change

Urbanization shows the clearest visual association among the three variables.

### 4. What Does the Statistical Analysis Tell Us?

Presents the regression results using coefficient plots with 95% confidence intervals.

The visualization compares:

- Primary model
- Sensitivity model

This allows the stability of the estimated relationships to be assessed visually.

### 5. Statistical Interpretation

The regression results demonstrate that:

- GDP is negative in the primary model but sensitive to influential observations.
- Health expenditure is not statistically significant.
- Urbanization remains positive and statistically significant in both models.

### 6. Key Takeaways

The main conclusions are:

1. NCD mortality declined overall between 2000 and 2021.
2. Progress was highly uneven across countries.
3. The relationships between NCD mortality and the three explanatory factors were mixed.
4. Urbanization showed the strongest and most robust association.
5. GDP showed a non-robust negative association.
6. Health expenditure was not statistically significant.
7. The three variables explain only a modest share of cross-country variation.
8. The findings represent associations rather than causal effects.

---

## Repository Structure

    Global-NCD-Mortality/
    │
    ├── Documentation/
    │   ├── data_cleaning_capstone_detailed.md
    │   ├── data_preparation.md
    │   ├── statistical_analysis_country_change.md
    │   └── statistical_analysis_country_year.md
    │
    ├── Python/
    │   ├── analyze_ncd.py
    │   ├── prepare_gdp_import.py
    │   ├── prepare_health_expenditure.py
    │   ├── prepare_urban_population.py
    │   ├── statistical_analysis_country_change.py
    │   └── statistical_analysis_country_year.py
    │
    ├── SQL/
    │   ├── 01_validation.sql
    │   ├── 02_cross_dataset_validation.sql
    │   └── 03_analytical_datasets.sql
    │
    ├── Tableau/
    │   └── NCD mortality story.twb
    │
    ├── .gitignore
    └── README.md

The raw and processed datasets are not included in the repository.

---

## Tools & Technologies

### Data Processing

- Python
- pandas
- NumPy

### Database & SQL

- PostgreSQL
- SQL
- DBeaver

### Statistical Analysis

- Python
- statsmodels
- Pearson correlation
- Spearman correlation
- Multiple linear regression
- Heteroscedasticity-robust standard errors
- Variance Inflation Factor (VIF)
- Breusch-Pagan test
- Cook's distance
- Sensitivity analysis

### Data Visualization

- Tableau
- Tableau Story
- Interactive dashboards
- Maps
- Scatterplots
- Regression trendlines
- KPI visualizations

### Version Control

- Git
- GitHub

---

## Limitations

Several limitations should be considered when interpreting the results.

### Cross-Country Analysis

The primary regression uses one observation per country representing the change between 2000 and 2021.

This allows countries to be compared consistently but does not model the full year-by-year dynamics of NCD mortality.

### Association Does Not Imply Causation

The regression analysis identifies statistical associations.

It does not establish that changes in GDP, health expenditure, or urbanization directly caused changes in NCD mortality.

### Unmeasured Factors

NCD mortality is influenced by many factors that are not included in this analysis, including behavioral, environmental, demographic, and healthcare-system factors.

### Influential Observations

The GDP result was sensitive to influential observations.

The sensitivity analysis demonstrates why the primary GDP finding should be interpreted cautiously.

### Data Estimates

WHO Global Health Estimates are modeled estimates designed to support international comparisons and may differ from national official estimates.

---

## Project Status

**Completed**

The project includes:

- Data collection
- Data cleaning
- Data validation
- SQL data preparation
- Python analysis
- Statistical hypothesis testing
- Sensitivity analysis
- Tableau dashboards
- Tableau Story
- Project documentation
- GitHub repository

---

## Author

**John Elflein**

Spiced Academy — Data Analytics Capstone Project

2026