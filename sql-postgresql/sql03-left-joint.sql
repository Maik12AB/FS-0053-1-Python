-- Uniendo dos o más tablas

/*
Select *
FROM Artist
*/

-- Artist con Album
-- Cuando trabajamos con JOIN una buena práctica es:
-- 1. Indicar el nombre de la columna que desamos
-- 2. Indicar la tabla a la que pretenece la columna
/*
SELECT Artist.artist_id, Artist.name artist_name
FROM Artist
	LEFT JOIN Album ON Album.artist_id = Artist.artist_id
*/

-- 3. Utilizar alias en las tablas
/*
SELECT a.artist_id, al.album_id, al.artist_id artist_id_album,
	a.name artist_name, al.title
FROM Artist a
	LEFT JOIN Album al ON al.artist_id = a.artist_id
*/

-- Agregar el nombre de las canciones
/*
SELECT a.artist_id, a.name artist_name, al.title album_name, t.name track_name
FROM Artist a
	LEFT JOIN Album al ON al.artist_id = a.artist_id
	LEFT JOIN Track t ON t.album_id = al.album_id
*/


-- No listar artistas que no tienen album
/*
SELECT a.artist_id, a.name artist_name, al.title album_name, t.name track_name
FROM Artist a
	LEFT JOIN Album al ON al.artist_id = a.artist_id
	LEFT JOIN Track t ON t.album_id = al.album_id
WHERE al.title IS NOT null
*/

-- Ordenar la consulta (Result set)
/*
SELECT a.artist_id, a.name artist_name, al.title album_name, t.name track_name
FROM Artist a
	LEFT JOIN Album al ON al.artist_id = a.artist_id
	LEFT JOIN Track t ON t.album_id = al.album_id
WHERE al.title IS NOT null
ORDER BY artist_name, album_name
*/

-- Que artista no tiene album
/*
SELECT a.artist_id, a.name artist_name, al.title album_name
FROM Artist a
	LEFT JOIN Album al ON al.artist_id = a.artist_id
WHERE al.title IS null
*/

-- Cuantas canciones tenemos por album
SELECT a.artist_id, a.name artist_name, al.title album_name, COUNT(t.name) track_count
FROM Artist a
	LEFT JOIN Album al ON al.artist_id = a.artist_id
	LEFT JOIN Track t ON t.album_id = al.album_id
WHERE al.title IS NOT null
GROUP BY a.artist_id, a.name, al.title
ORDER BY artist_name, album_name
