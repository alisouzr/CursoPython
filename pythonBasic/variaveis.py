nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

print("Seu nome é", nome)
print(idade, altura)
print("Seu IMC é", peso / altura**2)
