-- lists all cities contained in the database hbtn_0d_usa
-- Each record displays: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- The database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
