"""
Funções - def em Python -  *args **kwargs (Parte 3)
"""


""" def func(*args):
    args = list(args)
    print(args)


func(10, 20, 30) """


def func(*args, **kwargs):
    print(args)
    print(kwargs)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Aliny', sobrenome='Souza')
