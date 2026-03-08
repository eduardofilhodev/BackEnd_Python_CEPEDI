#Declarações e funções:

produtos={
    "001": {"nome": "Arroz", "preco": 5.50, "estoque": 100},
    "002": {"nome": "Feijão", "preco": 7.80, "estoque": 80},
    "003": {"nome": "Macarrão", "preco": 4.20, "estoque": 150},
    "004": {"nome": "Óleo de Soja", "preco": 6.30, "estoque": 60},
    "005": {"nome": "Açúcar", "preco": 3.90, "estoque": 90},
    
}  
código_desconto_cliente= {"CLIENTE10": 0.10, "CLIENTE20": 0.20}

lista_funcionarios= ['Ana Silva', 'Bruno Souza', 'Carla Pereira', 'Daniel Costa']

senha_acesso_gerente= ("123")


def menu_principal():
    print("=== Sistema de Gerenciamento de Mercado ===")
    print("1. Menu do Gerente")
    print("2. Menu do Cliente")
    print("3. Sair")
    opcao_principal= int(input("Escolha uma opção: "))
    return opcao_principal

def menu_gerente():
    print("=== Menu do Gerente ===")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Atualizar Informações do Produto")
    print("4. Visualizar Produtos")
    print("5. Visualizar Funcionários")
    print("6. Sair")
    opcao_gerente= int(input("Escolha uma opção: "))
    return opcao_gerente 

def menu_cliente():
    print("=== Menu do Cliente ===")
    print("1. Carrinho de Compras")
    print("2. Sair")
    opcao_cliente= int(input("Escolha uma opção: "))
    return opcao_cliente

def adicionar_produto():
    codigo = input("Digite o código do produto: ")
    if codigo in produtos:
        return print("Produto já existe.\n")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    produtos[codigo] = {"nome": nome, "preco": preco, "estoque": estoque}
    print("Produto adicionado com sucesso.")

def remover_produto():
    codigo = input("Digite o código do produto a ser removido: ")
    if codigo in produtos:
        del produtos[codigo]
        print("Produto removido com sucesso.")
    else:
        print("Produto não encontrado.")

    
def atualizar_info_produto():
    codigo = input("Digite o código do produto para atualizar as informações: ")
    
    if codigo in produtos:
        while True:
            nome = input("Digite o novo nome do produto (deixe em branco para não alterar): ").strip()

            if nome != "" and not all(parte.isalpha() for parte in nome.split()):
                #Isalpha não aceita espaços, por isso o split e o all
                print("Nome inválido. Use apenas letras e espaços.")
                continue

            preco_input = input("Digite o novo preço do produto (deixe em branco para não alterar): ").strip()
            if preco_input:
                try:
                    preco = float(preco_input)
                    if preco < 0:
                        print("Preço não pode ser negativo.")
                        continue
                except ValueError:
                    print("Preço inválido. Digite um número.")
                    continue

            estoque_input = input("Digite a nova quantidade em estoque (deixe em branco para não alterar): ").strip()
            if estoque_input:
                if not estoque_input.isdigit():
                    print("Estoque inválido. Digite um número inteiro.")
                    continue
                estoque = int(estoque_input)
                if estoque < 0:
                    print("Estoque não pode ser negativo.")
                    continue

            if nome:
                produtos[codigo]["nome"] = nome
            if preco_input:
                produtos[codigo]["preco"] = preco
            if estoque_input:
                produtos[codigo]["estoque"] = estoque

            print("Informações do produto atualizadas com sucesso.")
            break

    else:
        print("Produto não encontrado.")



def visualizar_produtos():
    print("=== Lista de Produtos ===")
    for codigo, info in produtos.items():
        print(f"Código: {codigo}, Nome: {info['nome']}, Preço: R${info['preco']:.2f}, Estoque: {info['estoque']} unidades")

def carrinho_compras():
    visualizar_produtos()
    carrinho = {}
    while True:
        codigo = input("Digite o código do produto para adicionar ao carrinho (ou 'sair' para finalizar): ")
        if codigo.lower() == 'sair':
            break
        if codigo in produtos:
            quantidade = int(input("Digite a quantidade desejada: "))
            if quantidade <= produtos[codigo]['estoque']:
                if codigo in carrinho:
                    carrinho[codigo]['quantidade'] += quantidade
                else:
                    carrinho[codigo] = {
                        'nome': produtos[codigo]['nome'],
                        'preco': produtos[codigo]['preco'],
                        'quantidade': quantidade
                    }
                produtos[codigo]['estoque'] -= quantidade
                print(f"{quantidade} unidades de {produtos[codigo]['nome']} adicionadas ao carrinho.")
            else:
                print("Quantidade solicitada excede o estoque disponível.")
        else:
            print("Produto não encontrado.")
    
    
    print("=== Carrinho de Compras ===")
    total = 0
    for codigo, item in carrinho.items():
        subtotal = item['preco'] * item['quantidade']
        total += subtotal 
        print(f"Código: {codigo}, Nome: {item['nome']}, Preço: R${item['preco']:.2f}, Quantidade: {item['quantidade']}, Subtotal: R${subtotal:.2f}")
    print(f"Total a pagar: R${total:.2f}")

######### ########## ########### ########### ########### ########### ########### ########### ########### ###########

opcao_principal=0
while opcao_principal!=3:   
    try:
        opcao_principal= menu_principal()
    except ValueError:
        print("Entrada inválida. Por favor, insira um número correspondente às opções do menu.")
        continue
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        continue

    match opcao_principal:
        case 1:
            
            while True:
                senha_digitada= input("Digite a senha de acesso do gerente: ")
                if senha_digitada == senha_acesso_gerente:
                    print("Acesso concedido ao menu do gerente.\n")
                    break
                else:
                    print("Senha incorreta. Tente novamente.\n")

            opcao_gerente=0
            while opcao_gerente!=6:
                try:
                    opcao_gerente= menu_gerente()
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número correspondente às opções do menu.")
                    continue
                except Exception as e:
                    print(f"Ocorreu um erro: {e}")
                    continue

                match opcao_gerente:
                    case 1:
                        adicionar_produto()
                    case 2:
                        remover_produto()
                    case 3:
                        atualizar_info_produto()
                    case 4:
                        visualizar_produtos()
                    case 5:
                        print("Funcionários do mercado:")
                        for funcionario in lista_funcionarios:
                            print(f"- {funcionario}")
                    case 6:
                        print("Saindo do menu do gerente...")
                    case _:
                        print("Opção inválida. Tente novamente.")
        case 2:
            opcao_cliente=0
            while opcao_cliente!=2:
                try:
                    opcao_cliente= menu_cliente()
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número correspondente às opções do menu.")
                    continue
                except Exception as e:
                    print(f"Ocorreu um erro: {e}")
                    continue

                match opcao_cliente:
                    case 1:
                        print("Acessando o carrinho de compras...\n")
                        carrinho_compras()
                    case 2:
                        print("Saindo do menu do cliente...")
                    case _:
                        print("Opção inválida. Tente novamente.")
        case 3:
            print("Saindo do sistema...")
        case _:
            print("Opção inválida. Tente novamente.")
