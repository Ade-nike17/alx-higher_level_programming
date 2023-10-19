-- creates the table force_name
-- if the table force_name already exists, script should not fail
-- id INT
-- name VARCHAR(256) cant't be null
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
