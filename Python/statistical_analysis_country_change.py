import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# ============================================================
# 1. LOAD DATA
# ============================================================

file_path = "Data/Processed/ncd_analytical_country_change.csv"


df = pd.read_csv(file_path)

print("=== DATASET SHAPE ===")
print(df.shape)

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATE COUNTRIES ===")
print(df["code"].duplicated().sum())

print("\n=== DESCRIPTIVE STATISTICS ===")
print(df.describe().round(2))

# ============================================================
# 2. UNIVARIATE EDA
# ============================================================

import matplotlib.pyplot as plt
from scipy.stats import skew

variables = {
    "ncd_mortality_pct_change": "NCD mortality % change",
    "gdp_pct_change": "GDP per capita % change",
    "health_expenditure_pct_change": "Health expenditure per capita % change",
    "urban_population_pct_point_change": "Urban population percentage-point change"
}

print("\n=== UNIVARIATE EDA ===")

for var, label in variables.items():

    series = df[var]

    print(f"\n--- {label} ---")
    print(f"Mean:   {series.mean():.2f}")
    print(f"Median: {series.median():.2f}")
    print(f"Std:    {series.std():.2f}")
    print(f"Min:    {series.min():.2f}")
    print(f"Max:    {series.max():.2f}")
    print(f"Skew:   {skew(series):.2f}")

    plt.figure(figsize=(8, 5))
    plt.hist(series, bins=30)
    plt.title(f"Distribution of {label}")
    plt.xlabel(label)
    plt.ylabel("Number of countries")
    plt.tight_layout()
    plt.show()

# ============================================================
# 3. BIVARIATE EDA
# ============================================================

from scipy.stats import pearsonr, spearmanr

outcome = "ncd_mortality_pct_change"

predictors = {
    "gdp_pct_change": "GDP per capita % change",
    "health_expenditure_pct_change": "Health expenditure per capita % change",
    "urban_population_pct_point_change": "Urban population percentage-point change"
}

print("\n=== BIVARIATE EDA ===")

for var, label in predictors.items():

    x = df[var]
    y = df[outcome]

    pearson_r, pearson_p = pearsonr(x, y)
    spearman_r, spearman_p = spearmanr(x, y)

    print(f"\n--- NCD mortality vs {label} ---")

    print(f"Pearson correlation:  r = {pearson_r:.3f}, p = {pearson_p:.4f}")
    print(f"Spearman correlation: r = {spearman_r:.3f}, p = {spearman_p:.4f}")

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, alpha=0.6)

    plt.title(f"NCD Mortality Change vs {label}")
    plt.xlabel(label)
    plt.ylabel("NCD mortality % change")

    plt.tight_layout()
    plt.show()

# ============================================================
# MULTICOLLINEARITY (VIF) — COUNTRY CHANGE DATA
# ============================================================

print("\n=== MULTICOLLINEARITY (VIF) ===")

from statsmodels.stats.outliers_influence import variance_inflation_factor

# Define explanatory variables
X_vif = df[
    [
        "gdp_pct_change",
        "health_expenditure_pct_change",
        "urban_population_pct_point_change"
    ]
].dropna()

# Add constant
X_vif = sm.add_constant(X_vif)

# Calculate VIF
vif_data = pd.DataFrame()
vif_data["variable"] = X_vif.columns
vif_data["VIF"] = [
    variance_inflation_factor(X_vif.values, i)
    for i in range(X_vif.shape[1])
]

print(vif_data)

# ============================================================
# MULTIPLE LINEAR REGRESSION — COUNTRY CHANGE DATA
# ============================================================

print("\n=== MULTIPLE LINEAR REGRESSION ===")

# Define variables
regression_df = df[
    [
        "ncd_mortality_pct_change",
        "gdp_pct_change",
        "health_expenditure_pct_change",
        "urban_population_pct_point_change"
    ]
].dropna()

# Dependent variable
y = regression_df["ncd_mortality_pct_change"]

# Explanatory variables
X = regression_df[
    [
        "gdp_pct_change",
        "health_expenditure_pct_change",
        "urban_population_pct_point_change"
    ]
]

# Add constant
X = sm.add_constant(X)

# Fit OLS model
model_change = sm.OLS(y, X).fit()

print(model_change.summary())

# ============================================================
# REGRESSION DIAGNOSTICS — HETEROSCEDASTICITY
# ============================================================

from statsmodels.stats.diagnostic import het_breuschpagan

print("\n=== HETEROSCEDASTICITY (BREUSCH-PAGAN TEST) ===")

# Calculate Breusch-Pagan test
bp_test = het_breuschpagan(
    model_change.resid,
    model_change.model.exog
)

labels = [
    "LM Statistic",
    "LM-Test p-value",
    "F Statistic",
    "F-Test p-value"
]

for label, value in zip(labels, bp_test):
    print(f"{label}: {value}")

# ============================================================
# REGRESSION DIAGNOSTICS — INFLUENTIAL OBSERVATIONS
# ============================================================

from statsmodels.stats.outliers_influence import OLSInfluence

print("\n=== INFLUENTIAL OBSERVATIONS (COOK'S DISTANCE) ===")

# Calculate influence statistics
influence = OLSInfluence(model_change)

# Cook's distance
cooks_distance = influence.cooks_distance[0]

# Add Cook's distance to a copy of the regression data
influence_df = regression_df.copy()
influence_df["cooks_distance"] = cooks_distance

# Sort by Cook's distance
influence_df = influence_df.sort_values(
    "cooks_distance",
    ascending=False
)

print("\nTop 10 observations by Cook's distance:")

print(
    influence_df[
        [
            "cooks_distance",
            "ncd_mortality_pct_change",
            "gdp_pct_change",
            "health_expenditure_pct_change",
            "urban_population_pct_point_change"
        ]
    ].head(10)
)

# Common rule-of-thumb threshold
threshold = 4 / len(regression_df)

print(f"\nCook's distance threshold (4/n): {threshold:.4f}")

print(
    f"Observations above threshold: "
    f"{(cooks_distance > threshold).sum()}"
)

# ============================================================
# IDENTIFY INFLUENTIAL COUNTRIES
# ============================================================

print("\n=== MOST INFLUENTIAL COUNTRIES ===")

influence_df = regression_df.copy()
influence_df["cooks_distance"] = cooks_distance

influence_df = influence_df.sort_values(
    "cooks_distance",
    ascending=False
)

# Add country names using the original dataframe index
influence_df["country"] = df.loc[
    influence_df.index,
    "country"
]

print(
    influence_df[
        [
            "country",
            "cooks_distance",
            "ncd_mortality_pct_change",
            "gdp_pct_change",
            "health_expenditure_pct_change",
            "urban_population_pct_point_change"
        ]
    ].head(10)
)

# ============================================================
# REGRESSION DIAGNOSTICS — RESIDUALS
# ============================================================

print("\n=== RESIDUAL DIAGNOSTICS ===")

residuals = model_change.resid
fitted = model_change.fittedvalues

print(f"Mean residual: {residuals.mean():.4f}")
print(f"Std residual: {residuals.std():.4f}")
print(f"Min residual: {residuals.min():.4f}")
print(f"Max residual: {residuals.max():.4f}")

# Residuals vs fitted values
plt.figure(figsize=(8, 5))
plt.scatter(fitted, residuals, alpha=0.6)

plt.axhline(y=0, linestyle="--")

plt.title("Residuals vs Fitted Values")
plt.xlabel("Fitted NCD mortality % change")
plt.ylabel("Residuals")

plt.tight_layout()
plt.show()

# Histogram of residuals
plt.figure(figsize=(8, 5))
plt.hist(residuals, bins=30)

plt.title("Distribution of Regression Residuals")
plt.xlabel("Residual")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# ============================================================
# MULTIPLE LINEAR REGRESSION (HC3 ROBUST SE)
# ============================================================

print("\n=== MULTIPLE LINEAR REGRESSION (HC3 ROBUST SE) ===")

# Use the same complete cases as the original regression
regression_df = df[
    [
        "ncd_mortality_pct_change",
        "gdp_pct_change",
        "health_expenditure_pct_change",
        "urban_population_pct_point_change"
    ]
].dropna()

# Dependent variable
y = regression_df["ncd_mortality_pct_change"]

# Explanatory variables
X = regression_df[
    [
        "gdp_pct_change",
        "health_expenditure_pct_change",
        "urban_population_pct_point_change"
    ]
]

# Add intercept
X = sm.add_constant(X)

# Fit OLS model with HC3 robust standard errors
model_hc3 = sm.OLS(y, X).fit(cov_type="HC3")

print(model_hc3.summary())

# ============================================================
# SENSITIVITY ANALYSIS: EXCLUDING INFLUENTIAL OBSERVATIONS
# ============================================================

print("\n=== SENSITIVITY ANALYSIS: EXCLUDING INFLUENTIAL OBSERVATIONS ===")

# Calculate Cook's distance for the original OLS model
influence = model_change.get_influence()
cooks_d = influence.cooks_distance[0]

# Define Cook's distance threshold
n = len(regression_df)
cooks_threshold = 4 / n

# Identify influential observations
influential = cooks_d > cooks_threshold

print(f"Cook's distance threshold: {cooks_threshold:.4f}")
print(f"Influential observations excluded: {influential.sum()}")

# Remove influential observations
sensitivity_df = regression_df.loc[~influential].copy()

print(f"Observations remaining: {len(sensitivity_df)}")

# Define dependent variable
y_sensitivity = sensitivity_df["ncd_mortality_pct_change"]

# Define explanatory variables
X_sensitivity = sensitivity_df[
    [
        "gdp_pct_change",
        "health_expenditure_pct_change",
        "urban_population_pct_point_change"
    ]
]

# Add intercept
X_sensitivity = sm.add_constant(X_sensitivity)

# Fit sensitivity model with HC3 robust standard errors
model_sensitivity = sm.OLS(
    y_sensitivity,
    X_sensitivity
).fit(cov_type="HC3")

print(model_sensitivity.summary())

# ============================================================
# FINAL MODEL COMPARISON
# ============================================================

print("\n=== FINAL MODEL COMPARISON ===")

# Extract results from the primary HC3 model
primary_results = pd.DataFrame({
    "variable": model_hc3.params.index,
    "coefficient_primary": model_hc3.params.values,
    "p_value_primary": model_hc3.pvalues.values,
    "ci_lower_primary": model_hc3.conf_int()[0].values,
    "ci_upper_primary": model_hc3.conf_int()[1].values
})

# Extract results from the sensitivity HC3 model
sensitivity_results = pd.DataFrame({
    "variable": model_sensitivity.params.index,
    "coefficient_sensitivity": model_sensitivity.params.values,
    "p_value_sensitivity": model_sensitivity.pvalues.values,
    "ci_lower_sensitivity": model_sensitivity.conf_int()[0].values,
    "ci_upper_sensitivity": model_sensitivity.conf_int()[1].values
})

# Combine the two models
comparison = primary_results.merge(
    sensitivity_results,
    on="variable"
)

# Remove intercept from hypothesis comparison
comparison = comparison[
    comparison["variable"] != "const"
]

# Display results
print(comparison.to_string(index=False))

# Model-level statistics
print("\n=== MODEL-LEVEL STATISTICS ===")

print(f"Primary model observations: {int(model_hc3.nobs)}")
print(f"Primary model R-squared: {model_hc3.rsquared:.3f}")
print(f"Primary model adjusted R-squared: {model_hc3.rsquared_adj:.3f}")

print(f"Sensitivity model observations: {int(model_sensitivity.nobs)}")
print(f"Sensitivity model R-squared: {model_sensitivity.rsquared:.3f}")
print(f"Sensitivity model adjusted R-squared: {model_sensitivity.rsquared_adj:.3f}")