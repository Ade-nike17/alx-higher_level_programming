-- list all the cuties of California in the database hbtn_0d_usa
-- The states table contains only one record where name = California but the id can be different
-- Results must be sorted in ascending order by cities.id
-- The database name will be passed as an argument of the mysql command
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
);

