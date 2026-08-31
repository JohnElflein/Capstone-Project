import pandas as pd

# Load analytical dataset
df = pd.read_csv("Data/Processed/ncd_analytical_country_year.csv")

# Basic dataset information
print("=== DATASET SHAPE ===")
print(df.shape)

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isna().sum())

print("\n=== DESCRIPTIVE STATISTICS ===")
print(df.describe())

print("\n=== MISSING GDP VALUES ===")
print(
    df[df["gdp_per_capita"].isna()][
        ["country", "code", "year"]
    ].to_string(index=False)
)

print("\n=== MISSING HEALTH EXPENDITURE VALUES ===")
print(
    df[df["health_expenditure_per_capita"].isna()][
        ["country", "code", "year"]
    ].to_string(index=False)
)

print("\n=== COMPLETE CASES ===")
complete = df[
    df["gdp_per_capita"].notna()
    & df["health_expenditure_per_capita"].notna()
    & df["urban_population_pct"].notna()
    & df["ncd_mortality_rate"].notna()
]

print("Complete observations:", len(complete))
print("Complete countries:", complete["code"].nunique())

# ============================================================
# UNIVARIATE EXPLORATORY DATA ANALYSIS
# ============================================================

variables = [
    "ncd_mortality_rate",
    "gdp_per_capita",
    "health_expenditure_per_capita",
    "urban_population_pct"
]

print("\n=== UNIVARIATE EDA ===")

for var in variables:
    print(f"\n--- {var} ---")
    print(f"Mean:   {df[var].mean():.2f}")
    print(f"Median: {df[var].median():.2f}")
    print(f"Std:    {df[var].std():.2f}")
    print(f"Min:    {df[var].min():.2f}")
    print(f"Max:    {df[var].max():.2f}")
    print(f"Skew:   {df[var].skew():.2f}")

    import matplotlib.pyplot as plt

# ============================================================
# DISTRIBUTION PLOTS
# ============================================================

for var in variables:
    plt.figure(figsize=(8, 5))
    plt.hist(df[var].dropna(), bins=30)
    plt.title(f"Distribution of {var}")
    plt.xlabel(var)
    plt.ylabel("Number of observations")
    plt.tight_layout()
    plt.show()

# ============================================================
# LOG TRANSFORMATIONS
# ============================================================

import numpy as np

df["log_gdp_per_capita"] = np.log(df["gdp_per_capita"])
df["log_health_expenditure"] = np.log(
    df["health_expenditure_per_capita"]
)

print("\n=== LOG-TRANSFORMED VARIABLES ===")

for var in ["log_gdp_per_capita", "log_health_expenditure"]:
    print(f"\n--- {var} ---")
    print(f"Mean:   {df[var].mean():.2f}")
    print(f"Median: {df[var].median():.2f}")
    print(f"Std:    {df[var].std():.2f}")
    print(f"Min:    {df[var].min():.2f}")
    print(f"Max:    {df[var].max():.2f}")
    print(f"Skew:   {df[var].skew():.2f}")

# ============================================================
# BIVARIATE EDA
# ============================================================

print("\n=== BIVARIATE EDA ===")

# Use complete cases for the variables needed in the analysis
eda_df = df[
    [
        "ncd_mortality_rate",
        "gdp_per_capita",
        "health_expenditure_per_capita",
        "urban_population_pct",
        "log_gdp_per_capita",
        "log_health_expenditure"
    ]
].dropna()

print(f"\nComplete observations used for bivariate analysis: {len(eda_df)}")

# ------------------------------------------------------------
# Pearson correlations
# ------------------------------------------------------------

print("\n--- Pearson correlations with NCD mortality ---")

print(
    "NCD mortality vs log GDP per capita:",
    eda_df["ncd_mortality_rate"].corr(
        eda_df["log_gdp_per_capita"],
        method="pearson"
    )
)

print(
    "NCD mortality vs log health expenditure:",
    eda_df["ncd_mortality_rate"].corr(
        eda_df["log_health_expenditure"],
        method="pearson"
    )
)

print(
    "NCD mortality vs urban population:",
    eda_df["ncd_mortality_rate"].corr(
        eda_df["urban_population_pct"],
        method="pearson"
    )
)

# ------------------------------------------------------------
# Spearman correlations
# ------------------------------------------------------------

print("\n--- Spearman correlations with NCD mortality ---")

print(
    "NCD mortality vs log GDP per capita:",
    eda_df["ncd_mortality_rate"].corr(
        eda_df["log_gdp_per_capita"],
        method="spearman"
    )
)

print(
    "NCD mortality vs log health expenditure:",
    eda_df["ncd_mortality_rate"].corr(
        eda_df["log_health_expenditure"],
        method="spearman"
    )
)

print(
    "NCD mortality vs urban population:",
    eda_df["ncd_mortality_rate"].corr(
        eda_df["urban_population_pct"],
        method="spearman"
    )
)

# ============================================================
# SCATTERPLOTS
# ============================================================

# NCD mortality vs log GDP per capita
plt.figure(figsize=(8, 6))
plt.scatter(
    eda_df["log_gdp_per_capita"],
    eda_df["ncd_mortality_rate"],
    alpha=0.4
)
plt.xlabel("Log GDP per capita")
plt.ylabel("NCD mortality rate")
plt.title("NCD Mortality Rate vs Log GDP per Capita")
plt.tight_layout()
plt.show()


# NCD mortality vs log health expenditure
plt.figure(figsize=(8, 6))
plt.scatter(
    eda_df["log_health_expenditure"],
    eda_df["ncd_mortality_rate"],
    alpha=0.4
)
plt.xlabel("Log Health Expenditure per Capita")
plt.ylabel("NCD mortality rate")
plt.title("NCD Mortality Rate vs Log Health Expenditure")
plt.tight_layout()
plt.show()


# NCD mortality vs urban population
plt.figure(figsize=(8, 6))
plt.scatter(
    eda_df["urban_population_pct"],
    eda_df["ncd_mortality_rate"],
    alpha=0.4
)
plt.xlabel("Urban Population (%)")
plt.ylabel("NCD mortality rate")
plt.title("NCD Mortality Rate vs Urban Population")
plt.tight_layout()
plt.show()

# ============================================================
# CORRELATION AMONG EXPLANATORY VARIABLES
# ============================================================

print("\n=== CORRELATION AMONG EXPLANATORY VARIABLES ===")

predictor_df = eda_df[
    [
        "log_gdp_per_capita",
        "log_health_expenditure",
        "urban_population_pct"
    ]
]

print("\n--- Pearson correlation matrix ---")
print(predictor_df.corr(method="pearson").round(3))

print("\n--- Spearman correlation matrix ---")
print(predictor_df.corr(method="spearman").round(3))

# ============================================================
# SIMPLE LINEAR REGRESSION
# ============================================================

import statsmodels.api as sm


print("\n=== SIMPLE LINEAR REGRESSION ===")

# Use complete cases for each model

# ------------------------------------------------------------
# Model 1: NCD mortality vs log GDP per capita
# ------------------------------------------------------------

model_data = df[
    ["ncd_mortality_rate", "log_gdp_per_capita"]
].dropna()

X = sm.add_constant(model_data["log_gdp_per_capita"])
y = model_data["ncd_mortality_rate"]

model_gdp = sm.OLS(y, X).fit()

print("\n--- Model 1: NCD mortality vs log GDP per capita ---")
print(model_gdp.summary())


# ------------------------------------------------------------
# Model 2: NCD mortality vs log health expenditure
# ------------------------------------------------------------

model_data = df[
    ["ncd_mortality_rate", "log_health_expenditure"]
].dropna()

X = sm.add_constant(model_data["log_health_expenditure"])
y = model_data["ncd_mortality_rate"]

model_health = sm.OLS(y, X).fit()

print("\n--- Model 2: NCD mortality vs log health expenditure ---")
print(model_health.summary())


# ------------------------------------------------------------
# Model 3: NCD mortality vs urban population
# ------------------------------------------------------------

model_data = df[
    ["ncd_mortality_rate", "urban_population_pct"]
].dropna()

X = sm.add_constant(model_data["urban_population_pct"])
y = model_data["ncd_mortality_rate"]

model_urban = sm.OLS(y, X).fit()

print("\n--- Model 3: NCD mortality vs urban population ---")
print(model_urban.summary())

# ============================================================
# MULTIPLE LINEAR REGRESSION
# ============================================================

print("\n=== MULTIPLE LINEAR REGRESSION ===")

# Use complete cases for all variables in the model
regression_df = df[
    [
        "ncd_mortality_rate",
        "log_gdp_per_capita",
        "log_health_expenditure",
        "urban_population_pct"
    ]
].dropna()

# Define dependent variable
y = regression_df["ncd_mortality_rate"]

# Define explanatory variables
X = regression_df[
    [
        "log_gdp_per_capita",
        "log_health_expenditure",
        "urban_population_pct"
    ]
]

# Add intercept
X = sm.add_constant(X)

# Fit model
multiple_model = sm.OLS(y, X).fit()

print(multiple_model.summary())


# ============================================================
# MULTICOLLINEARITY — VARIANCE INFLATION FACTOR (VIF)
# ============================================================

print("\n=== MULTICOLLINEARITY (VIF) ===")

from statsmodels.stats.outliers_influence import variance_inflation_factor

# Use the same observations as the multiple regression
vif_df = regression_df[
    [
        "log_gdp_per_capita",
        "log_health_expenditure",
        "urban_population_pct"
    ]
].copy()

# Add intercept
vif_X = sm.add_constant(vif_df)

# Calculate VIF for each explanatory variable
vif_results = pd.DataFrame()
vif_results["variable"] = vif_X.columns
vif_results["VIF"] = [
    variance_inflation_factor(vif_X.values, i)
    for i in range(vif_X.shape[1])
]

print(vif_results)

# ============================================================
# HETEROSCEDASTICITY — BREUSCH-PAGAN TEST
# ============================================================

print("\n=== HETEROSCEDASTICITY (BREUSCH-PAGAN TEST) ===")

from statsmodels.stats.diagnostic import het_breuschpagan

# Calculate Breusch-Pagan test
bp_test = het_breuschpagan(
    multiple_model.resid,
    multiple_model.model.exog
)

bp_labels = [
    "LM Statistic",
    "LM-Test p-value",
    "F Statistic",
    "F-Test p-value"
]

for label, value in zip(bp_labels, bp_test):
    print(f"{label}: {value}")

# ============================================================
# MULTIPLE LINEAR REGRESSION WITH ROBUST STANDARD ERRORS
# ============================================================

print("\n=== MULTIPLE LINEAR REGRESSION (HC3 ROBUST SE) ===")

# Use the same complete-case dataset as the original regression
y = regression_df["ncd_mortality_rate"]

X = regression_df[
    [
        "log_gdp_per_capita",
        "log_health_expenditure",
        "urban_population_pct"
    ]
]

X = sm.add_constant(X)

# Fit OLS with HC3 heteroscedasticity-robust standard errors
model_robust = sm.OLS(y, X).fit(cov_type="HC3")

print(model_robust.summary())

# ============================================================
# PANEL STRUCTURE CHECK
# ============================================================

print("\n=== PANEL STRUCTURE ===")

# Number of observations per country
obs_per_country = df.groupby("code")["year"].agg(
    observations="count",
    min_year="min",
    max_year="max"
)

print("\n--- Observations per country ---")
print(obs_per_country["observations"].describe())

# Countries with fewer than 22 observations
incomplete_countries = obs_per_country[
    obs_per_country["observations"] < 22
]

print("\n--- Countries with fewer than 22 observations ---")
print(incomplete_countries)

# Countries with the full 2000–2021 period
complete_panel = obs_per_country[
    (obs_per_country["observations"] == 22) &
    (obs_per_country["min_year"] == 2000) &
    (obs_per_country["max_year"] == 2021)
]

print("\n--- Complete panels ---")
print("Countries with complete 2000–2021 data:", len(complete_panel))

# Overall year coverage
print("\n--- Observations by year ---")
print(df.groupby("year")["code"].nunique().to_string())

# Countries represented in the dataset
print("\n--- Total countries ---")
print("Countries:", df["code"].nunique())

# Country-year duplicates
duplicates = df.duplicated(
    subset=["code", "year"]
).sum()

print("\n--- Duplicate country-year observations ---")
print("Duplicates:", duplicates)