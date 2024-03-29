"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

number = input("Digite um número inteiro : ")

if number.isdigit():
      int_number = int(number)
      if int_number%2 == 0:
            print(f"O número {int_number} é par.")
      else:
            print(f"O número {int_number} é ímpar.")
else:
      print("Digite um número inteiro.")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Qual a hora? ")

if 0 <= int(hora) <= 11:
    print("Bom dia!")
elif 12 <= int(hora) <= 17 :
    print("Boa tarde!")
elif 18 <= int(hora) <= 23:
      print("Boa noite!")
else:
      print(f"Não conhheço essa hora {hora}")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome : ")

if len(nome) <= 4:
      print("Seu nome é curto")
elif 5 <= len(nome) <= 6:
      print("Seu nome é normal")
else:
      print("Seu nome é muito grande")