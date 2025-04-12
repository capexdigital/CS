print('Bem vindo a Livraria do Joao\n')
menu = '-' * 10 + ' MENU ' + '-' * 15
print(menu)
print('\n')
print('1 - CADASTRAR LIVRO')
print('2 - CONSULTAR LIVRO')
print('3 - REMOVER LIVRO')
print('4 - SAIR')

print('\n')

livro = []
listaLivro = []

id_global = 0

#Cadastrar Livro
def cadastrar_livro(id_global):
    for i in range(1):
        listaLivro.append(str(input('Nome:')))
        listaLivro.append(str(input('Autor:')))
        listaLivro.append(str(input('Editora:')))
        livro.append(listaLivro[:])
        id_global = id_global + 1
        livro.clear()
        print('\n')
        print(f'id - {id_global}')
        print(listaLivro)
        print(menu)
        break

# Loop para escolha de opções do menu
while True:
    EscolhaMenu = int(input("Selecione a opção desejada:"))
    if EscolhaMenu == 1:
        cadastrar_livro(id_global)
    elif EscolhaMenu == 2:
        print('2')
    break


#Consultar Livro
    #def consultar_livro():


#Consultar Todos 

#Consultar por Id

#Consultar por Autor

#Retornar ao menu

#Remover Livro

#Encerrar Programa