
# Sistema de Gestão de Cursos – Escola Técnica

## Estrutura do Projeto

- schema.sql → criação das tabelas (modelagem física)
- inserts.sql → dados de exemplo
- queries.sql → consultas de teste
- der.png → diagrama entidade‑relacionamento
- README.md → explicação do projeto

## Entidades

Aluno, Prontuario, Curso, Professor, Contrato e Professor_Curso.

## Relacionamentos

Aluno (1) — (1) Prontuario  
Curso (1) — (N) Aluno  
Professor (1) — (1) Contrato  
Professor (N) — (N) Curso (tabela associativa Professor_Curso)

## Como executar

1. Crie um banco de dados (ex: SQLite).
2. Execute:
   - schema.sql
   - inserts.sql
3. Teste consultas em queries.sql.
