-- creates the table unique_id
-- id INT with the default value of 1 and must be UNIQUE
-- name VARCHAR(256)
-- if table unique_id already exists, script should not fail
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
