class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            disciplina.adicionar_professor(self)

    def mostrar_disciplinas(self):
        print(f"Professor {self.nome} leciona:")
        for d in self.disciplinas:
            print(f"- {d.nome}")


class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)

    def mostrar_professores(self):
        print(f"Disciplina {self.nome} é ministrada por:")
        for p in self.professores:
            print(f"- {p.nome}")


# Programa principal
prof1 = Professor("Carlos")
prof2 = Professor("Ana")

disc1 = Disciplina("Matemática")
disc2 = Disciplina("Física")

# associação
prof1.adicionar_disciplina(disc1)
prof1.adicionar_disciplina(disc2)
prof2.adicionar_disciplina(disc2)

# mostrando relações
prof1.mostrar_disciplinas()
prof2.mostrar_disciplinas()

print()

disc1.mostrar_professores()
disc2.mostrar_professores()