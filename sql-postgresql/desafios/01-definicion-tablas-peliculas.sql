-- Requerimiento 3
-- Obtener el ID de la película “Titanic”.
/*
SELECT id
FROM peliculas
WHERE titulo = 'Titanic';
*/

-- Requerimiento 4
-- Listar a todos los actores que aparecen en la película "Titanic".
/*
SELECT *
FROM reparto
WHERE id_pelicula = 2;
*/

-- Utilizando join
/*
SELECT r.*
FROM reparto r
	RIGHT JOIN peliculas p ON p.id = r.id_pelicula
WHERE p.titulo = 'Titanic';
*/

-- Subconsultas
/*
SELECT *
FROM reparto
WHERE id_pelicula = (SELECT id FROM peliculas WHERE titulo = 'Titanic')
*/

-- Requerimiento 5
-- Consultar en cuántas películas del top 100 participa Harrison Ford.
/*
SELECT COUNT(*)
FROM reparto
WHERE actor = 'Harrison Ford'
*/

-- Subconsulta
/*
SELECT *
FROM peliculas
WHERE id in (SELECT id_pelicula FROM reparto WHERE actor = 'Harrison Ford')
*/


-- Requerimiento 6
-- Indicar las películas estrenadas entre los años 1990 y 1999
-- ordenadas por título de manera ascendente.
/*
SELECT *
FROM peliculas
WHERE año BETWEEN 1990 and 1999
ORDER BY titulo ASC
*/

-- Requerimiento 7
-- Hacer una consulta SQL que muestre los títulos con su longitud,
-- la longitud debe ser nombrado para la consulta como
-- “longitud_titulo”.
/*
select titulo, length(titulo) longitud_titulo
from peliculas
*/

-- Requerimiento 8
-- Consultar cual es la longitud más grande entre todos los títulos 
-- de las películas.
/*
select max( length(titulo) ) longitud_titulo
from peliculas
*/

-- Nombre de la pelicula con la longitud más grande
/*
select titulo, length(titulo) longitud_titulo
from peliculas
where length(titulo) = (select max( length(titulo) ) from peliculas)
*/
