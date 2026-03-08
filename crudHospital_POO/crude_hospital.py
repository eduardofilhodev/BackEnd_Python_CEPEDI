class Paciente: 
    def __init__(self, nome, idade, peso, altura, diagnostico, obsrervacao=None):
        self.nome = nome
        self.idade = idade
        self.peso = peso    
        self.altura = altura
        self.diagnostico = diagnostico
        self.obsrervacao= obsrervacao
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc
    def exibir_informacoes(self):
        imc = self.calcular_imc()
        if len(self.obsrervacao) > 0:
            info = f"\nNome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso} kg\nAltura: {self.altura} m\nDiagnóstico: {self.diagnostico}\nObservação: {self.obsrervacao}\nIMC: {imc:.2f}"
            return info
        info = f"\nNome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso} kg\nAltura: {self.altura} m\nDiagnóstico: {self.diagnostico}\nIMC: {imc:.2f}"
        return info
    ############ ############## ############ ########### ############ ############## ############ ###########
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario
    def exibir_informacoes(self):
        info = f"\nNome: {self.nome}\nCargo: {self.cargo}\nSalário: R$ {self.salario:.2f}\n"
        return info
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,novo_salario):     
        if isinstance(novo_salario, (int, float)) and novo_salario >= 0:
            self.__salario= novo_salario
        else:
            raise ValueError("\nNovo salário deve ser um número positivo.")

#********************************#
class Medico(Funcionario):
    def __init__(self, nome, cargo, salario):
        super().__init__(nome,cargo,salario)
    def exibir_informacoes(self):
        return super().exibir_informacoes()
#********************************#
class Enfermeiro(Funcionario):
    def __init__(self, nome, cargo, salario):
        super().__init__(nome,cargo,salario)
    def exibir_informacoes(self):
        return super().exibir_informacoes()
      ############ ############## ############ ########### ############ ############## ############ ###########

class Validator:
    @staticmethod
    def validar_idade(valor):
        while True:
            try:
                idade = int(input(valor))
                if idade > 0:
                    return idade
                else:
                    print("Idade deve ser maior que zero!")
            except ValueError:
                print("Digite um número válido!")

    @staticmethod
    def validar_float(valor):
        while True:
            try:
                numero = float(input(valor))
                if numero > 0:
                    return numero
                else:
                    print("Valor deve ser maior que zero!")
            except ValueError:
                print("Digite um número válido!")
    
    @staticmethod
    def validar_string(valor):
        while True:
            texto = input(valor).strip()
            if texto and not isinstance(texto, (int, float)):
                return texto
            else:
                print("O campo não pode estar vazio ou ser numérico!")

############# ############## ############ ########### ############ ############## ############ ###########


def menu(opcao=None):
    print("\nMenu prontuário - Hospital XYZ\n")
    print("1. Cadastrar Paciente")
    print("2. Exibir Informações do Paciente")
    print("3. Exibir Informações do Médico")
    print("4. Exibir Informações do Enfermeiro")
    print("5. Sair")
    opcao= int(input("Escolha uma opção:"))
    
    return opcao

def menu_paciente():
    print("\n1. Pesquisar por nome")
    print("2. Exibir todos os pacientes")
    opcao_paciente= int(input("Escolha uma opção: "))
    return opcao_paciente


medico= Medico("Dr. Aira", "Obstetra", 30000.00)
enfermeiro= Enfermeiro("Enf. Beto", "Enfermeiro", 3500.00)
opcao=0
pacientes= []
while opcao !=5:
    opcao= menu()
    match opcao: 
        case 1:
            nome= Validator.validar_string("Nome do paciente: ")
            idade= Validator.validar_idade("Idade: ")
            peso= Validator.validar_float("Peso (kg): ")
            altura= Validator.validar_float("Altura (m): ")
            diagnostico= Validator.validar_string("Diagnóstico: ")
            observacao= input("Observação (opcional): ")
            pacientes.append(Paciente(nome, idade, peso, altura, diagnostico, observacao))
            #paciente= Paciente (input("Nome do paciente: "), int(input("Idade: ")), float(input("Peso (kg): ")), float(input("Altura (m): ")), input("Diagnóstico: "), input("Observação (opcional): "))
            #pacientes.append(paciente)
            print("\nPaciente cadastrado com sucesso!")

        case 2:
            opcao_paciente = 0
            while opcao_paciente not in [1, 2]:
                opcao_paciente = menu_paciente()
            match opcao_paciente:   
                case 1:
                    nome_pesquisa = Validator.validar_string("Digite o nome do paciente para exibir as informações: ")
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
                    print("\n--- Informações do Paciente ---")
                    if len(pacientes) == 0:
                        print("\nNenhum paciente cadastrado ainda!")
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
