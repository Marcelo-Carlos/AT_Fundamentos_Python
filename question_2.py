#Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive.
# O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.
proceed = 's'
pair_numbers = 0

while proceed == 's':
    number = (int(input('Digite um numero inteiro: ')))
    if number < 1:
        print('Favor informar um número >= 1')
    elif number % 2 == 0:
        pair_numbers += number
    proceed = input('Deseja continuar? [S - Sim / N - Não] ').lower()
    
print(f'A soma dos números pares foi: {pair_numbers}')
    