""" Calculadora com while"""

entrada = 'sim'

operadores = ['+', '-', '/', '*']

while entrada == ('sim' or 's'):
    number_one = int(input("Digite um número inteiro: "))
    number_two = int(input("Digite outro número inteiro: "))
    operador = input("Digite um operador: ")
    if operador in operadores:
        resultado = f'{number_one}{operador}{number_two}'
        print(f'{number_one}{operador}{number_two} = {eval(resultado)}')
    entrada = input("\nDeseja continuar ? [s]im: ").lower()