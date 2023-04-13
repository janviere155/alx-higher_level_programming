-- 11-best_score.sql
-- list all records where `score>=10` in order of top score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
