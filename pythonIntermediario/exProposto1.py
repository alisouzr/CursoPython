def saudacao(saud, nome):
    print(f'{saud} {nome}')


saudacao('Olá', 'Aliny')


def soma(n1, n2, n3):
    print(n1+n2+n3)


soma(2, 5, 8)


def percentual(valor, perc):
    return valor + (perc/100*valor)


print(percentual(50, 10))


def fizzBuzz(som):
    if som % 5 == 0 and som % 3 == 0:
        return 'FizzBuzz'
    if som % 5 == 0:
        return 'buzz'
    if som % 3 == 0:
        return 'fizz'
    return som


print(fizzBuzz(15))
