"""
Iterando strings com while
"""
#       012345678910
nome = 'Aliny Souza' # Iteráveis

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])
nova_string = ''
cont =0

print('*' + "*".join(nome))

while cont< len(nome):
    nova_string+= f'*{nome[cont]}'
    cont+=1
print(nova_string)
