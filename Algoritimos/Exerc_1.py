#EMPRESA X
print('Bem-vindo a Loja do João Paulo Ferreira')

# Loop para input de valor
while True:
    valor = float(input('Valor do produto R$: '))
    if valor > 2500:
        break
    print('ERROR: Valor mínimo para desconto deve ser maior do que R$ 2500.')

quantidade = int(input('Filtrar quantidade: '))

# Função para aplicar desconto
def desconto(valor):
    if valor < 6000:
        print ('Desconto de 4% aplicado.')
        return valor * 0.96
    elif valor < 10000:
        print ('Desconto de 7% aplicado.')
        return valor * 0.93
    else:
        print ('Desconto de 11% aplicado.')
        return valor * 0.89

# Aplico o desconto no valor armazenando em outra variável
valor_com_desconto = desconto(valor)

# Calcular totais
total_sem_desconto = valor * quantidade
total_com_desconto = valor_com_desconto * quantidade

print(f'Total sem desconto: R$ {total_sem_desconto}')
print(f'Total com desconto: R$ {total_com_desconto}')