
-- listar alunos e seus cursos
SELECT aluno.nome, curso.nome_curso
FROM aluno
JOIN curso ON aluno.id_curso = curso.id_curso;

-- listar professores e cursos que lecionam
SELECT professor.nome, curso.nome_curso
FROM professor
JOIN professor_curso pc ON professor.id_professor = pc.id_professor
JOIN curso ON pc.id_curso = curso.id_curso;

-- ver prontuário dos alunos
SELECT aluno.nome, prontuario.situacao, prontuario.data_matricula
FROM aluno
JOIN prontuario ON aluno.id_aluno = prontuario.id_aluno;
