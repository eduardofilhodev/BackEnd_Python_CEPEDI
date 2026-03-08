 
class Prontuario:
    def __init__(self, diagnostico, observacao=None):
        self.diagnostico = diagnostico
        self.observacao = observacao


class Paciente:
    def __init__(self, nome, idade, peso, altura, diagnostico, observacao=None, medico=None):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

        
        self.prontuario = Prontuario(diagnostico, observacao)

        # ASSOCIAÇÃO (Paciente pode ter um médico)
        self.medico = medico

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def exibir_informacoes(self):
        imc = self.calcular_imc()

        info = f"\nNome: {self.nome}"
        info += f"\nIdade: {self.idade}"
        info += f"\nPeso: {self.peso} kg"
        info += f"\nAltura: {self.altura} m"
        info += f"\nDiagnóstico: {self.prontuario.diagnostico}"

        if self.prontuario.observacao:
            info += f"\nObservação: {self.prontuario.observacao}"

        if self.medico:
            info += f"\nMédico responsável: {self.medico.nome}"

        info += f"\nIMC: {imc:.2f}"

        return info


# SUPERCLASSE
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo

        # ATRIBUTO PRIVADO
        self.__salario = salario

    def exibir_informacoes(self):
        return f"\nNome: {self.nome}\nCargo: {self.cargo}\nSalário: R$ {self.salario:.2f}"

    # GETTER
    @property
    def salario(self):
        return self.__salario

    # SETTER
    @salario.setter
    def salario(self, novo_salario):
        if isinstance(novo_salario, (int, float)) and novo_salario >= 0:
            self.__salario = novo_salario
        else:
            raise ValueError("Salário inválido!")


# SUBCLASSE
class Medico(Funcionario):

    # POLIMORFISMO + OVERRIDE
    def exibir_informacoes(self):
        return f"\n👨‍⚕️ Médico\n{super().exibir_informacoes()}"


# SUBCLASSE
class Enfermeiro(Funcionario):

    
    def exibir_informacoes(self):
        return f"\n🩺 Enfermeiro\n{super().exibir_informacoes()}"
    
class PacienteErro(Exception):
    pass



class Validator:

    @staticmethod
    def validar_idade(valor):
        while True:
            try:
                idade = int(input(valor))
                if idade > 0:
                    return idade
                else:
                    raise PacienteErro("Idade deve ser maior que zero!")
            except ValueError:
                print("Digite um número válido!")
            except PacienteErro as e:
                print(e)

    @staticmethod
    def validar_float(valor):
        while True:
            try:
                numero = float(input(valor))
                if numero > 0:
                    return numero
                else:
                    raise PacienteErro("Valor deve ser maior que zero!")
            except ValueError:
                print("Digite um número válido!")
            except PacienteErro as e:
                print(e)

    @staticmethod
    def validar_string(valor):
        while True:
            texto = input(valor).strip()
            if texto:
                return texto
            else:
                print("O campo não pode estar vazio!")


def menu():
    print("\nMenu prontuário - Hospital XYZ\n")
    print("1. Cadastrar Paciente")
    print("2. Exibir Informações do Paciente")
    print("3. Exibir Informações do Médico")
    print("4. Exibir Informações do Enfermeiro")
    print("5. Sair")

    return int(input("Escolha uma opção: "))


def menu_paciente():
    print("\n1. Pesquisar por nome")
    print("2. Exibir todos os pacientes")

    return int(input("Escolha uma opção: "))


medico = Medico("Dr. Aira", "Obstetra", 30000)
enfermeiro = Enfermeiro("Enf. Beto", "Enfermeiro", 3500)

pacientes = []
opcao = 0

while opcao != 5:

    opcao = menu()

    match opcao:

        case 1:
            nome = Validator.validar_string("Nome do paciente: ")
            idade = Validator.validar_idade("Idade: ")
            peso = Validator.validar_float("Peso (kg): ")
            altura = Validator.validar_float("Altura (m): ")
            diagnostico = Validator.validar_string("Diagnóstico: ")
            observacao = input("Observação (opcional): ")

            paciente = Paciente(nome, idade, peso, altura, diagnostico, observacao, medico)

            pacientes.append(paciente)

            print("\nPaciente cadastrado com sucesso!")

        case 2:

            opcao_paciente = menu_paciente()

            match opcao_paciente:

                case 1:

                    nome_pesquisa = Validator.validar_string("Digite o nome do paciente: ")

                    paciente_encontrado = False

                    for p in pacientes:
                        if p.nome.lower() == nome_pesquisa.lower():

                            print("\n--- Informações do Paciente ---")
                            print(p.exibir_informacoes())

                            paciente_encontrado = True
                            break

                    if not paciente_encontrado:
                        print("\nPaciente não encontrado!")

                case 2:

                    if len(pacientes) == 0:
                        print("\nNenhum paciente cadastrado!")
                    else:
                        print("\n--- Lista de Pacientes ---\n")

                        for p in pacientes:
                            print(p.exibir_informacoes())
                            print("-" * 40)

        case 3:

            print("\n--- Informações do Médico ---")
            print(medico.exibir_informacoes())

        case 4:

            print("\n--- Informações do Enfermeiro ---")
            print(enfermeiro.exibir_informacoes())

        case 5:
            print("Saindo do sistema...")