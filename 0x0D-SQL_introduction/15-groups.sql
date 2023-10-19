-- lists the number of records with the same score in the table
-- The database name will be passed as an argument to the mysql command
SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
