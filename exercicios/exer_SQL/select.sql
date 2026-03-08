-- Seleção simples

SELECT * FROM cliente;

SELECT nome, cidade FROM cliente;

SELECT nome, idade, estado FROM cliente;

-- WHERE

SELECT * FROM cliente
WHERE estado = 'SP';

SELECT * FROM cliente
WHERE sexo = 'F';

SELECT * FROM cliente
WHERE idade > 30;

SELECT * FROM cliente
WHERE cidade = 'Rio de Janeiro';

SELECT * FROM cliente
WHERE email = 'rafaelgomes@email.com';

-- LIKE

SELECT * FROM cliente
WHERE nome LIKE 'J%';

SELECT * FROM cliente
WHERE email LIKE '%email%';

SELECT * FROM cliente
WHERE endereco LIKE '%Rua%';

-- ORDER

SELECT * FROM cliente
ORDER BY idade;

SELECT * FROM cliente
ORDER BY nome DESC;

SELECT * FROM cliente
ORDER BY data_cadastro DESC;

-- Agregação

SELECT COUNT(*) FROM cliente;

SELECT MAX(idade) FROM cliente;

SELECT MIN(idade) FROM cliente;

SELECT MAX(data_cadastro) FROM cliente;

SELECT estado, COUNT(*)
FROM cliente
GROUP BY estado;

-- GROUP BY

SELECT estado, COUNT(*)
FROM cliente
GROUP BY estado;

SELECT cidade, COUNT(*)
FROM cliente
GROUP BY cidade;

SELECT sexo, COUNT(*)
FROM cliente
GROUP BY sexo;

-- HAVING

SELECT estado, COUNT(*)
FROM cliente
GROUP BY estado
HAVING COUNT(*) > 1;

SELECT cidade, COUNT(*)
FROM cliente
GROUP BY cidade
HAVING COUNT(*) >= 2;

-- Datas

SELECT *
FROM cliente
WHERE data_cadastro > '2025-03-01';

SELECT *
FROM cliente
WHERE data_cadastro BETWEEN '2025-03-01' AND '2025-03-31';

-- Filtros compostos

SELECT *
FROM cliente
WHERE sexo = 'F'
AND estado = 'SP';

SELECT *
FROM cliente
WHERE idade BETWEEN 25 AND 35;

SELECT *
FROM cliente
WHERE estado IN ('SP','RJ','MG');

SELECT *
FROM cliente
WHERE nome LIKE '%a%'
AND sexo = 'F';

-- Alias

SELECT nome, email AS contato
FROM cliente;

SELECT id_cliente,
data_cadastro AS data_registro
FROM cliente;

-- LIMIT

SELECT *
FROM cliente
ORDER BY idade
LIMIT 3;

SELECT *
FROM cliente
ORDER BY data_cadastro DESC
LIMIT 2;

-- CASE

SELECT nome,
cidade,
CASE
WHEN idade >= 18 THEN 'Adulto'
ELSE 'Menor'
END AS classificacao
FROM cliente;