money = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    qtde = int(money/nota)
    print(f'{qtde} nota(s) de R$ {nota:.2f}')
    money -= qtde*nota

print('MOEDAS:')
for moeda in moedas:
    money = round(money, 2)
    qtde_moeda = int(money/moeda)
    print(f'{qtde_moeda} moeda(s) de R$ {moeda:.2f}')
    money -= qtde_moeda*moeda
