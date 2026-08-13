-- PUNTO 1
-- Creamos la tabla peliculas
/*
create table peliculas (
	id SERIAL,
	nombre varchar(255),
	anno integer,
	PRIMARY KEY (id)
);
*/

-- Creamos tags
/*
create table tags (
	id SERIAL,
	tag varchar(32),
	PRIMARY KEY (id)
);
*/


-- peliculas_tags
/*
create table peliculas_tags (
	id SERIAL,
	pelicula_id integer references peliculas (id),
	tags_id integer references tags (id),
	PRIMARY KEY (id)
);
*/

-- PUNTO 2
-- Insertar 5 peliculas
/*
INSERT INTO peliculas (nombre, anno) VALUES
	('Parque Jurásico', 1993),
	('Titanic', 1997),
	('Salvar al soldado Ryan', 1998),
	('El sexto sentido', 1999),
	('Matrix', 1999);
*/

-- Insertar 5 tags
/*
INSERT INTO tags (tag) VALUES 
	('Aventura'),
	('Drama'),
	('Fantasia'),
	('Acción'),
	('Romance');
*/

-- peliculas y tags
/*
INSERT INTO peliculas_tags (pelicula_id, tags_id) VALUES
	(1, 1),
	(1, 2),
	(1, 4),
	(2, 2),
	(2, 5);
*/

-- PUNTO 3
-- Cuenta la cantidad de tags que tiene cada película.
-- Si una película no tiene tags debe mostrar 0.

-- v1 - No muestra las peliculas sin tags
/*
SELECT pg.pelicula_id, COUNT(*) numero_tags
FROM peliculas_tags pg
GROUP BY pg.pelicula_id
*/

/*
SELECT p.id, COUNT(pg.*) numero_tags
FROM peliculas_tags pg
	RIGHT JOIN peliculas p ON p.id = pg.pelicula_id
GROUP BY p.id
*/

/*
SELECT p.id, COUNT(pg.*) numero_tags
FROM peliculas p
	LEFT JOIN peliculas_tags pg ON p.id = pg.pelicula_id
GROUP BY p.id
*/

-- utilizando subconsultas
/*
SELECT p.id, p.nombre, anno año, 
	(
		select count(*)
		from peliculas_tags
		where pelicula_id = p.id
	)  numero_tags
FROM peliculas p
*/
