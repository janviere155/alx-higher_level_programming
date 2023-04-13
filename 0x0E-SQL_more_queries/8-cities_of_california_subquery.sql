-- 8-cities_of_california_subquery.sql
-- Subquerying in two tables
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name='California'
)
ORDER BY id ASC;
