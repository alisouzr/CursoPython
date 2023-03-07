"""
Split, Jpoin, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
"""

string = 'O Brasil é o país do futebol, o Brasil é HEXA.'
lista = string.split(' ')  # split
string2 = ' '.join(lista)  # join

lista2 = ['Kelly', 'Aliny', 'Gleice', 1, 2, 3, 4, 5, 6, 7, 8]

for indice, valor in enumerate(lista2):  # enumerate
    print(indice, valor)

n1, n2, n3, *outra_lista = lista2  # desempacotamento
print(outra_lista)


print(string)
print(lista)
print(string2)
