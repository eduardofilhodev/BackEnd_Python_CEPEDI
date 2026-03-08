-- Delete básico

DELETE FROM cliente
WHERE id_cliente = 7;

DELETE FROM cliente
WHERE nome = 'João Batista';

DELETE FROM cliente
WHERE email = 'carlossilva@email.com';

-- Por condição

DELETE FROM cliente
WHERE cidade = 'Curitiba';

DELETE FROM cliente
WHERE estado = 'RJ';

DELETE FROM cliente
WHERE idade > 35;

-- LIKE

DELETE FROM cliente
WHERE nome LIKE 'A%';

DELETE FROM cliente
WHERE telefone LIKE '41%';

DELETE FROM cliente
WHERE email LIKE '%@email.com';

-- Múltiplas condições

DELETE FROM cliente
WHERE sexo = 'M'
AND cidade = 'São Paulo';

DELETE FROM cliente
WHERE idade BETWEEN 20 AND 30;

DELETE FROM cliente
WHERE endereco LIKE '%Av.%';

-- Segurança

DELETE FROM cliente
WHERE LENGTH(cep) < 8;

DELETE FROM cliente
WHERE data_cadastro < '2025-02-01';

DELETE FROM cliente
WHERE estado NOT IN ('SP','RJ','MG','PR','RS','DF');

-- Avançado

DELETE FROM cliente
WHERE idade = (SELECT MAX(idade) FROM cliente);

DELETE FROM cliente
WHERE data_cadastro = (SELECT MAX(data_cadastro) FROM cliente);

DELETE FROM cliente
WHERE id_cliente >
(SELECT AVG(id_cliente) FROM cliente);