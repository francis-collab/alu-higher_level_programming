
-- Task: List all records with a score >= 10 in the table second_table
-- This script will select and display records where score >= 10, ordered by score in descending order

SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;

