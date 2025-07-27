# Lista para armazenar livros cadastrados
lista_livros = []

# Variável para gerar IDs
id_global = 0

# Função para cadastrar um novo livro
def cadastrar_livro(id_global):
    id_global += 1
    
    # Cria um dicionário com os dados do livro
    livro = {
        'id': id_global,
        'nome': input('Nome: '),  
        'autor': input('Autor: '), 
        'editora': input('Editora: ')  
    }
    
    # Adiciona o livro à lista
    lista_livros.append(livro)
    
    # Confirmação do cadastro com o ID
    resposta = input('Cadastrar outro? [S/N]').upper()
    if resposta == 'S':
        cadastrar_livro(id_global)
    elif resposta == 'N':
        print(lista_livros)
        menu()
    else:
        print('\nERROR! Resposta inválida. Tente novamente.')

# Função para consultar livros
def consultar_livro():
    print("\n1 - Todos")
    print("2 - Por ID")
    print("3 - Por Autor")
    opcao = int(input("Selecione a opção desejada: "))

    if opcao == 1:
        for livro in lista_livros:
            print(f"ID: {livro['id']} | {livro['nome']}")

    elif opcao == 2:
        id_busca = int(input("ID: "))
        for livro in lista_livros:
            if livro['id'] == id_busca:
                print(f"\nNome: {livro['nome']}\nAutor: {livro['autor']}\nEditora: {livro['editora']}")
                return  
        print("\nLivro não encontrado!")
    
    elif opcao == 3:
        autor = str(input("Autor: "))
        for livro in lista_livros:
            if livro['autor'] in autor:
                print(f"\nID: {livro['id']} | Nome: {livro['nome']}")

# Função para remover livro
def remover_livro():
    id_remover = int(input("ID para remover: "))
    
    # Percorre a lista de livros
    for i, livro in enumerate(lista_livros):
        if livro['id'] == id_remover:
            lista_livros.pop(i)  # Remove o livro da lista
            print("\nLivro removido!")
            return
    print("ID não encontrado!")

def menu():
    while True:
        print("\nBem-vindo a livraria JP")
        print("\n" + "-"*30)
        print("1 - Cadastrar")
        print("2 - Consultar")
        print("3 - Remover")
        print("4 - Sair\n")
        opcao = input("Opção: ")
        
        if opcao == '1': 
            cadastrar_livro(id_global)
        elif opcao == '2': 
            consultar_livro()
        elif opcao == '3': 
            remover_livro()
        elif opcao == '4': 
            break
        else: 
            print("\nOpção inválida. Tente novamente.") 

# Inicia o programa
menu()

