-- Desafío 2

-- ¿Cuantos registros hay?
/*
SELECT COUNT(*)
FROM inscritos;
*/

-- ¿Cuántos inscritos hay en total?
/*
SELECT SUM(cantidad)
FROM inscritos
*/

-- ¿Cuál o cuáles son los registros de mayor antigüedad?
/*
SELECT *
FROM inscritos
WHERE fecha = (SELECT MIN(fecha) FROM inscritos)
ORDER BY fecha;
*/

-- ¿Cuántos inscritos hay por día? (entendiendo un día como una fecha distinta de ahora en adelante)
/*
SELECT fecha, sum(cantidad) inscrito_dias
FROM inscritos
GROUP BY fecha
ORDER BY fecha;
*/

-- ¿Qué día se inscribieron la mayor cantidad de personas y cuántas personas se inscribieron en ese día?
/*
SELECT fecha, SUM(cantidad) inscrito_dias
FROM inscritos
GROUP BY fecha
ORDER BY inscrito_dias DESC
LIMIT 1;
*/
