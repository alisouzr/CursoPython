"""
For / Else em Python
"""

variavel = ['Aliny Souza', 'Gleice Kelly', 'Maria']

for valor in variavel:
    print(valor)
    if valor.lower().startswith('g'):
        break
else:
    print(f'Não existe G no nome')
