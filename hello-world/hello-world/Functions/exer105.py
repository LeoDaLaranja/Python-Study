def notas(l):
    #Retorna um dict 
    '''
    - Quantidade de notas
    - A maior nota 
    - A média da turma
    - A situação
    '''
    turma = dict()
    media = (sum(l)/len(l))
    turma['media'] = round(media,2)
    maior = max(l)
    turma['maior nota']  = maior
    quant = len(l)
    turma['quantidade de notas'] = quant
    if media>6.0:
        turma['situação'] = 'Aprovada'
    elif 5.0>= media <6.0:
        turma['situação'] = 'Recuperação'
    else:
        turma['situação'] = 'Reprovada' 
    return print(turma)


lista_nota  = list()
while True:
    n = float(input('Nota do aluno: '))
    lista_nota.append(n)
    op = input('Deseja continuar? ').upper()
    if op == 'N':
        break
notas(lista_nota)