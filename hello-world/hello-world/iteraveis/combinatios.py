'''
Combinations, Permuatations e Product - Itertools

Combinação - Ordem não importa
Permutação - Ordem importa 
Ambos não repetem valores únicos 
Produto - Ordem importa e repete valores únicos 

'''

from itertools import combinations,permutations,product
pessoas = ['Leo','André','Eduardo','Leticia','Fabricio','Giovana']

for grupo in combinations(pessoas,2):
    #print(grupo)
    pass
for grupo in permutations(pessoas,2):
    #print(grupo)
    pass
for grupo in product(pessoas,repeat = 2):
    print(grupo)