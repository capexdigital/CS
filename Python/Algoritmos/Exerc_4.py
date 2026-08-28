# Exerc_4.py

lista_livros = []
_proximo_id = [1]  # usa lista para evitar problema de escopo com variável mutável


def cadastrar_livro(nome, autor, editora):
    """Cria e adiciona um livro à lista. Retorna o livro criado."""
    livro = {
        'id': _proximo_id[0],
        'nome': nome,
        'autor': autor,
        'editora': editora,
    }
    lista_livros.append(livro)
    _proximo_id[0] += 1
    return livro


def buscar_por_id(id_busca):
    """Retorna o livro com o ID informado, ou None se não encontrado."""
    for livro in lista_livros:
        if livro['id'] == id_busca:
            return livro
    return None


def buscar_por_autor(autor_busca):
    """Retorna a lista de livros cujo autor contém o texto buscado."""
    return [livro for livro in lista_livros if autor_busca.lower() in livro['autor'].lower()]


def remover_livro(id_remover):
    """Remove o livro com o ID informado. Retorna True se removido, False caso contrário."""
    for i, livro in enumerate(lista_livros):
        if livro['id'] == id_remover:
            lista_livros.pop(i)
            return True
    return False


def resetar():
    """Limpa a lista de livros e o contador de ID (útil para testes)."""
    lista_livros.clear()
    _proximo_id[0] = 1


# --- Funções interativas (não testadas diretamente) ---

def fluxo_cadastrar():
    while True:
        nome = input('Nome: ')
        autor = input('Autor: ')
        editora = input('Editora: ')
        livro = cadastrar_livro(nome, autor, editora)
        print(f"\nLivro cadastrado com ID {livro['id']}!")

        resposta = input('Cadastrar outro? [S/N]: ').upper()
        if resposta == 'S':
            continue
        elif resposta == 'N':
            print(lista_livros)
            return
        else:
            print('\nERROR! Resposta inválida. Tente novamente.')


def fluxo_consultar():
    print("\n1 - Todos")
    print("2 - Por ID")
    print("3 - Por Autor")
    opcao = int(input("Selecione a opção desejada: "))

    if opcao == 1:
        for livro in lista_livros:
            print(f"ID: {livro['id']} | {livro['nome']}")

    elif opcao == 2:
        id_busca = int(input("ID: "))
        livro = buscar_por_id(id_busca)
        if livro:
            print(f"\nNome: {livro['nome']}\nAutor: {livro['autor']}\nEditora: {livro['editora']}")
        else:
            print("\nLivro não encontrado!")

    elif opcao == 3:
        autor = input("Autor: ")
        encontrados = buscar_por_autor(autor)
        if encontrados:
            for livro in encontrados:
                print(f"ID: {livro['id']} | Nome: {livro['nome']}")
        else:
            print("\nNenhum livro encontrado para esse autor!")


def fluxo_remover():
    id_remover = int(input("ID para remover: "))
    if remover_livro(id_remover):
        print("\nLivro removido!")
    else:
        print("ID não encontrado!")


def menu():
    while True:
        print("\nBem-vindo a livraria JP")
        print("\n" + "-" * 30)
        print("1 - Cadastrar")
        print("2 - Consultar")
        print("3 - Remover")
        print("4 - Sair\n")
        opcao = input("Opção: ")

        if opcao == '1':
            fluxo_cadastrar()
        elif opcao == '2':
            fluxo_consultar()
        elif opcao == '3':
            fluxo_remover()
        elif opcao == '4':
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()