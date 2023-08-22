import os

palavra_secreta = 'amor'
digitadas = []
chance = 3

while True:

    if chance <= 0:
        print("VOCÊ PERDER!")
        break

    letra_user = input("Digite uma letra: ")

    if len(letra_user) > 1:
        print("Digite apenas uma letra.")
        continue

    digitadas.append(letra_user)

    if letra_user in palavra_secreta:
        print(f'A letra {letra_user} está na palavra secreta.')
    else:
        print(f'AFFSS aletra {letra_user} não está na palavra secreta.')

    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == palavra_secreta:
        os.system('clear')
        print(f'Parabéns!! a palavra secreta era {palavra_secreta}')
        break
    else:
        print(f' A palavra está assim : {secreto_temporario}')

    if letra_user not in palavra_secreta:
        chance -= 1

    print(f'Você ainda tem {chance} chances.')
