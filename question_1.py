#Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros, 
# (n1, n2, n3) e os imprima em ordem crescente.
def print_tuple(tup: tuple):
    ordered_list = list(tup)
    ordered_list.sort()
    tup = tuple(ordered_list)
    print(tup)
    

a = (3, 0, 2)   
print_tuple(a)
    