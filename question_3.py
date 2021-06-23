#Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois 
# números inteiros, A e B, e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e 
# retornar o resultado da operação. Depois, crie um programa em Python que obtenha dois números inteiros do usuário
# e indique o resultado de AB usando a função.

def check_potency(a, b: int):
    return print(f'A potência é: {a**b}')
    
number_1 = int(input('Digite um inteiro (base): '))
number_2 = int(input('Digite um número (expoente): '))

check_potency(number_1, number_2)