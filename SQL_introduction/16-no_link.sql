-- Task: List all records of the table second_table from the database hbtn_0c_0
-- This script will select records with a non-null name value, displaying the score and name, ordered by score in descending order

SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;
