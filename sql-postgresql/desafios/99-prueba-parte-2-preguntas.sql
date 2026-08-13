-- Parte 2
-- Preguntas y respuesta

-- preguntas
/*
create table preguntas (
	id SERIAL,
	pregunta varchar(255),
	respuesta_correcta varchar(255),
	primary key (id)
)
*/

/*
create table usuarios (
	id SERIAL,
	nombre varchar(255),
	edad integer,
	primary key (id)
)
*/

/*
create table respuestas (
	id SERIAL,
	respuesta varchar(255),
	usuario_id integer references usuarios (id),
	pregunta_id integer references preguntas (id),
	primary key (id)
)
*/

-- Agregar 5 registros a la tabla usuarios
/*
INSERT INTO usuarios (nombre, edad) VALUES
    ('Ana', 22),
    ('Carlos', 30),
    ('María', 27),
    ('Pedro', 35),
    ('Sofía', 24);
*/

-- Agregar 5 preguntas
/*
INSERT INTO preguntas (pregunta, respuesta_correcta) VALUES
    ('¿Cuál es la capital de Chile?', 'Santiago'),
    ('¿Cuál es la capital de Argentina?', 'Buenos Aires'),
    ('¿Cuál es el océano que se encuentra al oeste de Chile?', 'Océano Pacífico'),
    ('¿En qué continente se encuentra Egipto?', 'África'),
    ('¿Cuál es la capital de Japón?', 'Tokio');
*/

-- La primera pregunta debe ser contestada correctamente
-- por dos usuarios distintos
-- la primera pregunta debe estar contestada dos veces correctamente por distintos usuarios
/*
INSERT INTO respuestas (respuesta, usuario_id, pregunta_id) VALUES
    ('Santiago', 1, 1),
    ('Santiago', 2, 1);
*/

-- La pregunta 2 debe ser contestada correctamente por un usuario.
/*
INSERT INTO respuestas (respuesta, usuario_id, pregunta_id) VALUES
    ('Buenos Aires', 3, 2)
*/

-- Los otros dos registros deben ser respuestas 
-- incorrectas
/*
INSERT INTO respuestas (respuesta, usuario_id, pregunta_id) VALUES
    ('Atlantico', 4, 3),
    ('Oceania', 5, 4);
*/

-- Cuenta la cantidad de respuestas correctas 
-- totales por usuario (independiente de la
-- pregunta).
/*
select u.nombre, COUNT(r.*) respuesta_correcta
from usuarios u
	left join respuestas r ON r.usuario_id = u.id
	left join preguntas p ON p.id = r.pregunta_id
where r.respuesta = p.respuesta_correcta
group by u.nombre
*/

-- Probando la consulta
-- No ejecutar, solo para probar que todo
-- esta correcto
/*
INSERT INTO respuestas (respuesta, usuario_id, pregunta_id) VALUES
    ('Océano Pacífico', 1, 3)
*/

-- Ejemplo fuera de desafío
-- union
-- Combina los resultados de dos o más consultas 
-- SELECT en una sola lista de datos.
/*
select 'correctas' respuesta, u.nombre, COUNT(r.*) respuesta_correcta
from usuarios u
	left join respuestas r ON r.usuario_id = u.id
	left join preguntas p ON p.id = r.pregunta_id
where r.respuesta = p.respuesta_correcta
group by u.nombre
union
select 'incorrectas' respuesta, u.nombre, COUNT(r.*) respuesta_correcta
from usuarios u
	left join respuestas r ON r.usuario_id = u.id
	left join preguntas p ON p.id = r.pregunta_id
where r.respuesta <> p.respuesta_correcta
group by u.nombre
*/

-- Por cada pregunta, en la tabla preguntas, cuenta
-- cuántos usuarios tuvieron la respuesta correcta.
/*
select p.pregunta, COUNT(r.*) usuarios_resp_correcta
from usuarios u
	left join respuestas r ON r.usuario_id = u.id
	right join preguntas p ON p.id = r.pregunta_id
where r.respuesta = p.respuesta_correcta
group by p.pregunta
*/

/*
select p.pregunta, COUNT(r.*) usuarios_resp_correcta
from preguntas p
	left join respuestas r ON r.pregunta_id = p.id
	left join usuarios u ON u.id = r.usuario_id
where r.respuesta = p.respuesta_correcta
group by p.pregunta
*/

-- Implementar borrado en cascada para la tabla respuestas
-- cuando se borra un usuario
-- como ya existe el fk, debemos borrarlo y volver a crearlo
/*
ALTER TABLE respuestas
DROP CONSTRAINT respuestas_usuario_id_fkey;
*/
/*
ALTER TABLE respuestas
ADD CONSTRAINT respuestas_usuario_id_fkey
FOREIGN KEY (usuario_id)
REFERENCES usuarios (id)
ON DELETE CASCADE;
*/

-- Al borrar el usuario se debe borrar tambien
-- sus respuestas
--delete from usuarios where id = 1

/*
select * from usuarios
select * from respuestas where usuario_id = 1
*/



/*
select u.nombre, COUNT(r.*) respuesta_correcta
from usuarios u
	left join respuestas r ON r.usuario_id = u.id
	left join preguntas p ON p.id = r.pregunta_id
where r.respuesta = p.respuesta_correcta
group by u.nombre
*/


-- Crea una restricción que impida insertar usuarios menores de 18 años
-- en la base de datos.
/*
alter table usuarios
add constraint usuario_edad
check (edad >= 18)
*/

-- validar
/*
INSERT INTO usuarios (nombre, edad) VALUES
    ('Luis', 16)
*/

-- Altera la tabla existente de usuarios agregando el campo email
-- con la restricción de único.
/*
alter table usuarios
add column email varchar(255) unique
*/

-- Prueba
select * from usuarios

--update usuarios set email = 'algo@algo.com' where id = 2
update usuarios set email = 'algo@algo.com' where id = 4
