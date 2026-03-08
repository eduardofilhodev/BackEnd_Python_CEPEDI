class Componente:
    def __init__(self, nome):
        self.nome = nome


class Computador:
    def __init__(self, modelo):
        self.modelo = modelo
        self.componentes = []

    def adicionar_componente(self, nome):
        componente = Componente(nome)
        self.componentes.append(componente)

    def mostrar_componentes(self):
        print(f"Computador {self.modelo} possui:")
        for c in self.componentes:
            print(f"- {c.nome}")

    def destruir_computador(self):
        print(f"Destruindo o computador {self.modelo}...")
        self.componentes.clear()
        print("Todos os componentes foram removidos!")


# Programa principal
pc = Computador("PC Gamer")

pc.adicionar_componente("Processador")
pc.adicionar_componente("Memória RAM")
pc.adicionar_componente("SSD")

pc.mostrar_componentes()

print()

pc.destruir_computador()

print()

pc.mostrar_componentes()