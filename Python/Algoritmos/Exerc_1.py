print('Bem-vindo a Loja do João Paulo Ferreira')

# Loop para input de valor
while True:
    print('\n * Valor mínimo para desconto deve ser maior do que R$ 2500.\n')
    valor = float(input('Valor do produto R$:'))
    break

quantidade = int(input('Filtrar quantidade: '))

# Calcular total sem desconto
total_sem_desconto = valor * quantidade

# Função para aplicar desconto
def desconto(valor):
    if valor <= 2500:
        return valor 
    elif 2500 <= valor < 6000:
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
    

# Aplica desconto no valor armazenando-o em outra variável
valor_com_desconto = desconto(valor)

# Calcular total com desconto
total_com_desconto = valor_com_desconto * quantidade

print(f'Total sem desconto: R$ {total_sem_desconto}')
print(f'Total com desconto: R$ {total_com_desconto}')
