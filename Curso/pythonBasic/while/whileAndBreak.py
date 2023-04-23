"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
""" condição = True

while condição:
    nome = input("Qual o seu nome: ")
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('acabou.') """

contador = 0

#while contador <11:
#    print(contador)
#    contador+=1

while contador <=100:
    contador +=1
    if contador ==6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o ', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('acabou.')