"""
set -> retira os repetidos e cria uma lista (uma estrutura de dados que não contém elementos duplicados)
"""


def is_isogram(string):
    return len(string) == len(set(string.lower()))
    # se a quantidade de letras da string for igual à quantidade da string sem letra repetida True


print(is_isogram("aba"))
letra = "aba"
a = ""
for i in letra:
    if i == a:
        print('igual')
    a = i

print(set(letra.lower()))
