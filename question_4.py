#Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem inversa. 
# Imprima o vetor no final. Use listas.

def print_vet(vet: list):
    vet.reverse()
    return print(vet)

a = [2, 5, 8, 4, 1]
print_vet(a)