-- Agregamos dos cuentas bancarias
-- Iniciamos el balance con 1.000 cada una
/*
insert into cuentas (numero_cuenta, balance) values
	(100, 1000),
	(200, 1000)
*/

--UPDATE cuentas set numero_cuenta = numero_cuenta * 100

-- Tranferir 1.000 de la cuenta1 a la cuenta2
-- Estas transacciones donde resto a una cuenta y aumento
-- a la otra cuenta, se debe ejecutar ambas transacciones
-- si o si.
/*
BEGIN TRANSACTION;
UPDATE cuentas SET balance = balance - 1000 WHERE id = 1;
UPDATE cuentas SET balance = balance + 1000 WHERE id = 2;
COMMIT;
*/


-- Agregamos una nueva cuenta
/*
insert into cuentas (numero_cuenta, balance) values
	(300, 1000)
*/

-- Transferir 1.000 de la cuenta 300 a la cuenta 100
/*
BEGIN TRANSACTION;
UPDATE cuentas SET balance = balance - 1000 WHERE id = 3;
UPDATE cuentas SET balance = balance + 1000 WHERE id = 1;
*/

--ROLLBACK




/*
SELECT *
FROM cuentas
*/
