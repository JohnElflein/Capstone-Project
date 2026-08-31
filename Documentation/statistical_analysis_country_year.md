## Exploratory Data Analysis (EDA) - ncd_analytical_country_year dataset

### 1. Dataset Overview

The analytical dataset contains 3,949 country-year observations covering 2000–2021.

The variables used in the analysis are:

- `ncd_mortality_rate` — NCD mortality rate
- `gdp_per_capita` — GDP per capita, PPP (constant 2021 international $)
- `health_expenditure_per_capita` — Current Health Expenditure per capita in current international $ (PPP)
- `urban_population_pct` — Urban population as a percentage of total population

There are 88 missing GDP observations and one missing health expenditure observation. NCD mortality and urban population have no missing values.

For analyses requiring all four variables, 3,861 complete observations are available.

### 2. Univariate Analysis

The distributions of the variables were examined using descriptive statistics and histograms.

NCD mortality had a moderate right skew (skewness = 0.54).

GDP per capita was strongly right-skewed (skewness = 1.93), while health expenditure per capita was even more strongly right-skewed (skewness = 3.26). Urban population was approximately symmetric (skewness = −0.06).

Because GDP per capita and health expenditure per capita were strongly right-skewed, natural-log transformations were applied to these variables.

After transformation:

- `log_gdp_per_capita`: skewness = −0.14
- `log_health_expenditure`: skewness = −0.04

The transformed variables therefore have substantially more symmetric distributions and will be used where appropriate in subsequent statistical analysis.

### 3. Bivariate Analysis

Scatterplots and correlation coefficients were used to examine the relationships between NCD mortality and the explanatory variables.

Pearson correlations were:

| Relationship | Pearson r |
|---|---:|
| NCD mortality vs. log GDP per capita | −0.568 |
| NCD mortality vs. log health expenditure | −0.585 |
| NCD mortality vs. urban population | −0.522 |

Spearman correlations were:

| Relationship | Spearman ρ |
|---|---:|
| NCD mortality vs. log GDP per capita | −0.615 |
| NCD mortality vs. log health expenditure | −0.637 |
| NCD mortality vs. urban population | −0.564 |

All three explanatory variables therefore show moderate negative associations with NCD mortality in the observed country-year data.

The Spearman correlations are somewhat stronger than the Pearson correlations, suggesting that the relationships are consistently monotonic but may not be perfectly linear.

These findings are descriptive and do not establish causality.

### Next Steps

The next stage of the analysis will examine the relationships among GDP per capita, health expenditure per capita, and urbanization. This will help assess potential multicollinearity before developing multivariable statistical models.

The analysis will then proceed to inferential statistical testing of the relationship between GDP per capita and NCD mortality, while accounting for health expenditure and urbanization.

### 4. Simple Linear Regression

Three simple linear regression models were estimated to examine the association between NCD mortality and each explanatory variable individually.

#### NCD mortality and GDP per capita

Log GDP per capita was significantly negatively associated with NCD mortality (β = −89.12, p < 0.001). The model had an R² of 0.323, indicating that log GDP per capita explained approximately 32.3% of the variation in NCD mortality.

#### NCD mortality and health expenditure

Log health expenditure per capita was significantly negatively associated with NCD mortality (β = −77.54, p < 0.001). The model had an R² of 0.348, explaining approximately 34.8% of the variation in NCD mortality.

#### NCD mortality and urbanization

Urban population percentage was significantly negatively associated with NCD mortality (β = −4.26, p < 0.001). The model had an R² of 0.277, indicating that urbanization explained approximately 27.7% of the variation in NCD mortality.

Overall, all three explanatory variables showed statistically significant negative associations with NCD mortality when examined individually. These results are consistent with the correlations observed during bivariate EDA.

However, these models do not account for the strong correlations among the explanatory variables or the repeated observations of countries over time. Therefore, the results should be interpreted as simple associations rather than causal effects. Further analysis will assess multicollinearity and the panel structure of the data before estimating the final model.

### 5. Multiple Linear Regression

A multiple linear regression model was estimated to examine the association between NCD mortality and all three explanatory variables simultaneously:

- log GDP per capita
- log health expenditure per capita
- urban population percentage

The model used 3,861 complete observations from the 2000–2021 dataset.

#### Initial multiple regression model

The initial OLS model explained approximately 35.9% of the variation in NCD mortality (R² = 0.359; adjusted R² = 0.358).

When controlling for the other explanatory variables:

- **Log GDP per capita** had a coefficient of −7.82 (p = 0.210), indicating that its association with NCD mortality was not statistically significant after accounting for health expenditure and urbanization.
- **Log health expenditure per capita** had a coefficient of −53.03 (p < 0.001), indicating a statistically significant negative association with NCD mortality.
- **Urban population percentage** had a coefficient of −1.48 (p < 0.001), also indicating a statistically significant negative association with NCD mortality.

These results differ from the simple regression models. In the individual models, all three explanatory variables had relatively strong negative associations with NCD mortality. However, after including all three variables simultaneously, the coefficient for GDP per capita became much smaller and was no longer statistically significant.

This suggests that the apparent relationship between economic development and NCD mortality observed in the simple regression may partly reflect its strong relationship with health expenditure and urbanization.

#### Robust standard errors

The model was subsequently re-estimated using HC3 heteroscedasticity-robust standard errors after the Breusch–Pagan test indicated statistically significant heteroscedasticity.

The coefficients and R² remained unchanged because robust standard errors do not change the estimated regression coefficients. They instead provide more reliable standard errors, confidence intervals, and p-values when the variance of the residuals is not constant.

Using HC3 robust standard errors:

- **Log GDP per capita:** β = −7.82, p = 0.342, 95% CI −23.94 to 8.31
- **Log health expenditure per capita:** β = −53.03, p < 0.001, 95% CI −66.44 to −39.63
- **Urban population percentage:** β = −1.48, p < 0.001, 95% CI −1.80 to −1.17

The substantive conclusions therefore remain similar: health expenditure and urbanization show statistically significant negative associations with NCD mortality, while GDP per capita does not show a statistically significant independent association once the other variables are controlled for.

However, the explanatory variables are strongly correlated with one another, particularly GDP per capita and health expenditure. Therefore, the coefficients should not yet be interpreted as independent causal effects. Multicollinearity and the panel structure of the data require further investigation before the final statistical model is selected.

## 6. Conclusion

The country-year dataset provided a useful foundation for understanding patterns in NCD mortality and its relationship with economic development, health expenditure, and urbanization between 2000 and 2021.

The exploratory analysis showed that NCD mortality had a mean of approximately 586 deaths per 100,000 population, while GDP per capita and health expenditure were strongly right-skewed. Log transformations substantially reduced the skewness of both GDP per capita and health expenditure, making them more appropriate for regression analysis.

Bivariate analysis showed moderate to strong negative associations between NCD mortality and all three explanatory variables. Spearman correlations were -0.615 for log GDP per capita, -0.637 for log health expenditure, and -0.564 for urban population percentage. Simple linear regression models produced similar results, with all three variables showing statistically significant negative associations with NCD mortality when considered individually.

The multiple linear regression model explained approximately 35.9% of the variation in NCD mortality. However, the results changed considerably after controlling for the other explanatory variables. Log health expenditure remained significantly negatively associated with NCD mortality (β = -53.03, p < 0.001), as did urban population percentage (β = -1.48, p < 0.001). Log GDP per capita was no longer statistically significant (β = -7.82, p = 0.342). This difference between the simple and multiple regression models demonstrates the importance of considering relationships among explanatory variables.

The diagnostic analysis identified two important limitations. First, GDP per capita and health expenditure were highly correlated (Pearson r = 0.941), resulting in elevated VIF values of 9.52 and 8.86 respectively. This indicates substantial multicollinearity and makes it difficult to separate the individual effects of these variables in the multiple regression model. Second, the Breusch–Pagan test indicated statistically significant heteroscedasticity (p < 0.001). HC3 robust standard errors were therefore used for the multiple regression model. The robust results did not change the substantive conclusions: health expenditure and urbanization remained statistically significant, while GDP per capita remained non-significant.

Finally, examination of the panel structure showed that the dataset contained repeated observations for the same countries over time. There were 183 countries represented, with 175 having complete observations for all years from 2000 to 2021. Eight countries had incomplete time series, but there were no duplicate country-year observations. Because observations from the same country across different years are not necessarily independent, standard OLS regression on the pooled country-year observations should not be interpreted as a definitive hypothesis test without accounting for the panel structure.

### Overall assessment

The country-year analysis therefore provides valuable exploratory evidence that higher economic development, greater health expenditure, and higher urbanization are associated with lower NCD mortality. However, the strong correlation among the explanatory variables, heteroscedasticity, and repeated observations of countries over time limit the interpretation of these regression results as independent effects or causal relationships.

For the primary hypothesis testing, the analysis will therefore shift to the `ncd_analytical_country_change.csv` dataset. This dataset contains one observation per country and measures the change between 2000 and 2021. Using changes over the study period will allow the analysis to directly address whether countries experiencing greater changes in economic development, health expenditure, and urbanization also experienced greater changes in NCD mortality, while avoiding the repeated-observation issue present in the country-year dataset.

The country-year analysis should consequently be viewed as an exploratory and diagnostic stage of the project rather than the final hypothesis test.