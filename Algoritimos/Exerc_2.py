# GELADOS JPF
print('Bem-vindo a Loja de Gelados do João Paulo Ferreira')
print('AC - Açai')
print('CP - Cupuaçu')

# Loop restringindo opções de escolha do usuário
while True:
    sabor = str(input('Selecione o sabor desejado:')) 
    if sabor in ['AC', 'ac']:
        print('P - R$ 11')
        print('M - R$ 16')
        print('G - R$ 20')
    
    elif sabor in ['CP', 'cp']:
        print('P - R$ 9')
        print('M - R$ 14')
        print('G - R$ 18')
        break
    else:
        print('Sabor Inválido. Tente novamente')
        
# implementar if/else com cada uma das combinações de sabor e tamanho
while True:
    tamanho = str(input('Selecione o tamanho desejado:'))
    if tamanho in ['p', 'P'] and sabor in ['AC', 'ac']:
        print('AÇAI PEQUENO')
    elif tamanho in ['p', 'P'] and sabor in ['CP', 'cp']:
        print('CUPUAÇU PEQUENO')
    elif tamanho in ['m', 'M'] and sabor in ['AC', 'ac']:
        print('AÇAI MÉDIO')
    elif tamanho in ['m', 'M'] and sabor in ['CP', 'cp']:
        print('CUPUAÇU MÉDIO')
    elif tamanho in ['g', 'G'] and sabor in ['AC', 'ac']:
        print('AÇAI GRANDE')
    elif tamanho in ['g', 'G'] and sabor in ['CP', 'cp']:
        print('CUPUAÇU GRANDE')        
        break
    else:
        print('Tamanho inválido')

# acumulador para somar valores dos pedidos
while True:
    qtd = int(input('Selecione a quantidade desejada:'))
    print(qtd)
    break


