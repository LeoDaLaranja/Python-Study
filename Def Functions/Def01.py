"""
Funções- Def em python(Part 1)

"""
nome = 'Leo'
msg = 'Olá'
def funcao(msg):
    print('A sua mensagem é:', msg)

funcao('Voltando a programar depois de 3 meses parado')

def funcao1(msg = 'Olá',nome = 'usuário' ):
    print(msg, nome)

funcao1(msg = 'Olá',nome = 'Leo')

def funcaoComRetorno(msg = 'Olá',nome ='Jhow'):
    nome_replace = nome.replace('e','3')
    msg_replace = msg.replace('a','4')
    return f'{msg_replace} {nome_replace}'

variavel = funcaoComRetorno(msg,nome)
print(variavel)


