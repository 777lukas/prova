import json
produto = []
categoria = []

id_categoria = 0
id_produto = 0

def carregar_arquivo(eletronico):
    try:
        with open(eletronico, 'r') as arquivo:
            dados = json.load(arquivo)
            print(f"Arquivo {eletronico} carregado!")
            return dados
    except FileNotFoundError:
        print(f"Arquivo não encontrado. Criando novo arquivo.")
        return []


def exibir_menu():
    print(".........chash royale.........")
    print("1.Cadastrar Categoria")
    print("2.cadastrar produto")
    print("3.listar produto")
    print("4. the end")

def cadastrar_categoria():
    global id_categoria
    print("/cadastrar produto:")
    nome_categoria = input ("Nome: ")
    id_categoria +=1

    armazem_categoria = {
        "nome_categoria" : nome_categoria,
        "id_categoria" : id_categoria
     }

    categoria.append(armazem_categoria)
    print("salvo")
     
def cadastrar_produto():
    global produtos_id
    nome_produto = input("Nome do produto: ")
    preco = float(input("Preço: "))
    id_categoria = int(input("ID da categoria: "))
    produtos_id += 1
    produto = {
        "id": produtos_id,
        "nome": nome_produto,
        "preco": preco,
        "id_categoria": id_categoria
    }

def listar_categorias():
    if categoria:
        print("CATEGORIAS:")
        for c in categoria:
            print(f"ID: {c['id']} - Nome: {c['nome']}")
    else:
        print("Nenhuma categoria cadastrada.")

def listaProdutos():
    produtos = cadastrar_categoria()
    
    if not produtos:
        print("\nNenhum produto cadastrado.")
    else:
        print("\n----- Produtos -----")
        for p in produtos:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Preço: R$ {p['preco']:.2f}")

def MenuPrincipal():
    while True:
        funcao = input("\n--- Loja da cheems ---\n1. Cadastrar novo produto\n2. Listar Produtos\n3. Sair\nOpção: ")
        
        match funcao:
            case "1":
                cadastrar_produto()
            case "2":
                listaProdutos()
            case "3":
                print("\nSaindo...")
                break
            case _:
                print("\nOpção inválida, tente novamente.")
MenuPrincipal()