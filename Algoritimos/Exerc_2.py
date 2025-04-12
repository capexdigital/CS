# GELADOS JPF
print('Bem-vindo a Loja de Gelados do João Paulo Ferreira\n')
print('--- MENU ---')
print('AC - Açai')
print('CP - Cupuaçu\n')

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
        print('\nSabor Inválido. Tente novamente\n')
        
# implementar if/else com cada uma das combinações de sabor e tamanho
while True:
    tamanho = input("Selecione o tamanho desejado:")
    if tamanho in ['p', 'P'] and sabor in ['AC', 'ac']:
        print('\nAÇAI PEQUENO\n')
    elif tamanho in ['p', 'P'] and sabor in ['CP', 'cp']:
        print('\nCUPUAÇU PEQUENO\n')
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
    if tamanho in ['p', 'P'] and sabor in ['AC', 'ac']:
        total = total + qtd * 11
        print(f'Total R$ {total}')
    break


