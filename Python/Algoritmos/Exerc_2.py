PRECOS = {
    ('ac', 'p'): 11,
    ('ac', 'm'): 16,
    ('ac', 'g'): 20,
    ('cp', 'p'): 9,
    ('cp', 'm'): 14,
    ('cp', 'g'): 18,
}

NOMES_SABOR = {'ac': 'Açaí', 'cp': 'Cupuaçu'}
NOMES_TAMANHO = {'p': 'Pequeno', 'm': 'Médio', 'g': 'Grande'}


def preco_unitario(sabor, tamanho):
    """Retorna o preço unitário para um sabor e tamanho, ou None se inválido."""
    sabor = sabor.lower()
    tamanho = tamanho.lower()
    return PRECOS.get((sabor, tamanho))


def calcular_valor_pedido(sabor, tamanho, quantidade):
    """Calcula o valor de um pedido. Levanta ValueError se sabor/tamanho for inválido."""
    preco = preco_unitario(sabor, tamanho)
    if preco is None:
        raise ValueError(f'Combinação inválida: sabor={sabor}, tamanho={tamanho}')
    return preco * quantidade


def descricao_pedido(sabor, tamanho):
    """Retorna a descrição legível do pedido, ex: 'Açaí Pequeno'."""
    sabor_nome = NOMES_SABOR.get(sabor.lower())
    tamanho_nome = NOMES_TAMANHO.get(tamanho.lower())
    if sabor_nome is None or tamanho_nome is None:
        raise ValueError(f'Combinação inválida: sabor={sabor}, tamanho={tamanho}')
    return f'{sabor_nome} {tamanho_nome}'


def escolher_sabor():
    while True:
        sabor = input('Selecione o sabor desejado (AC/CP): ').strip().lower()
        if sabor == 'ac':
            print('\nP - R$ 11')
            print('M - R$ 16')
            print('G - R$ 20\n')
            return sabor
        elif sabor == 'cp':
            print('\nP - R$ 9')
            print('M - R$ 14')
            print('G - R$ 18\n')
            return sabor
        else:
            print('\nSabor inválido. Digite novamente\n')


def escolher_tamanho(sabor):
    while True:
        tamanho = input('Selecione o tamanho desejado (P/M/G): ').strip().lower()
        if tamanho in ('p', 'm', 'g'):
            print(f'\n{descricao_pedido(sabor, tamanho).upper()}\n')
            return tamanho
        else:
            print('\nTamanho inválido. Digite novamente\n')


def main():
    print('\nBem-vindo a Loja de Gelados do João Paulo Ferreira\n')
    menu = '-' * 10 + 'MENU' + '-' * 15
    print(menu)
    print('\n' + '-' * 2 + '[AC]-Açaí' + '-' * 18)
    print('-' * 2 + '[CP]-Cupuaçu' + '-' * 15 + '\n')

    total = 0

    while True:
        sabor = escolher_sabor()
        tamanho = escolher_tamanho(sabor)
        qtd = int(input('Selecione a quantidade desejada: '))

        total += calcular_valor_pedido(sabor, tamanho, qtd)
        print(f'\nTotal parcial: R$ {total:,.2f}')

        acrescentar = input('Deseja algo mais? (s/n): ').strip().lower()
        if acrescentar != 's':
            break

    print('\nValor total a pagar: R$ {:,.2f}'.format(total))


if __name__ == "__main__":
    main()