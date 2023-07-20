-- lists all the cities of california in the database
-- results stored in ascending order by cities.id
-- cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa

SELECT id, name FROM cities 
WHERE state_id = 
(
    SELECT id FROM states 
    WHERE name = "California"
) ORDER BY id;
