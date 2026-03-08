
# Sistema de Gestão de Cursos – Escola Técnica

## Estrutura do Projeto
- tabelas.sql → criação das tabelas (modelagem física)
- inserts.sql → dados de exemplo
- queries.sql → consultas de teste

## Entidades

Aluno, Prontuario, Curso, Professor, Contrato e Professor_Curso.

## Relacionamentos
Aluno (1) — (1) Prontuario  
Curso (1) — (N) Aluno  
Professor (1) — (1) Contrato  
Professor (N) — (N) Curso (tabela associativa Professor_Curso)
