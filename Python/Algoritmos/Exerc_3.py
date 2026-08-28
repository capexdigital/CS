# Exerc_3.py

PRECOS = {
    1: 1.10,  # Digitalização
    2: 1.00,  # Impressão Colorida
    3: 0.40,  # Impressão preto e branco
    4: 0.20,  # Fotocópia
}

ADICIONAIS = {
    0: 0,
    1: 15,
    2: 40,
}


def calcular_valor_base(escolha_servico, num_pag):
    """Calcula o valor base do serviço, sem desconto nem adicional."""
    if escolha_servico not in PRECOS:
        raise ValueError(f'Serviço inválido: {escolha_servico}')
    return PRECOS[escolha_servico] * num_pag


def aplicar_desconto(total, num_pag):
    """Aplica desconto progressivo baseado no número de páginas."""
    if num_pag < 20:
        return total
    elif num_pag < 200:
        return total * 0.85
    elif num_pag < 2000:
        return total * 0.80
    elif num_pag < 20000:
        return total * 0.75
    return total


def aplicar_adicional(total, adicional):
    """Adiciona o valor do encadernamento escolhido."""
    if adicional not in ADICIONAIS:
        raise ValueError(f'Adicional inválido: {adicional}')
    return total + ADICIONAIS[adicional]


def calcular_total(escolha_servico, num_pag, adicional):
    """Calcula o valor final: base -> desconto -> adicional."""
    total = calcular_valor_base(escolha_servico, num_pag)
    total = aplicar_desconto(total, num_pag)
    total = aplicar_adicional(total, adicional)
    return total


def ler_escolha_servico():
    while True:
        escolha = int(input('Escolha o serviço desejado: '))
        if escolha in PRECOS:
            return escolha
        print('\nOpção Inválida. Selecione de 1 a 4\n')


def ler_num_paginas():
    while True:
        num_pag = int(input('Escolha o número de páginas: '))
        if num_pag > 10000:
            print('\nNão aceitamos tantas páginas de uma vez. Por favor, digite novamente\n')
        else:
            return num_pag


def ler_adicional():
    print('\nEscolha seu adicional\n')
    print('0 - Sem Adicionais')
    print('1 - Encadernação Simples - R$ 15.00')
    print('2 - Encadernação Capa Dura - R$ 40.00')
    while True:
        adicional = int(input('\nDeseja acrescentar algum adicional?: '))
        if adicional in ADICIONAIS:
            return adicional
        print('\nOpção inválida. Escolha 0, 1 ou 2.')


def main():
    print('\nBem-vindo a Copiadora JPF\n')
    print('1 - Digitalização')
    print('2 - Impressão Colorida')
    print('3 - Impressão Preto e Branco')
    print('4 - Fotocópia\n')

    escolha_servico = ler_escolha_servico()
    num_pag = ler_num_paginas()

    if num_pag < 20:
        print('\nDesconto apenas para pedidos acima de 20 páginas.\n')
    elif num_pag < 200:
        print('Desconto de 15% aplicado.')
    elif num_pag < 2000:
        print('Desconto de 20% aplicado.')
    elif num_pag < 20000:
        print('Desconto de 25% aplicado.')

    adicional = ler_adicional()
    total = calcular_total(escolha_servico, num_pag, adicional)

    print(f'\nTotal a pagar: R$ {total:.2f}')


if __name__ == "__main__":
    main()