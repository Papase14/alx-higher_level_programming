-- SCRIPT THAT CREATES A TABLE IN THE CURRENT DATABASE
-- cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

CREATE TABLE IF NOT EXIST first_table (
    id INT,
    name VARCHAR(256)
);
