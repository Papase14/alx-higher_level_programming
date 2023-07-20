-- lists all cities contained in the database 
-- Results must be sorted in ascending order by cities.id
-- cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id
