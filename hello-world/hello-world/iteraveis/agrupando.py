from itertools import groupby, tee


alunos = [
    {'nome':'Leo','nota':'A',},
    {'nome':'Guilherme','nota':'A',},
    {'nome':'Giovana','nota':'A',},
    {'nome':'Matheus','nota':'A-',},
    {'nome':'Jhow','nota':'D',},
    {'nome':'Ana','nota':'C',},
    {'nome':'Marcia','nota':'D',},
    {'nome':'Rafael','nota':'B',},
    {'nome':'Du','nota':'A+',},
    {'nome':'João','nota':'C-',},

]
ordena = lambda item:item['nota']
alunos.sort(key = ordena)
alunos_agrupados = groupby(alunos,ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1,va2 = tee(valores_agrupados) #faz uma cópia dos valores em duas variaveis, possibilitando o uso mais de uma vez ao invés de fazre outro for
    print(f'Agrupamento:{agrupamento}')
    
    print('Alunos: ')
    for aluno in va1:
       print(aluno) 
       
        
    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()

#agora colocando a quantidade de alunos por agrupamento