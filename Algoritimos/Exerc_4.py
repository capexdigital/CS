print('Bem vindo a Livraria do Joao')

menu = '-' * 10 + 'MENU' + '-' * 15
print(menu)
print('\n')
print('1 - CADASTRAR LIVRO')
print('2 - CONSULTAR LIVRO')
print('\n')

listaLivro = []

id_global = 0

# Loop para escolha de opções do menu
while True:
    EscolhaMenu = int(input("Selecione a opção desejada:"))
    if EscolhaMenu == 1:
        print('1')
    elif EscolhaMenu == 2:
        print('2')
    break

#Cadastrar Livro
def cadastrar_livro(id):
    nome = str(input('Nome:'))
    autor = str(input('Nome:'))
    editora = str(input('Nome:'))



#Consultar Livro
    #def consultar_livro():


#Consultar Todos 

#Consultar por Id

#Consultar por Autor

#Retornar ao menu

#Remover Livro

#Encerrar Programa