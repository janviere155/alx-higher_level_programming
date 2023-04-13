-- 16-no_link.sql
-- Script to list all records
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
