-- lists all records in a table
-- results display score and the name
-- ordered in descending order
-- cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
