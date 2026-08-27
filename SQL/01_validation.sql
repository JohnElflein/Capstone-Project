
--NCD validation
SELECT *
FROM s_johnelflein.who_ncd_mortality
LIMIT 10;

SELECT count(*) AS row_count
FROM s_johnelflein.who_ncd_mortality;

SELECT
    MIN("Period") AS min_year,
    MAX("Period") AS max_year
FROM s_johnelflein.who_ncd_mortality;

SELECT "Dim1"
FROM s_johnelflein.who_ncd_mortality;

SELECT DISTINCT "Indicator"
FROM s_johnelflein.who_ncd_mortality;

SELECT COUNT(DISTINCT "SpatialDimValueCode") AS countries
FROM s_johnelflein.who_ncd_mortality;


--GDP validation
ALTER TABLE s_johnelflein.worldbank_gdp_per_capita_import
RENAME TO worldbank_gdp_per_capita;

SELECT *
FROM worldbank_gdp_per_capita wgpc;

SELECT COUNT(*) AS row_count
FROM s_johnelflein.worldbank_gdp_per_capita;

SELECT
    "Country Name",
    "Country Code",
    "2000",
    "2021"
FROM s_johnelflein.worldbank_gdp_per_capita
LIMIT 10;

SELECT DISTINCT
    "Indicator Name",
    "Indicator Code"
FROM s_johnelflein.worldbank_gdp_per_capita;

SELECT
    COUNT(*) AS total_rows,
    COUNT("2000") AS gdp_2000_available,
    COUNT("2021") AS gdp_2021_available
FROM s_johnelflein.worldbank_gdp_per_capita;


--Health expenditure validation
ALTER TABLE s_johnelflein.who_health_expenditure_import 
RENAME TO who_health_expenditure;

SELECT COUNT(*) AS row_count
FROM s_johnelflein.who_health_expenditure;

SELECT
    MIN(year) AS min_year,
    MAX(year) AS max_year
FROM s_johnelflein.who_health_expenditure;

SELECT COUNT(DISTINCT code) AS country_count
FROM s_johnelflein.who_health_expenditure;

SELECT
    location,
    year,
    che_ppp_pc
FROM s_johnelflein.who_health_expenditure
ORDER BY location, year
LIMIT 10;

SELECT
    COUNT(*) AS total_rows,
    COUNT(che_ppp_pc) AS available_values,
    COUNT(*) - COUNT(che_ppp_pc) AS missing_values
FROM s_johnelflein.who_health_expenditure;

SELECT
    location,
    code,
    year,
    che_ppp_pc
FROM s_johnelflein.who_health_expenditure
WHERE che_ppp_pc IS NULL;


--Urban population validation
SELECT COUNT(*) AS row_count
FROM s_johnelflein.un_urban_population;

SELECT
    MIN(year) AS min_year,
    MAX(year) AS max_year
FROM s_johnelflein.un_urban_population;

SELECT COUNT(DISTINCT code) AS country_count
FROM s_johnelflein.un_urban_population;

SELECT
    COUNT(*) AS total_rows,
    COUNT(urban_population_pct) AS available_values,
    COUNT(*) - COUNT(urban_population_pct) AS missing_values
FROM s_johnelflein.un_urban_population;

SELECT *
FROM s_johnelflein.un_urban_population
ORDER BY location, year
LIMIT 10;

