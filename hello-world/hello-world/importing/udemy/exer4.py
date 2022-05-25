'''
1- Crie uma função que receba uma funçõo 
como parâmetro e retorne o valor da função 
executada 

'''


def funcao():
    return f'Função 1 em execução'

def funcao2(x):
    print(funcao())
    return f'Função 2 em execução'



print(funcao2(funcao))


'''
2 - Crie uma funação que recebe uma função2 como parâmetro e retorne
o valor da função2 executada. Faça a função1 executar duas funções que recebam um 
número diferente de argumentos

'''

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome,saudacao):
    return f'{saudacao}, {nome}'

executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao = 'Bom dia')

print(executando)
print(executando2)