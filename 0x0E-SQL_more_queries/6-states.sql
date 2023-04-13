-- 6-states.sql
-- Auto-generated id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	UNIQUE (id),
	PRIMARY KEY (id)
);
