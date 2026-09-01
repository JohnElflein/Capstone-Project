# Statistical Analysis — Country Change Dataset

## 1. Purpose and Research Question

This analysis uses the `ncd_analytical_country_change.csv` dataset to examine whether changes in economic development, healthcare expenditure, and urbanization were associated with changes in NCD mortality between 2000 and 2021.

The main research question is:

> **How has NCD mortality changed across countries between 2000 and 2021, and how are economic development, healthcare expenditure, and urbanization associated with these changes?**

For the inferential analysis, the focus is specifically on changes between 2000 and 2021 rather than individual yearly observations.

The overall research hypothesis is:

> **Economic development, healthcare expenditure, and urbanization are significantly associated with changes in NCD mortality across countries between 2000 and 2021.**

### Specific hypotheses

#### H1 — GDP per capita

**H₀:** Change in GDP per capita is not significantly associated with change in NCD mortality.

**H₁:** Change in GDP per capita is significantly associated with change in NCD mortality.

#### H2 — Health expenditure per capita

**H₀:** Change in health expenditure per capita is not significantly associated with change in NCD mortality.

**H₁:** Change in health expenditure per capita is significantly associated with change in NCD mortality.

#### H3 — Urbanization

**H₀:** Change in urban population is not significantly associated with change in NCD mortality.

**H₁:** Change in urban population is significantly associated with change in NCD mortality.

---

## 2. Dataset Overview and Data Quality

The country-change dataset contains one observation per country, with variables representing values in 2000, values in 2021, and calculated changes between the two years.

### Dataset shape

- **Observations:** 171 countries
- **Variables:** 14

### Variables

| Variable | Description |
|---|---|
| `country` | Country name |
| `code` | ISO country code |
| `ncd_mortality_2000` | NCD mortality rate in 2000 |
| `ncd_mortality_2021` | NCD mortality rate in 2021 |
| `ncd_mortality_pct_change` | Percentage change in NCD mortality between 2000 and 2021 |
| `gdp_2000` | GDP per capita in 2000 |
| `gdp_2021` | GDP per capita in 2021 |
| `gdp_pct_change` | Percentage change in GDP per capita |
| `health_expenditure_2000` | Health expenditure per capita in 2000 |
| `health_expenditure_2021` | Health expenditure per capita in 2021 |
| `health_expenditure_pct_change` | Percentage change in health expenditure per capita |
| `urban_population_2000` | Urban population percentage in 2000 |
| `urban_population_2021` | Urban population percentage in 2021 |
| `urban_population_pct_point_change` | Percentage-point change in urban population |

### Missing values

No missing values were present in any of the 14 variables.

This means all 171 countries could be included in the initial analysis without requiring missing-value imputation.

### Duplicate countries

There were **0 duplicate countries**.

Therefore, the dataset contains one observation for each country.

---

## 3. Descriptive Statistics

Descriptive statistics were calculated to understand the distribution and magnitude of changes between 2000 and 2021 before conducting inferential statistical tests.

## 3.1 NCD Mortality

| Statistic | Value |
|---|---:|
| Mean 2000 | 642.65 |
| Mean 2021 | 523.09 |
| Mean % change | −17.98% |
| Median % change | −20.18% |
| Standard deviation | 16.71 |
| Minimum % change | −57.22% |
| Maximum % change | 62.26% |
| Skewness | 1.02 |

On average, NCD mortality decreased by **17.98%** between 2000 and 2021.

The median decrease was slightly larger at **20.18%**, indicating that more than half of countries experienced a decline in NCD mortality.

However, the range was substantial. The largest decrease was **57.22%**, while the largest increase was **62.26%**.

The positive skewness of **1.02** indicates that the distribution contains some countries with relatively large increases in NCD mortality.

---

## 3.2 GDP per Capita

| Statistic | Value |
|---|---:|
| Mean % change | 63.11% |
| Median % change | 38.68% |
| Standard deviation | 69.70 |
| Minimum % change | −40.24% |
| Maximum % change | 412.64% |
| Skewness | 1.60 |

GDP per capita increased by an average of **63.11%** between 2000 and 2021.

The median increase was **38.68%**, indicating substantial variation between countries.

The range was very large, from a **40.24% decrease** to a **412.64% increase**.

The skewness of **1.60** indicates a strongly right-skewed distribution, with some countries experiencing exceptionally large percentage increases in GDP per capita.

---

## 3.3 Health Expenditure per Capita

| Statistic | Value |
|---|---:|
| Mean % change | 281.41% |
| Median % change | 219.30% |
| Standard deviation | 240.53 |
| Minimum % change | −67.83% |
| Maximum % change | 1750.37% |
| Skewness | 2.40 |

Health expenditure per capita increased substantially between 2000 and 2021.

The mean increase was **281.41%**, while the median increase was **219.30%**.

The distribution was highly variable, ranging from a **67.83% decrease** to an increase of **1750.37%**.

The skewness of **2.40** indicates a strongly right-skewed distribution, with some countries experiencing exceptionally large percentage increases.

---

## 3.4 Urbanization

Urbanization was measured as the percentage of the population living in urban areas. Because this is already a percentage, change was measured in **percentage points** rather than percentage change.

| Statistic | Value |
|---|---:|
| Mean change | +7.19 percentage points |
| Median change | +5.77 percentage points |
| Standard deviation | 7.30 |
| Minimum change | −7.66 percentage points |
| Maximum change | +35.04 percentage points |
| Skewness | 1.05 |

The average urban population share increased by **7.19 percentage points** between 2000 and 2021.

The median increase was **5.77 percentage points**.

Most countries therefore experienced an increase in urbanization, although changes varied considerably across countries.

---

## 4. Univariate Exploratory Data Analysis

Univariate EDA was conducted using summary statistics and visualizations to examine the distribution of each change variable.

The analysis showed that:

- NCD mortality change was moderately right-skewed (**skew = 1.02**).
- GDP percentage change was strongly right-skewed (**skew = 1.60**).
- Health expenditure percentage change was highly right-skewed (**skew = 2.40**).
- Urbanization change was moderately right-skewed (**skew = 1.05**).

The strong skewness of GDP and especially health expenditure indicates that percentage changes are not normally distributed across countries. This is important when interpreting correlation and regression results and when examining influential observations.

Because the objective of the analysis is to examine changes between two time points, the original percentage-change variables were retained rather than transforming them at this stage.

---

## 5. Bivariate EDA

Bivariate analysis was conducted to examine the relationship between the change in NCD mortality and each explanatory variable individually.

Both **Pearson** and **Spearman** correlation coefficients were calculated.

Pearson correlation measures the strength of a linear relationship, while Spearman correlation measures the strength of a monotonic relationship based on the ranks of observations. Using both provides a useful check given the skewed distributions of several variables.

## 5.1 NCD Mortality and GDP Change

### Pearson correlation

- **r = −0.139**
- **p = 0.0690**

The Pearson correlation indicates a weak negative relationship between GDP percentage change and NCD mortality percentage change.

However, the p-value of **0.0690** is greater than 0.05, so the relationship was not statistically significant at the conventional 5% significance level.

### Spearman correlation

- **r = −0.061**
- **p = 0.4311**

The Spearman correlation was also negative but very weak and not statistically significant.

Overall, the bivariate analysis provides little evidence of a strong relationship between GDP growth and changes in NCD mortality.

---

## 5.2 NCD Mortality and Health Expenditure Change

### Pearson correlation

- **r = −0.072**
- **p = 0.3461**

The Pearson correlation indicates a very weak negative relationship that was not statistically significant.

### Spearman correlation

- **r = −0.124**
- **p = 0.1074**

The Spearman correlation was also negative but did not reach statistical significance.

Overall, there was no statistically significant bivariate association between changes in health expenditure per capita and changes in NCD mortality.

---

## 5.3 NCD Mortality and Urbanization Change

### Pearson correlation

- **r = 0.280**
- **p = 0.0002**

The Pearson correlation indicates a moderate positive relationship between urbanization change and NCD mortality change.

The p-value of **0.0002** indicates that this relationship is statistically significant.

### Spearman correlation

- **r = 0.291**
- **p = 0.0001**

The Spearman correlation produced a very similar result.

The consistency between Pearson and Spearman correlations suggests that the positive relationship is not simply the result of a small number of extreme values.

Overall, urbanization was the only explanatory variable to show a statistically significant bivariate association with NCD mortality change.

---

## 6. Multicollinearity

Before estimating the multiple regression model, multicollinearity was assessed using the **Variance Inflation Factor (VIF)**.

VIF measures how strongly an explanatory variable is correlated with the other explanatory variables in a regression model.

The results were:

| Variable | VIF |
|---|---:|
| GDP % change | 2.177 |
| Health expenditure % change | 2.159 |
| Urbanization percentage-point change | 1.040 |

The VIF values are relatively low and do not indicate problematic multicollinearity.

In particular, GDP growth and health expenditure growth had VIF values of approximately **2.2**, while urbanization had a VIF close to **1**.

This is substantially different from the country-year analysis, where GDP and health expenditure were strongly correlated across individual country-year observations.

The country-change dataset therefore provides a much cleaner basis for estimating a multiple regression model using the three changes as explanatory variables.

The constant had a VIF of **3.474**, but the VIF of the intercept is not generally used when assessing multicollinearity among explanatory variables.

---

## 7. Multiple Linear Regression

A multiple linear regression model was estimated to examine the association between changes in the three explanatory variables and changes in NCD mortality while controlling for the other explanatory variables.

The model was specified as:

**NCD mortality % change = β₀ + β₁(GDP % change) + β₂(health expenditure % change) + β₃(urbanization change) + ε**

The dependent variable was:

- `ncd_mortality_pct_change`

The explanatory variables were:

- `gdp_pct_change`
- `health_expenditure_pct_change`
- `urban_population_pct_point_change`

The model included **171 countries**.

The initial OLS model produced:

- **R² = 0.115**
- **Adjusted R² = 0.099**
- **F-statistic = 7.240**
- **F-test p-value = 0.000135**

The model as a whole was statistically significant.

The R² of **0.115** means that approximately **11.5% of the cross-country variation in NCD mortality percentage change** was explained by the three explanatory variables together.

The adjusted R² of **0.099** accounts for the number of explanatory variables included in the model.

Because heteroscedasticity was subsequently assessed, the final interpretation uses HC3 heteroscedasticity-robust standard errors.

---

## 8. Heteroscedasticity

The **Breusch–Pagan test** was used to assess whether the variance of the regression residuals differed systematically across observations.

The results were:

- LM Statistic = **4.872**
- LM-test p-value = **0.1814**
- F Statistic = **1.633**
- F-test p-value = **0.1838**

Both p-values were greater than 0.05.

Therefore, the Breusch–Pagan test did **not provide statistically significant evidence of heteroscedasticity**.

Nevertheless, the final regression model was estimated using **HC3 robust standard errors**. This provides additional protection against possible heteroscedasticity and is a conservative approach for cross-country data.

Importantly, using HC3 standard errors does not change the regression coefficients or R². It changes the estimated standard errors, confidence intervals, test statistics, and p-values.

---

## 9. Primary Multiple Regression with HC3 Robust Standard Errors

The final primary model used heteroscedasticity-robust HC3 standard errors.

### Results

| Variable | Coefficient | p-value | 95% CI |
|---|---:|---:|---:|
| GDP % change | −0.0645 | 0.024 | −0.120 to −0.009 |
| Health expenditure % change | +0.0094 | 0.313 | −0.009 to +0.028 |
| Urbanization change | +0.7160 | <0.001 | +0.343 to +1.089 |

The model had:

- **171 observations**
- **R² = 0.115**
- **Adjusted R² = 0.099**

---

## 9.1 GDP per Capita

GDP percentage change had a coefficient of:

**β = −0.0645**

with:

**p = 0.024**

and a 95% confidence interval of:

**−0.120 to −0.009**

The negative coefficient indicates that greater increases in GDP per capita were associated with larger decreases in NCD mortality percentage change, after controlling for changes in health expenditure and urbanization.

The p-value of 0.024 is below 0.05, meaning the association was statistically significant in the primary model.

The confidence interval does not include zero, which is consistent with statistical significance.

However, this result must be interpreted cautiously because the subsequent influence analysis showed that the GDP coefficient was sensitive to influential observations.

---

## 9.2 Health Expenditure per Capita

Health expenditure percentage change had a coefficient of:

**β = +0.0094**

with:

**p = 0.313**

and a 95% confidence interval of:

**−0.009 to +0.028**

The coefficient was positive but very small.

The p-value of 0.313 is substantially greater than 0.05, and the confidence interval includes zero.

Therefore, there was no statistically significant evidence that changes in health expenditure per capita were associated with changes in NCD mortality after controlling for GDP growth and urbanization.

---

## 9.3 Urbanization

Urban population percentage-point change had a coefficient of:

**β = +0.7160**

with:

**p < 0.001**

and a 95% confidence interval of:

**+0.343 to +1.089**

The positive coefficient indicates that countries experiencing greater increases in urbanization tended to experience less favorable changes in NCD mortality.

Specifically, a one-percentage-point increase in the urban population share was associated with an estimated **0.716 percentage-point higher change in NCD mortality**, holding GDP growth and health expenditure growth constant.

The relationship was highly statistically significant.

The confidence interval also remains entirely above zero.

---

## 10. Influential Observations — Cook's Distance

Cook's distance was used to identify observations that had a potentially large influence on the estimated regression model.

Cook's distance considers both the residual of an observation and its influence on the fitted regression coefficients.

The commonly used threshold of:

**4/n**

was applied.

With 171 observations:

**4 / 171 = 0.0234**

Eight observations exceeded this threshold.

The most influential observations were:

| Country | Cook's distance | NCD mortality % change | GDP % change | Health expenditure % change | Urbanization change |
|---|---:|---:|---:|---:|---:|
| Mozambique | 0.2527 | +24.07% | +104.67% | +1146.31% | +5.21 |
| Equatorial Guinea | 0.1105 | −24.00% | +42.95% | +558.29% | +31.83 |
| Philippines | 0.0907 | +62.26% | +86.86% | +414.73% | +15.31 |
| Lesotho | 0.0651 | +35.60% | +31.71% | +305.37% | +21.33 |
| China | 0.0470 | −32.80% | +412.64% | +732.67% | +28.29 |
| India | 0.0377 | +4.83% | +159.72% | +213.85% | +6.80 |
| Azerbaijan | 0.0370 | −50.20% | +255.52% | +850.55% | +7.23 |
| Jamaica | 0.0237 | +30.95% | +7.89% | +98.33% | +5.82 |

The influential observations include countries with unusually large changes in GDP, health expenditure, urbanization, or NCD mortality.

These observations were not automatically removed from the primary analysis. Instead, they were retained and a sensitivity analysis was conducted to determine whether the main conclusions depended heavily on them.

---

## 11. Residual Diagnostics

Residual diagnostics were used to assess the behavior of the regression errors.

For the primary model:

- Mean residual = **0.0000**
- Standard deviation = **15.7235**
- Minimum residual = **−35.1736**
- Maximum residual = **74.6910**

The mean residual being essentially zero is expected for an OLS model with an intercept.

The residual distribution also showed some departure from normality, with positive skewness and several relatively large residuals. This was consistent with the presence of influential observations identified using Cook's distance.

Because the primary objective is inference about the regression coefficients rather than prediction, the analysis focuses particularly on the robustness of the coefficient estimates and their statistical significance.

---

## 12. Sensitivity Analysis

A sensitivity analysis was conducted by excluding the eight observations that exceeded the Cook's distance threshold of **0.0234**.

This reduced the sample from:

**171 → 163 countries**

The sensitivity model was again estimated using HC3 robust standard errors.

### Sensitivity model results

| Variable | Coefficient | p-value | 95% CI |
|---|---:|---:|---:|
| GDP % change | −0.0380 | 0.089 | −0.082 to +0.006 |
| Health expenditure % change | +0.0028 | 0.647 | −0.009 to +0.015 |
| Urbanization change | +0.6605 | <0.001 | +0.378 to +0.943 |

The sensitivity model had:

- **163 observations**
- **R² = 0.118**
- **Adjusted R² = 0.102**

---

## 12.1 GDP Sensitivity

The GDP coefficient changed from:

**−0.0645 → −0.0380**

The coefficient remained negative, but the p-value changed from:

**0.024 → 0.089**

The confidence interval changed from:

**−0.120 to −0.009**

to:

**−0.082 to +0.006**

The confidence interval now includes zero.

Therefore, the GDP association was **not robust to the exclusion of influential observations**.

The primary model provides evidence of a negative association, but the sensitivity analysis indicates that this evidence depends to some degree on influential countries.

---

## 12.2 Health Expenditure Sensitivity

The health expenditure coefficient changed from:

**+0.0094 → +0.0028**

The p-value changed from:

**0.313 → 0.647**

Both models therefore provide no statistically significant evidence of an association.

The confidence interval in the sensitivity model was:

**−0.009 to +0.015**

which includes zero.

The conclusion for health expenditure is therefore stable.

---

## 12.3 Urbanization Sensitivity

The urbanization coefficient changed from:

**+0.7160 → +0.6605**

The relationship remained highly statistically significant:

**p < 0.001**

The sensitivity-model confidence interval was:

**+0.378 to +0.943**

which remains entirely above zero.

The relatively small change in the coefficient and continued statistical significance indicate that the urbanization finding is **robust to influential observations**.

---

## 13. Final Model Comparison

The primary and sensitivity models were compared to assess the stability of the results.

| Variable | Primary β | Primary p | Sensitivity β | Sensitivity p |
|---|---:|---:|---:|---:|
| GDP % change | −0.0645 | 0.0235 | −0.0380 | 0.0895 |
| Health expenditure % change | +0.0094 | 0.3127 | +0.0028 | 0.6465 |
| Urbanization change | +0.7160 | 0.0002 | +0.6605 | 0.000005 |

### Model-level comparison

| Statistic | Primary model | Sensitivity model |
|---|---:|---:|
| Observations | 171 | 163 |
| R² | 0.115 | 0.118 |
| Adjusted R² | 0.099 | 0.102 |

The R² increased slightly after removing influential observations, from **0.115 to 0.118**. Therefore, removing the influential observations did not reduce the overall explanatory power of the model.

More importantly, the urbanization coefficient remained very similar and statistically significant, while the GDP coefficient became statistically non-significant.

---

## 14. Hypothesis Testing Conclusions

## H1 — GDP per capita

**H₀:** Change in GDP per capita is not significantly associated with change in NCD mortality.

**H₁:** Change in GDP per capita is significantly associated with change in NCD mortality.

### Result

The primary HC3 model found a statistically significant negative association:

**β = −0.0645, p = 0.024**

However, after excluding influential observations:

**β = −0.0380, p = 0.089**

The association was therefore no longer statistically significant.

### Conclusion

**H1 is not considered robustly supported.**

The primary model suggests that greater GDP growth was associated with greater decreases in NCD mortality, but this relationship was sensitive to influential observations.

The result should therefore be reported as a negative association observed in the primary model rather than as a robust finding.

---

## H2 — Health expenditure per capita

**H₀:** Change in health expenditure per capita is not significantly associated with change in NCD mortality.

**H₁:** Change in health expenditure per capita is significantly associated with change in NCD mortality.

### Result

The primary model found:

**β = +0.0094, p = 0.313**

The sensitivity model found:

**β = +0.0028, p = 0.647**

Neither model produced a statistically significant result.

### Conclusion

**H2 is not supported.**

The analysis provides no statistically significant evidence that changes in health expenditure per capita were associated with changes in NCD mortality between 2000 and 2021.

---

## H3 — Urbanization

**H₀:** Change in urban population is not significantly associated with change in NCD mortality.

**H₁:** Change in urban population is significantly associated with change in NCD mortality.

### Result

The primary model found:

**β = +0.7160, p < 0.001**

The sensitivity model found:

**β = +0.6605, p < 0.001**

The confidence intervals in both models excluded zero.

### Conclusion

**H3 is supported.**

The analysis provides statistically significant evidence of a positive association between increases in urbanization and changes in NCD mortality.

This result was also robust to the exclusion of influential observations.

---

## 15. Overall Conclusion

The overall research hypothesis proposed that economic development, healthcare expenditure, and urbanization would be significantly associated with changes in NCD mortality across countries between 2000 and 2021.

The results provide **partial support** for this hypothesis.

Urbanization was the strongest and most robust finding. Countries with larger increases in their urban population share tended to experience less favorable changes in NCD mortality. This association remained statistically significant after controlling for GDP and health expenditure and remained highly significant after influential observations were excluded.

GDP growth showed a statistically significant negative association with NCD mortality change in the primary model. However, this association was no longer statistically significant after influential observations were excluded. The GDP finding should therefore be considered **sensitive rather than robust**.

Changes in health expenditure per capita were not significantly associated with changes in NCD mortality in either the primary or sensitivity model.

Overall:

| Hypothesis | Result |
|---|---|
| **H1 — GDP** | Not robustly supported |
| **H2 — Health expenditure** | Not supported |
| **H3 — Urbanization** | Supported and robust |

The model explained approximately **11.5% of the variation** in cross-country changes in NCD mortality in the primary analysis.

These findings should be interpreted as **associations rather than causal effects**. The analysis compares changes between two points in time and does not establish that changes in GDP, health expenditure, or urbanization caused changes in NCD mortality. Other country-level factors that are not included in the model may also contribute to the observed differences.

The country-change analysis therefore provides evidence about which factors are statistically associated with differences in NCD mortality trajectories across countries, while the descriptive country-year analysis and Tableau visualizations provide additional information about how NCD mortality evolved over time and how patterns varied geographically and regionally.