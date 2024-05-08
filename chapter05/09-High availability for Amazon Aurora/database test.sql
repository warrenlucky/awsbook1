CREATE DATABASE test;
use test;
CREATE TABLE user (
id INT AUTO_INCREMENT,
        name VARCHAR(25),
        age INT,
        PRIMARY KEY (id));
INSERT INTO user(name, age) VALUES ('zhangsan', 18);
INSERT INTO user(name, age) VALUES ('lisi', 19);
INSERT INTO user(name, age) VALUES ('wangwu', 20);