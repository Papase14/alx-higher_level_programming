--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
