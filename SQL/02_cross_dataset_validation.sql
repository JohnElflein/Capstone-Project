-- ============================================================
-- NCD Mortality Capstone — Cross-Dataset Validation
-- ============================================================


-- ============================================================
-- 1. Country Coverage by Dataset
-- ============================================================

SELECT
    'NCD mortality' AS dataset,
    COUNT(DISTINCT "SpatialDimValueCode") AS countries
FROM s_johnelflein.who_ncd_mortality

UNION ALL

SELECT
    'GDP per capita',
    COUNT(DISTINCT code)
FROM s_johnelflein.worldbank_gdp_per_capita

UNION ALL

SELECT
    'Health expenditure',
    COUNT(DISTINCT code)
FROM s_johnelflein.who_health_expenditure

UNION ALL

SELECT
    'Urban population',
    COUNT(DISTINCT code)
FROM s_johnelflein.un_urban_population;


-- ============================================================
-- 2. Countries Present in All Four Datasets
-- ============================================================

SELECT
    COUNT(*) AS countries_in_all_four
FROM (
    SELECT DISTINCT "SpatialDimValueCode"
    FROM s_johnelflein.who_ncd_mortality

    INTERSECT

    SELECT DISTINCT code
    FROM s_johnelflein.worldbank_gdp_per_capita

    INTERSECT

    SELECT DISTINCT code
    FROM s_johnelflein.who_health_expenditure

    INTERSECT

    SELECT DISTINCT code
    FROM s_johnelflein.un_urban_population
) AS common_countries;


-- ============================================================
-- 3. List of Countries Present in All Four Datasets
-- ============================================================

SELECT
    "SpatialDimValueCode"
FROM (
    SELECT DISTINCT "SpatialDimValueCode"
    FROM s_johnelflein.who_ncd_mortality

    INTERSECT

    SELECT DISTINCT code
    FROM s_johnelflein.worldbank_gdp_per_capita

    INTERSECT

    SELECT DISTINCT code
    FROM s_johnelflein.who_health_expenditure

    INTERSECT

    SELECT DISTINCT code
    FROM s_johnelflein.un_urban_population
) AS common_countries
ORDER BY "SpatialDimValueCode";


-- ============================================================
-- 4. NCD Mortality Availability at Study Endpoints
-- ============================================================

SELECT
    "Period",
    COUNT(*) AS total_rows,
    COUNT("FactValueNumeric") AS available_values,
    COUNT(*) - COUNT("FactValueNumeric") AS missing_values
FROM s_johnelflein.who_ncd_mortality
WHERE "Period" IN (2000, 2021)
GROUP BY "Period"
ORDER BY "Period";


-- ============================================================
-- 5. GDP Availability at Study Endpoints
-- ============================================================

SELECT
    year,
    COUNT(*) AS total_rows,
    COUNT(gdp_per_capita) AS available_values,
    COUNT(*) - COUNT(gdp_per_capita) AS missing_values
FROM s_johnelflein.worldbank_gdp_per_capita
WHERE year IN (2000, 2021)
GROUP BY year
ORDER BY year;


-- ============================================================
-- 6. Health Expenditure Availability at Study Endpoints
-- ============================================================

SELECT
    year,
    COUNT(*) AS total_rows,
    COUNT(che_ppp_pc) AS available_values,
    COUNT(*) - COUNT(che_ppp_pc) AS missing_values
FROM s_johnelflein.who_health_expenditure
WHERE year IN (2000, 2021)
GROUP BY year
ORDER BY year;


-- ============================================================
-- 7. Urban Population Availability at Study Endpoints
-- ============================================================

SELECT
    year,
    COUNT(*) AS total_rows,
    COUNT(urban_population_pct) AS available_values,
    COUNT(*) - COUNT(urban_population_pct) AS missing_values
FROM s_johnelflein.un_urban_population
WHERE year IN (2000, 2021)
GROUP BY year
ORDER BY year;


-- ============================================================
-- 8. Countries with Complete Data for Both 2000 and 2021
-- ============================================================

WITH complete_countries AS (
    SELECT
        n."SpatialDimValueCode"
    FROM s_johnelflein.who_ncd_mortality n

    JOIN s_johnelflein.worldbank_gdp_per_capita g
        ON n."SpatialDimValueCode" = g.code

    JOIN s_johnelflein.who_health_expenditure h
        ON n."SpatialDimValueCode" = h.code

    JOIN s_johnelflein.un_urban_population u
        ON n."SpatialDimValueCode" = u.code

    WHERE n."Period" IN (2000, 2021)
      AND g.year IN (2000, 2021)
      AND h.year IN (2000, 2021)
      AND u.year IN (2000, 2021)
      AND n."FactValueNumeric" IS NOT NULL
      AND g.gdp_per_capita IS NOT NULL
      AND h.che_ppp_pc IS NOT NULL
      AND u.urban_population_pct IS NOT NULL

    GROUP BY n."SpatialDimValueCode"

    HAVING COUNT(DISTINCT n."Period") = 2
       AND COUNT(DISTINCT g.year) = 2
       AND COUNT(DISTINCT h.year) = 2
       AND COUNT(DISTINCT u.year) = 2
)

SELECT
    COUNT(*) AS complete_countries
FROM complete_countries;


-- ============================================================
-- 9. Duplicate NCD Country-Year Observations
-- ============================================================

SELECT
    "SpatialDimValueCode" AS code,
    "Period" AS year,
    COUNT(*) AS observations
FROM s_johnelflein.who_ncd_mortality
WHERE "Period" IN (2000, 2021)
GROUP BY "SpatialDimValueCode", "Period"
HAVING COUNT(*) > 1;


-- ============================================================
-- 10. Duplicate GDP Country-Year Observations
-- ============================================================

SELECT
    code,
    year,
    COUNT(*) AS observations
FROM s_johnelflein.worldbank_gdp_per_capita
WHERE year IN (2000, 2021)
GROUP BY code, year
HAVING COUNT(*) > 1;


-- ============================================================
-- 11. Duplicate Health Expenditure Country-Year Observations
-- ============================================================

SELECT
    code,
    year,
    COUNT(*) AS observations
FROM s_johnelflein.who_health_expenditure
WHERE year IN (2000, 2021)
GROUP BY code, year
HAVING COUNT(*) > 1;


-- ============================================================
-- 12. Duplicate Urban Population Country-Year Observations
-- ============================================================

SELECT
    code,
    year,
    COUNT(*) AS observations
FROM s_johnelflein.un_urban_population
WHERE year IN (2000, 2021)
GROUP BY code, year
HAVING COUNT(*) > 1;


-- ============================================================
-- 13. Sample NCD Mortality Observations
-- ============================================================

SELECT
    "Location",
    "SpatialDimValueCode",
    "Period",
    "FactValueNumeric"
FROM s_johnelflein.who_ncd_mortality
WHERE "Period" IN (2000, 2021)
LIMIT 10;


-- ============================================================
-- 14. NCD Dimension Values
-- ============================================================

SELECT DISTINCT
    "Dim1",
    "Dim1 type"
FROM s_johnelflein.who_ncd_mortality
LIMIT 20;


-- ============================================================
-- 15. NCD Observations by Dimension
-- ============================================================

SELECT
    "Dim1",
    COUNT(*) AS observations
FROM s_johnelflein.who_ncd_mortality
GROUP BY "Dim1"
ORDER BY observations DESC;


-- ============================================================
-- 16. NCD Observations by Dimension Type
-- ============================================================

SELECT
    "Dim1 type",
    COUNT(*) AS observations
FROM s_johnelflein.who_ncd_mortality
GROUP BY "Dim1 type"
ORDER BY observations DESC;
