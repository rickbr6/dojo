Use world;
SELECT * FROM languages;
SELECT * FROM countries;
SELECT * FROM cities;

-- 1)
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages on countries.id = languages.country_id
WHERE language = "Slovene"
ORDER by percentage desc;

-- 2)
SELECT countries.name, COUNT(cities.name) AS num_of_cities FROM countries
JOIN cities on countries.id = country_id
GROUP by countries.name
ORDER by num_of_cities desc;

-- 3)
SELECT cities.name, cities.population FROM countries
JOIN cities on countries.id = country_id
WHERE countries.name = "Mexico" and cities.population > 500000;

-- 4)
SELECT * FROM countrylanguage;

SELECT countries.name, countrylanguage.Language AS language_gt_89P, countrylanguage.Percentage FROM countries
JOIN countrylanguage on countries.code = countrylanguage.CountryCode
WHERE countrylanguage.Percentage > 89
ORDER by countrylanguage.Percentage desc;

-- 5)
SELECT name, surface_area, population FROM countries
WHERE surface_area < 501 AND population > 100000;

-- 6)
SELECT name, capital, life_expectancy FROM countries
WHERE government_form = "Constitutional Monarchy" AND capital > 200;

-- 7)
SELECT countries.name, cities.name, cities.district, cities.population FROM countries
JOIN cities on countries.id = cities.country_id
WHERE cities.district = "Buenos Aires" AND cities.population > 500000;

-- 8)
SELECT Region, COUNT(Code) AS country_count FROM country
GROUP by Region
ORDER by country_count desc














