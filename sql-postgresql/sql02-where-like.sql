-- Clausula especial LIKE
-- Se usa en conjunto con WHERE
-- Busca patrones en columnas
-- de texto

-- % es un comodin
-- Representa/sustituye cero, uno o más caracteres
/*
SELECT *
FROM Customer
WHERE first_name LIKE 'F%'
*/

/*
SELECT *
FROM Customer
WHERE address LIKE '%4th%'
*/

/*
SELECT *
FROM Customer
WHERE first_name LIKE '%eus%'
	or last_name LIKE '%eus%'
	or company LIKE '%eus%'
	or address LIKE '%eus%'
*/

-- _ guion bajo sustituye un caracter
/*
SELECT *
FROM Customer
WHERE first_name LIKE '_a_a'
*/

SELECT *
FROM Customer
WHERE first_name LIKE '_a_a%'







-- Expresiones regulares (REGEX)
-- validar un correo electrónico
-- algo@algo.com

-- @ tenemos uno y solo un arroba
-- a la izquierda del arriba debo tener texto
-- a la derecha del arroba debo teber texto
-- a la derecha del arroba debo tener al menos un punto

-- RUT
-- 99999999-9
-- Un guion
-- a la derecha del guin debemos tener un numero entra 0 y 9 o k y debe ser un solo caracter
-- a la izquierda debemos tener puros digitos y deben ser 7 u 8

