"""
Operador Ternário
"""

logged_user = False

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Uusário precisa logar.'

mensagem = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg)
print(mensagem)
