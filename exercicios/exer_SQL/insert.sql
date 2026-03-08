-- 1
INSERT INTO cliente
VALUES (
(SELECT MAX(id_cliente)+1 FROM cliente),
'Marcos Silva', 32, 'M',
'marcos.silva@email.com',
'(71)99999-1111',
'Rua A, 123',
'Salvador',
'BA',
'40000-000',
'2025-01-10'
);

-- 2
INSERT INTO cliente
(id_cliente, nome, idade, cidade, estado, data_cadastro)
VALUES (
(SELECT MAX(id_cliente)+1 FROM cliente),
'Ana Souza',
28,
'Recife',
'PE',
'2025-01-15'
);

-- 3
INSERT INTO cliente
(id_cliente, nome, idade, sexo, email, cidade, estado, data_cadastro)
VALUES
((SELECT MAX(id_cliente)+1 FROM cliente),'Paulo Ramos',40,'M','paulo@gmail.com','Rio de Janeiro','RJ','2025-01-20'),
((SELECT MAX(id_cliente)+2 FROM cliente),'Beatriz Santos',22,'F','bia22@hotmail.com','Belo Horizonte','MG','2025-01-22'),
((SELECT MAX(id_cliente)+3 FROM cliente),'Juliana Torres',35,'F','julianatorres@gmail.com','Curitiba','PR','2025-01-25');

-- 4
INSERT INTO cliente
(id_cliente, nome, sexo, cidade, estado, data_cadastro)
VALUES (
(SELECT MAX(id_cliente)+1 FROM cliente),
'Carlos Mendes',
'M',
'Fortaleza',
'CE',
'2025-02-01'
);

-- 5
INSERT INTO cliente
(id_cliente, nome, idade, sexo, endereco, cidade, estado, cep, data_cadastro)
VALUES (
(SELECT MAX(id_cliente)+1 FROM cliente),
'Fernanda Lima',
29,
'F',
'Av. das Flores, 890',
'Manaus',
'AM',
'69000-200',
'2025-02-05'
);

-- 6
INSERT INTO cliente
(id_cliente, nome, sexo, cidade, estado, data_cadastro)
VALUES
((SELECT MAX(id_cliente)+1 FROM cliente),'Roberto Alves','M','Goiânia','GO','2025-02-10'),
((SELECT MAX(id_cliente)+2 FROM cliente),'Patrícia Oliveira','F','Vitória','ES','2025-02-11'),
((SELECT MAX(id_cliente)+3 FROM cliente),'João Lucas','M','São Luís','MA','2025-02-12');

-- 7
INSERT INTO cliente
(id_cliente, nome, idade, sexo, email, telefone, cidade, estado, data_cadastro)
VALUES (
(SELECT MAX(id_cliente)+1 FROM cliente),
'Lara Costa',
26,
'F',
'lara.costa@empresa.com',
'+55 11 98888-7777',
'São Paulo',
'SP',
'2025-02-15'
);

-- 8
INSERT INTO cliente
(id_cliente, nome, cidade, estado, data_cadastro)
SELECT
(SELECT MAX(id_cliente)+1 FROM cliente),
nome,
cidade,
estado,
'2025-02-18'
FROM cliente
WHERE id_cliente = 1;