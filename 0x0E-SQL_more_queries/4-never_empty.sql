-- creates the table id_not_null
-- id INT with the defaukt value of 1
-- name VARCHAR(256)
-- if the table id_not_null already exists, script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
