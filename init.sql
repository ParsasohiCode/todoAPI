CREATE DATABASE IF NOT EXISTS todolist;
USE todolist;

CREATE TABLE IF NOT EXISTS todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 
INSERT INTO todos (title, completed, created_at) VALUES ('Buy groceries', FALSE, CURRENT_TIMESTAMP);
INSERT INTO todos (title, completed, created_at) VALUES ('Finish project', TRUE, CURRENT_TIMESTAMP);
INSERT INTO todos (title, completed, created_at) VALUES ('Call the bank', FALSE, CURRENT_TIMESTAMP);

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    last_login TIMESTAMP
);

INSERT INTO users (username, password_hash) VALUES ('testuser1', 'dummyhash1');
INSERT INTO users (username, password_hash) VALUES ('testuser2', 'dummyhash2');
