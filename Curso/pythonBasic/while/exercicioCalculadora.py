""" Calculadora com while"""

entrada = 'sim'

operadores = ['+', '-', '/', '*']

while entrada == ('sim' or 's'):
    number_one = input("Digite um número: ")
    number_two = input("Digite outro número: ")

    numeros_validos = None
    number_one_float = 0
    number_two_float = 0

    try:
        number_one_float = float(number_one)
        number_two_float = float(number_two)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operador = input("Digite um operador: ")
    if operador in operadores:
        resultado = f'{number_one}{operador}{number_two}'
        print(f'{number_one}{operador}{number_two} = {eval(resultado)}')
    else:
        print('Operador digitado inválido.')
        continue
    entrada = input("\nDeseja continuar ? [s]im: ").lower()