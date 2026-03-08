-- 1 Atualização simples

UPDATE cliente
SET nome = 'Ana P. Ferreira'
WHERE id_cliente = 1;

UPDATE cliente
SET idade = 35
WHERE nome = 'Carlos Eduardo Silva';

UPDATE cliente
SET email = 'beatriz.santos@novoemail.com'
WHERE nome = 'Beatriz Santos';

-- 2 Atualização por condição

UPDATE cliente
SET estado = 'SP'
WHERE cidade = 'São Paulo';

UPDATE cliente
SET cidade = 'Belo Horizonte'
WHERE estado = 'MG';

UPDATE cliente
SET idade = idade + 1
WHERE sexo = 'F';

-- 3 Múltiplos campos

UPDATE cliente
SET telefone = '11999999999',
email = 'novo@email.com'
WHERE id_cliente = 6;

UPDATE cliente
SET cidade = 'São Paulo',
estado = 'SP',
cep = '04500-000'
WHERE nome = 'Julia Andrade';

-- 4 Filtros complexos

UPDATE cliente
SET endereco = CONCAT(endereco,' (Atualizado)')
WHERE endereco LIKE '%Rua%';

UPDATE cliente
SET nome = CONCAT(nome,' - VIP')
WHERE idade > 30;

UPDATE cliente
SET estado = 'RJ'
WHERE cep LIKE '220%';

-- 5 Intervalo

UPDATE cliente
SET telefone = CONCAT('119',telefone)
WHERE idade BETWEEN 25 AND 30;

UPDATE cliente
SET cep = '99999-999'
WHERE data_cadastro < '2025-03-01';

-- 6 Manutenção

UPDATE cliente
SET cep = REPLACE(cep,'-','');

UPDATE cliente
SET nome = UPPER(nome);

-- 7 Avançado

UPDATE cliente
SET idade = idade + 5
WHERE estado IN ('SP','RJ','MG');

UPDATE cliente
SET nome = CONCAT(nome,' - Verificar email')
WHERE email NOT LIKE '%.com';

-- 8 Subconsulta

UPDATE cliente
SET idade = 99
WHERE id_cliente = (SELECT MIN(id_cliente) FROM cliente);

UPDATE cliente
SET nome = CONCAT(nome,' (NOVO)')
WHERE data_cadastro = (SELECT MAX(data_cadastro) FROM cliente);