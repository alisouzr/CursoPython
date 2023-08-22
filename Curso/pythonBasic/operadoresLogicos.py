"""
Operadores Lógicos
and, or, not
in e not in
"""
a = 2
b = 3

nome = 'Aliny Souza'

if 'y' in nome:
    print(nome)

if 'e' not in nome:
    print(nome)

print(20 >= 10 and 10 <= 20)
print(20 <= 10 or 10 <= 20)

if not a > b:
    print('não é verdadeiro')
