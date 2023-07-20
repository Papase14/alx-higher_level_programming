-- displays the top 3 of cities temperatures
-- during July and August
-- ordered by temperature
-- cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY  avg_temp DESC
LIMIT 3;
