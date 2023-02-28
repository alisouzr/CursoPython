"""
Listas em Python
fatiamento
append, insert, pop, dek, clear, extend, +
min, max
range
"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)  # adiciona os elementos da l2 no final da l1
l2.append('b')  # adiciona o elemento b no final da l2
l2.insert(0, 'banana')  # insere no indice 0 o elemento 'banana'
l2.pop()  # elimina o último elemento da l2
del(l2[3:5])  # elimina os elementos de indice 3 à 5 da l2

print(l1)
print(l2)
print(max(l1))
print(min(l1))

l2 = list(range(0, 10))
print(l2)
