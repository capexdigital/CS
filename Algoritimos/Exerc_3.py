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

for i in range (1):
    escolha_servico = int(input('Escolha o serviço desejado:'))
    if escolha_servico == 1:
        num_pag = (int(input('Escolha o número de páginas:')))
        total = DIG * num_pag
        print('\nTotal a pagar R$: ''{:,.2f}'.format(total))
    elif escolha_servico == 2:
        num_pag = (int(input('Escolha o número de páginas:')))
        total = ICO * num_pag
        print('\nTotal a pagar R$: ''{:,.2f}'.format(total))
    elif escolha_servico == 3:
        num_pag = (int(input('Escolha o número de páginas:')))
        total = IPB * num_pag
        print('\nTotal a pagar R$: ''{:,.2f}'.format(total))
    elif escolha_servico == 4:
        num_pag = (int(input('Escolha o número de páginas:')))
        print(FOT)
    elif num_pag > 10000:  # type: ignore
        print('\nNão aceitamos tantas páginas de uma vez. Por favor, digite novamente\n')
    else:
        print('\nOpção Inválida. Selecione de 1 a 4\n')
        
    break


def desconto():
    if num_pag < 20:
        print('Desconto apenas para pedidos acima de 20 páginas.')
    if num_pag >= 20 and num_pag < 200:
        print ('Desconto de 15% aplicado.')
        return num_pag * 0.85
    elif num_pag >= 200 and num_pag < 2000:
        print ('Desconto de 20% aplicado.')
        return num_pag * 0.80
    elif num_pag >= 2000 and num_pag < 20000:
        print ('Desconto de 25% aplicado.')
        return num_pag * 0.75
    else: num_pag > 20000
    print ('Desconto de 15% aplicado.')

# Tabela de adicionais
def extra():
    print('Escolha seu adicional')
    print('0 - Sem Adicionais')
    print('1 - Encadernação Simples')
    print('2 - Encadernação Capa Dura')

    #adc0 = num_pag + 0 # Sem adicionais
    #adc1 = num_pag + 15 # Encadernação Simples 
    #adc2 = num_pag + 40 # Encadernação Capa Dura

# Calcular valor final
#total = (servico * num_pag) + taxa


