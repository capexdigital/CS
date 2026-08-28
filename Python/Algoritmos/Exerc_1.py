def desconto(valor):
    """Aplica desconto progressivo com base no valor do produto."""
    if valor <= 2500:
        return valor
    elif 2500 < valor < 6000:
        print('Desconto de 4% aplicado.')
        return valor * 0.96
    elif 6000 <= valor < 10000:
        print('Desconto de 7% aplicado.')
        return valor * 0.93
    elif valor >= 10000:
        print('Desconto de 11% aplicado.')
        return valor * 0.89
    else:
        print('Valor inválido')
        return valor


def total_sem_desconto(valor, quantidade):
    """Calcula o total sem aplicar nenhum desconto."""
    return valor * quantidade


def total_com_desconto(valor, quantidade):
    """Calcula o total aplicando o desconto sobre o valor unitário."""
    valor_com_desconto = desconto(valor)
    return valor_com_desconto * quantidade


if __name__ == "__main__":
    print('Bem-vindo a Loja do João Paulo Ferreira')

    print('\n * Valor mínimo para desconto deve ser maior do que R$ 2500.\n')
    valor = float(input('Valor do produto R$:'))
    quantidade = int(input('Filtrar quantidade: '))

    total_sem = total_sem_desconto(valor, quantidade)
    total_com = total_com_desconto(valor, quantidade)

    print(f'Total sem desconto: R$ {total_sem}')
    print(f'Total com desconto: R$ {total_com}')