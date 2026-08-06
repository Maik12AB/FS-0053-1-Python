
-- La tabla esta recien creada por lo tanto regresa
-- cero registros
/*
SELECT *
FROM cocina_chilena
*/


-- Insertamos el primer registro de la tabla
-- no indicamos el id porque es una columna
-- autoingremental (serial)
/*
INSERT INTO cocina_chilena (nombre) values
   ('Pastel de choclo')
*/

-- Si volvemos a ejecutar el insert
-- observamos que se "duplica" el
-- nombre de Pastel de choclo
-- ahora tenemos dos registros
/*
INSERT INTO cocina_chilena (nombre) values
   ('Pastel de choclo')
*/


-- Agregamos un nuvo registro con
-- un error ortigrafico
/*
INSERT INTO cocina_chilena (nombre) values
   ('Umitas')
*/

-- Corregir el nombre
-- Para corregir registros que ya existen
-- se debe utilizar UPDATE
-- WARNING: UPDATE debe ir acompañado
-- de un WHERE
/*
UPDATE cocina_chilena
SET nombre = 'Humitas'
WHERE id=3
*/

-- Si ejecuto UPDATE sin WHERE modifica
-- todos los valores de la columna para
-- todas las filas
/*
UPDATE cocina_chilena
SET nombre = 'Humitas'
*/

-- Restauramos valores anteriores
/*
UPDATE cocina_chilena
SET nombre = 'Pastel de choclo'
WHERE id in (1, 2)
*/

-- Borrado de registros
-- Para borrar registros existentes
-- DELETE
/*
DELETE FROM cocina_chilena WHERE id=2
*/

-- Una vez que borramos un registro el valor
-- del id "se puerde" la BBDD no lo vuelve
-- a asignar.
-- A menos, que lo asignemos manualmente
-- pero esto seria una mala práctica

-- En este caso, insertara el nuevo
-- registro con id=4
/*
INSERT INTO cocina_chilena (nombre) values
   ('Cazuela')
*/


-- NOTA:
-- Se modifica la tabla cocina_chilena para que la columna
-- nombre solo almacene valores unicos.
/*
ALTER TABLE IF EXISTS public.cocina_chilena
    ADD CONSTRAINT nombre_unico UNIQUE (nombre);
*/

-- No permite agregar Cazuela porque este valor ya
-- existe en el id=4
/*
INSERT INTO cocina_chilena (nombre) values
   ('Cazuela')
*/


-- Observamos que asigna el id=6
-- El id=5 se "utilizo" con el error
-- la BBDD no regresa el id sino
-- que lo salta
/*
INSERT INTO cocina_chilena (nombre) values
   ('Empanada')
*/


-- Insertar varios registros a la vez
/*
INSERT INTO cocina_chilena (nombre) VALUES
	('Charquicán'),
	('Porotos con rienda'),
	('Mate con huesillo')
*/

-- - -------------------------------------------
-- Creamos la tabla de pedidos

-- Insertar un pedido
/*
INSERT INTO pedido (fecha, nombre, comida_id, unidades) VALUES
	('2026-08-05', 'Carlos Soto', 4, 1)
*/

-- Probar la FOREYKEY
/*
ERROR:  insert or update on table "pedido" violates foreign key constraint "comida_pedido"
Key (comida_id)=(100) is not present in table "cocina_chilena". 

SQL state: 23503
Detail: Key (comida_id)=(100) is not present in table "cocina_chilena".
*/
/*
INSERT INTO pedido (fecha, nombre, comida_id, unidades) VALUES
	('2026-08-05', 'Alvaro Catalan', 100, 1)
*/


-- Probar NOT NULL de nombre
/*
ERROR:  null value in column "nombre" of relation "pedido" violates not-null constraint
Failing row contains (3, 2026-08-05, null, 1, 1). 

SQL state: 23502
Detail: Failing row contains (3, 2026-08-05, null, 1, 1).
*/

/*
INSERT INTO pedido (fecha, comida_id, unidades) VALUES
	('2026-08-05', 1, 1)
*/



/*
SELECT *
FROM cocina_chilena
*/
/*
SELECT *
FROM pedido
*/
/*
SELECT p.id, p.fecha, p.nombre, c.nombre nombre_comida, p.unidades
FROM pedido p
	LEFT JOIN cocina_chilena c ON c.id = p.comida_id
*/


-- - CREAR TABLAS
/*
-- Table: public.cocina_chilena

-- DROP TABLE IF EXISTS public.cocina_chilena;

CREATE TABLE IF NOT EXISTS public.cocina_chilena
(
    id integer NOT NULL DEFAULT nextval('cocina_chilena_id_seq'::regclass),
    nombre character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT cocina_chilena_pkey PRIMARY KEY (id),
    CONSTRAINT nombre_unico UNIQUE (nombre)
)

TABLESPACE pg_default;
*/

/*
-- Table: public.pedido

-- DROP TABLE IF EXISTS public.pedido;

CREATE TABLE IF NOT EXISTS public.pedido
(
    id integer NOT NULL DEFAULT nextval('pedido_id_seq'::regclass),
    fecha date,
    nombre character varying(50) COLLATE pg_catalog."default" NOT NULL,
    comida_id integer,
    unidades smallint,
    CONSTRAINT pedido_pkey PRIMARY KEY (id),
    CONSTRAINT comida_pedido FOREIGN KEY (comida_id)
        REFERENCES public.cocina_chilena (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.pedido
    OWNER to postgres;
*/
