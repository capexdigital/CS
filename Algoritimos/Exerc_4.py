div1 = '-' * 30
print(div1)
print('Bem vindo a Livraria do Joao\n')

livro = []
listaLivro = []

id_global = 0

#Cadastrar Livro
def cadastrar_livro(id_global):
    for i in range(1):
        listaLivro.append(str(input('Nome:')))
        listaLivro.append(str(input('Autor:')))
        listaLivro.append(str(input('Editora:')))
        id_global = id_global + 1
        livro.append(listaLivro[:])
        livro.clear()
        print('\n')
        print(f'id - {id_global}')
        print(listaLivro)
        res = input('Deseja fazer mais um cadastro? [S/N]')
        if res in 'Nn':
            print(listaLivro)
            break
        else:
            cadastrar_livro(id_global)
        break


#Consultar Livro
def consultar_livro():
    print('consultar')
        

# Remover Livro
def remover_livro():
    print('remover')

# Sair 
def sair():
    print('sair')
    



# Loop para escolha de opções do menu
def menu():
    while True:
        div1 = '-' * 30
        print(div1)
        print('Bem vindo a Livraria do Joao\n')
        print('1 - CADASTRAR LIVRO')
        print('2 - CONSULTAR LIVRO')
        print('3 - REMOVER LIVRO')
        print('4 - SAIR\n')
        EscolhaMenu = int(input("Selecione a opção desejada:"))
        if EscolhaMenu == 1:
            cadastrar_livro(id_global)
        elif EscolhaMenu == 2:
            consultar_livro()
        elif EscolhaMenu == 3:
            remover_livro()
        elif EscolhaMenu == 4:
            sair()
        else:
            print('\nOpção inválida. Tente Novamente\n')
menu()

#Consultar Todos 

#Consultar por Id

#Consultar por Autor

#Retornar ao menu

#Encerrar Programa