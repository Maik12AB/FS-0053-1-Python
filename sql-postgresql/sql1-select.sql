-- Extraer datos de una base de datos

-- Doble guion comentario de 1 línea

/*
Para
comentarios
de
varias
líneas
*/

-- sintaxis es como se escribe algo
-- sentencia lo que deseamos ejecutar

-- sintaxis de SELECT
/*
SELECT *
FROM <Tabla>
[WHERE <condición>]
[GROUP BY <columnas>]
[HAVING <condición>]
[ORDER BY <columnas>]
...
*/

-- Sentencia
-- Es la forma más básica de consultar datos
/*
SELECT *
FROM Customer
*/

-- Cómo listar solo algunas columnas
/*
SELECT customer_id, first_name, last_name, city, state, country
FROM Customer
*/

-- Uso de Alias
-- Palaba AS es opcional
/*
SELECT customer_id AS cliente_id, first_name AS primer_nombre, last_name AS primer_apellido,
	city ciudad, state estado, country pais
FROM Customer
*/


-- Columnas calculadas
-- Las columnas calculadas se crean sin nombre de columna (valido para humanos)
-- Utilizar siempre un alias para que el nombre de la columna sea semantico
/*
SELECT customer_id AS cliente_id, first_name AS primer_nombre, last_name AS primer_apellido,
	city ciudad, state estado, country pais, (2 + 2) suma
FROM Customer
*/

-- Crear una columna con el nombre completo
-- || doble barra son el operador de concatenación en PostgreSQL
/*
SELECT customer_id, UPPER( first_name || ' ' || last_name ) full_name
FROM Customer
*/



-- Modificadores de consultas
-- Modifican el resultado de la consulta

-- ALL
-- Es el comportamiento predeterminado
-- No es necesario incluirlo
/*
SELECT ALL customer_id AS cliente_id, first_name AS primer_nombre, last_name AS primer_apellido,
	city ciudad, state estado, country pais
FROM Customer
*/

-- LIMIT
-- Filtra el número de filas que puedo obtener en la consulta
/*
SELECT customer_id AS cliente_id, first_name AS primer_nombre, last_name AS primer_apellido,
	city ciudad, state estado, country pais
FROM Customer
LIMIT 3
*/

-- DISTINCT
-- Según las columnas solicitadas devuelve filas unicas (1 vez)

-- Devuelve todos los paises, los paises aparecen varias veces
/*
SELECT country pais
FROM Customer
*/

-- Devuelve cada país una sola vez
/*
SELECT DISTINCT country pais
FROM Customer
*/

-- Filtro por filas
/*
SELECT *
FROM Customer
WHERE country = 'Brazil'
*/

-- Filtrar filas que contienen null
/*
SELECT *
FROM Customer
WHERE state is null
*/

-- Seleccionando clientes que pertenecen a Chile o Argentina
/*
SELECT *
FROM Customer
WHERE Country = 'Chile' or Country = 'Argentina'
*/

-- Filtrando valores numéricos
/*
SELECT *
FROM Invoice
WHERE total >= 10
*/

-- Filtrado por fecha
-- Lo mejor es utilizar la ISO 8601 para
-- hacer referencia a las fechas
/*
SELECT *
FROM Invoice
WHERE invoice_date = '2025-01-30'
*/

-- Clausula especial
-- BETWEEN
/*
SELECT invoice_id, customer_id, invoice_date, total
FROM Invoice
WHERE total >= 10 and total <= 15
*/

/*
SELECT invoice_id, customer_id, invoice_date, total
FROM Invoice
WHERE total BETWEEN 10 and 15
*/

-- IN
-- Valida que un valor exista en una lista
/*
SELECT *
FROM Customer
WHERE Country IN ('Chile', 'Argentina')
*/

-- Mostrando registros que no pertenecen a esos paices
/*
SELECT *
FROM Customer
WHERE Country NOT IN ('Chile', 'Argentina')
*/

-- - ------------------------
-- Funciones de agregado
/*
SELECT *
FROM Invoice
*/

-- Contar el número de filas
/*
SELECT COUNT(*) total_invoice
FROM Invoice
*/

/*
SELECT COUNT(*) cantidad_invoice,
	SUM(total) total_facturado,
	AVG(total) factura_promedio,
	ROUND( AVG(total), 3) factura_promedio_redondeado,
	MIN(total) monto_minimo_facturado,
	MAX(total) monto_maximo_facturado
FROM Invoice
*/

-- Suma de total de ventas por país
/*
SELECT billing_country, SUM(total) facturado
FROM Invoice
GROUP BY billing_country
*/

-- Ordenando la consulta
-- ASC (Valor predeterminado) | DESC
SELECT billing_country, SUM(total) facturado
FROM Invoice
GROUP BY billing_country
ORDER BY facturado DESC
