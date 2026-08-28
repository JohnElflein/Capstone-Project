CREATE TABLE s_johnelflein.ncd_analytical_country_year AS
SELECT
    n."Location" AS country,
    n."SpatialDimValueCode" AS code,
    n."Period" AS year,
    n."FactValueNumeric" AS ncd_mortality_rate,
    g.gdp_per_capita,
    h.che_ppp_pc AS health_expenditure_per_capita,
    u.urban_population_pct
FROM s_johnelflein.who_ncd_mortality n
INNER JOIN s_johnelflein.worldbank_gdp_per_capita g
    ON n."SpatialDimValueCode" = g.code
    AND n."Period" = g.year
INNER JOIN s_johnelflein.who_health_expenditure h
    ON n."SpatialDimValueCode" = h.code
    AND n."Period" = h.year
INNER JOIN s_johnelflein.un_urban_population u
    ON n."SpatialDimValueCode" = u.code
    AND n."Period" = u.year
WHERE n."Period" BETWEEN 2000 AND 2021;

SELECT COUNT(*) AS total_rows
FROM s_johnelflein.ncd_analytical_country_year;

SELECT
    MIN(year) AS min_year,
    MAX(year) AS max_year
FROM s_johnelflein.ncd_analytical_country_year;

SELECT COUNT(DISTINCT code) AS countries
FROM s_johnelflein.ncd_analytical_country_year;

SELECT *
FROM s_johnelflein.ncd_analytical_country_year
ORDER BY country, year
LIMIT 20;

SELECT
    code,
    year,
    COUNT(*) AS observations
FROM s_johnelflein.ncd_analytical_country_year
GROUP BY code, year
HAVING COUNT(*) > 1;



WITH complete_countries AS (
    SELECT
        n."SpatialDimValueCode" AS code
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
    code
FROM complete_countries
ORDER BY code;


CREATE TABLE s_johnelflein.ncd_analytical_country_change AS
WITH complete_countries AS (
    SELECT
        n."SpatialDimValueCode" AS code
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
),
data_2000 AS (
    SELECT
        n."Location" AS country,
        n."SpatialDimValueCode" AS code,
        n."FactValueNumeric" AS ncd_mortality_2000,
        g.gdp_per_capita AS gdp_2000,
        h.che_ppp_pc AS health_expenditure_2000,
        u.urban_population_pct AS urban_population_2000
    FROM s_johnelflein.who_ncd_mortality n
    JOIN complete_countries c
        ON n."SpatialDimValueCode" = c.code
    JOIN s_johnelflein.worldbank_gdp_per_capita g
        ON n."SpatialDimValueCode" = g.code
        AND g.year = 2000
    JOIN s_johnelflein.who_health_expenditure h
        ON n."SpatialDimValueCode" = h.code
        AND h.year = 2000
    JOIN s_johnelflein.un_urban_population u
        ON n."SpatialDimValueCode" = u.code
        AND u.year = 2000
    WHERE n."Period" = 2000
),
data_2021 AS (
    SELECT
        n."SpatialDimValueCode" AS code,
        n."FactValueNumeric" AS ncd_mortality_2021,
        g.gdp_per_capita AS gdp_2021,
        h.che_ppp_pc AS health_expenditure_2021,
        u.urban_population_pct AS urban_population_2021
    FROM s_johnelflein.who_ncd_mortality n
    JOIN complete_countries c
        ON n."SpatialDimValueCode" = c.code
    JOIN s_johnelflein.worldbank_gdp_per_capita g
        ON n."SpatialDimValueCode" = g.code
        AND g.year = 2021
    JOIN s_johnelflein.who_health_expenditure h
        ON n."SpatialDimValueCode" = h.code
        AND h.year = 2021
    JOIN s_johnelflein.un_urban_population u
        ON n."SpatialDimValueCode" = u.code
        AND u.year = 2021
    WHERE n."Period" = 2021
)
SELECT
    d00.country,
    d00.code,
    d00.ncd_mortality_2000,
    d21.ncd_mortality_2021,
    ((d21.ncd_mortality_2021 - d00.ncd_mortality_2000)
        / d00.ncd_mortality_2000) * 100
        AS ncd_mortality_pct_change,
    d00.gdp_2000,
    d21.gdp_2021,
    ((d21.gdp_2021 - d00.gdp_2000)
        / d00.gdp_2000) * 100
        AS gdp_pct_change,
    d00.health_expenditure_2000,
    d21.health_expenditure_2021,
    ((d21.health_expenditure_2021 - d00.health_expenditure_2000)
        / d00.health_expenditure_2000) * 100
        AS health_expenditure_pct_change,
    d00.urban_population_2000,
    d21.urban_population_2021,
    d21.urban_population_2021 - d00.urban_population_2000
        AS urban_population_pct_point_change
FROM data_2000 d00
JOIN data_2021 d21
    ON d00.code = d21.code;

SELECT COUNT(*) AS total_countries
FROM s_johnelflein.ncd_analytical_country_change;

SELECT
    code,
    COUNT(*) AS observations
FROM s_johnelflein.ncd_analytical_country_change
GROUP BY code
HAVING COUNT(*) > 1;


SELECT
    COUNT(*) AS total_rows,
    COUNT(*) FILTER (
        WHERE ncd_mortality_2000 IS NULL
           OR ncd_mortality_2021 IS NULL
           OR gdp_2000 IS NULL
           OR gdp_2021 IS NULL
           OR health_expenditure_2000 IS NULL
           OR health_expenditure_2021 IS NULL
           OR urban_population_2000 IS NULL
           OR urban_population_2021 IS NULL
    ) AS rows_with_missing_values
FROM s_johnelflein.ncd_analytical_country_change;


SELECT *
FROM s_johnelflein.ncd_analytical_country_change
ORDER BY country
LIMIT 20;