num = input("Digite um número: ")

if num.isnumeric():
    if int(num) % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
else:
    print('Número não é um inteiro')
