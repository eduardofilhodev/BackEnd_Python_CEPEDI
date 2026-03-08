
CREATE TABLE curso (
    id_curso INTEGER PRIMARY KEY,
    nome_curso TEXT,
    carga_horaria INTEGER
);

CREATE TABLE aluno (
    id_aluno INTEGER PRIMARY KEY,
    nome TEXT,
    cpf TEXT,
    data_nascimento DATE,
    id_curso INTEGER,
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
);

CREATE TABLE prontuario (
    id_prontuario INTEGER PRIMARY KEY,
    data_matricula DATE,
    situacao TEXT,
    id_aluno INTEGER UNIQUE,
    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno)
);

CREATE TABLE professor (
    id_professor INTEGER PRIMARY KEY,
    nome TEXT,
    especialidade TEXT
);

CREATE TABLE contrato (
    id_contrato INTEGER PRIMARY KEY,
    carga_horaria_semanal INTEGER,
    tipo_vinculo TEXT,
    id_professor INTEGER UNIQUE,
    FOREIGN KEY (id_professor) REFERENCES professor(id_professor)
);

CREATE TABLE professor_curso (
    id_professor INTEGER,
    id_curso INTEGER,
    PRIMARY KEY (id_professor, id_curso),
    FOREIGN KEY (id_professor) REFERENCES professor(id_professor),
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
);
