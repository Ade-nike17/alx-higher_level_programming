-- creates the database hbtn_0d_usa
-- if database exists, script should fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates a table 'states' in the database created
-- if table exists, script should not fail
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
