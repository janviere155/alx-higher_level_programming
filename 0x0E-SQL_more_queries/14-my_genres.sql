-- List tv shows and their genres
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT name
FROM tv_genres
JOIN tv_show_genres ON id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title='Dexter'
ORDER BY name;
