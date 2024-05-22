CREATE DATABASE manageo;
USE manageo;

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO user (first_name, last_name, email, password) VALUES
('Vanny','Lamorte', 'a', "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"),
('Eric','Salcioli','eric.s@gmail.com', 'a2adfd31a6a0d6fbeef868f9431ace5a519892092d97a793985446a69d773d9f');
-- Eric's Password: eric.s

