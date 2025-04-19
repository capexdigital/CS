print('\n')
print('Bem-vindo a Loja de Gelados do João Paulo Ferreira\n')
menu = '-' * 10 + 'MENU' + '-' * 15
print(menu)
print('\n')
sabor_1 = '-' * 2 + '[AC]-Açaí' + '-' * 18
print(sabor_1)
sabor_2 =  '-' * 2 + '[CP]-Cupuaçu' + '-' * 15
print(sabor_2)
print('\n')

total = 0


# Loop restringindo opções de escolha do usuário
while True:
    sabor = input("Selecione o sabor desejado:")
    if (sabor == 'AC' or sabor == 'ac'):
        print('\nP - R$ 11')
        print('M - R$ 16')
        print('G - R$ 20\n')
        break
    
    elif (sabor == 'CP' or sabor == 'cp'):
        print('\nP - R$ 9')
        print('M - R$ 14')
        print('G - R$ 18\n')
        break
    else:
        print('\nSabor Inválido. Digite novamente\n')
        
# implementar if/else com cada uma das combinações de sabor e tamanho
while True:
    tamanho = input("Selecione o tamanho desejado:")
    if tamanho in ['p', 'P'] and sabor in ['AC', 'ac']:
        print('\nAÇAI PEQUENO\n')
    elif tamanho in ['p', 'P'] and sabor in ['CP', 'cp']:
        print('\nCUPUAÇU PEQUENO\n')
    elif tamanho in ['m', 'M'] and sabor in ['AC', 'ac']:
        print('\nAÇAI MÉDIO\n')
    elif tamanho in ['m', 'M'] and sabor in ['CP', 'cp']:
        print('\nCUPUAÇU MÉDIO\n')
    elif tamanho in ['g', 'G'] and sabor in ['AC', 'ac']:
        print('\nAÇAI GRANDE\n')
    elif tamanho in ['g', 'G'] and sabor in ['CP', 'cp']:
        print('\nCUPUAÇU GRANDE\n')        
        break
    else:
        print('\nTamanho inválido. Digite novamente\n')
    break

# acumulador para somar valores dos pedidos
while True:
    qtd = int(input('Selecione a quantidade desejada:'))

    # Tabela de valores açai
    if tamanho in ['p', 'P'] and sabor in ['AC', 'ac']:
        total = total + qtd * 11
        print(f'\nTotal R$ {total}')
    elif tamanho in ['m', 'M'] and sabor in ['AC', 'ac']:
        total = total + qtd * 16
        print(f'\nTotal R$ {total}')
    elif tamanho in ['g', 'G'] and sabor in ['AC', 'ac']:
        total = total + qtd * 20
        print(f'\nTotal R$ {total}')
        
    # Tabela de valores cupuaçu
    elif tamanho in ['p', 'P'] and sabor in ['CP', 'cp']:
        total = total + qtd * 9
        print(f'\nTotal R$ {total}')
    elif tamanho in ['m', 'M'] and sabor in ['CP', 'cp']:
        total = total + qtd * 14
        print(f'\nTotal R$ {total}')
    elif tamanho in ['g', 'G'] and sabor in ['CP', 'cp']:
        total = total + qtd * 18
        print(f'\nTotal R$ {total}')
    break

while True:
    acrescentar = str(input('Deseja algo mais? (s/n):'))
    while acrescentar in ['s','n' or 'S','N']:
        if acrescentar == 's' or acrescentar == 'S':
            continue
        elif acrescentar == 'n' or acrescentar == 'N':
            print('\nValor total a pagar R$: ''{:,.2f}'.format(total))
        else:
            print('\nValor total R$: ''{:,.2f}'.format(total))
        break
    break
        