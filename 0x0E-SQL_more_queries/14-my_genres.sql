-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- Results must be sorted in ascending order by the genre name
-- cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name;
