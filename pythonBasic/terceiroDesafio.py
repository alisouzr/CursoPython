hora = int(input('Digite a hora atual: '))

if hora >= 0 and hora <= 11:
    print('Bom dia')
elif hora >= 12 and hora <= 17:
    print('Boa Tarde')
else:
    print('Boa noite')
