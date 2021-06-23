#Escreva uma função em Python que leia uma tupla contendo números inteiros, retorne uma lista contendo 
# somente os números ímpares e uma nova tupla contendo somente os elementos nas posições pares.
def check_numbers(vet: tuple):
    vet = list(vet)
    odd_numbers = []
    pair_numbers = []
    for i in range(0, len(vet)):
        if i % 2 == 0:
            pair_numbers.append(vet[i])
    pair_numbers = tuple(pair_numbers)    
    for i in vet:
        if i % 2 != 0:
            odd_numbers.append(i)
              
    print(f'Tupla de números nas posições pares: {pair_numbers}')
    print(f'Lista de números impares: {odd_numbers}')

a = (1, 8, 5, 9, 4, 7)
check_numbers(a)