
def num_pag():
    int(input('Digite o número de páginas: '))

def escolha_servico():
    DIG = 1.10 # Digitalização
    ICO = 1 # Impressão Colorida
    IPB = 0.40 # Impressão preto e branco
    FOT = 0.20 # Fotocópia

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

# Adicionais
def adicional():
    print('Escolha seu adicional')
    print('0 - Sem Adicionais')
    print('1 - Encadernação Simples')
    print('2 - Encadernação Capa Dura')

    #adc0 = num_pag + 0 # Sem adicionais
    #adc1 = num_pag + 15 # Encadernação Simples 
    #adc2 = num_pag + 40 # Encadernação Capa Dura

num_pag()
adicional()


    


