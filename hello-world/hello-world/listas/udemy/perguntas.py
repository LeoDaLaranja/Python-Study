from calendar import c


perguntas = {
    'Pergunta 1': {
        'Pergunta'  : 'Quanto é 2+2 ',
        'Respostas' : {
            'a' : 6,
            'b' : 8,
            'c' : 4,
        },
        'resposta_certa' : 'c',
    },
    'Pergunta 2': {
        'Pergunta': 'Com quantos paus se faz uma canoa? ',
        'Respostas' : {'a':1,'b':2,'c':'sua mãe'},
        'resposta_certa' : 'c'
    }
}
respostas_certas = 0
for pk, pv in perguntas.items():

    print(f'{pk}:  {pv["Pergunta"]}')
    
    for rk,rv in pv['Respostas'].items():
        print(f'{rk}: {rv}')
    
    r = input('Sua opcao: ')
    if r == pv['resposta_certa']:
        print('Você acertou ')
        respostas_certas +=1
    else: 
        print('Você errou')
print(f'Você acertou {respostas_certas} perguntas')