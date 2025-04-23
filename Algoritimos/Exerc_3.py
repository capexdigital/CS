# MENU
print('\nBem-vindo a Copiadora JPF\n')

DIG = float(1.10) # Digitalização
ICO = float(1) # Impressão Colorida
IPB = float(0.40) # Impressão preto e branco
FOT = float(0.20) # Fotocópia

print('1 - Digitalização')
print('2 - Impressão Colorida')
print('3 - Impressão Preto e Branco')
print('4 - Fotocópia\n')

# Escolha serviço
while True:
    escolha_servico = int(input('Escolha o serviço desejado:'))
    if escolha_servico in (1, 2, 3, 4):
        break
    else:
        print('\nOpção Inválida. Selecione de 1 a 4\n')

# Escolha número de páginas
while True:
    num_pag = int(input('Escolha o número de páginas:'))
    if num_pag > 10000:
        print('\nNão aceitamos tantas páginas de uma vez. Por favor, digite novamente\n')
    else:
        break

# Cálculo do valor base
if escolha_servico == 1:
    total = DIG * num_pag
elif escolha_servico == 2:
    total = ICO * num_pag
elif escolha_servico == 3:
    total = IPB * num_pag
elif escolha_servico == 4:
    total = FOT * num_pag

# Aplicar desconto
if num_pag < 20:
    print('\nDesconto apenas para pedidos acima de 20 páginas.\n')
elif 20 <= num_pag < 200:
    print('Desconto de 15% aplicado.')
    total *= 0.85
elif 200 <= num_pag < 2000:
    print('Desconto de 20% aplicado.')
    total *= 0.80
elif 2000 <= num_pag < 20000:
    print('Desconto de 25% aplicado.')
    total *= 0.75

# Adicionais
print('\nEscolha seu adicional\n')
print('0 - Sem Adicionais')
print('1 - Encadernação Simples - R$ 15.00')
print('2 - Encadernação Capa Dura - R$ 40.00')

while True:
    adicional = int(input('\nDeseja acrescentar algum adicional?:'))
    if adicional == 0:
        break
    elif adicional == 1:
        total += 15
        break
    elif adicional == 2:
        total += 40
        break
    else:
        print('Opção inválida. Escolha 0, 1 ou 2.')

# Valor final
print(f'\nTotal a pagar: R$ {total:.2f}')