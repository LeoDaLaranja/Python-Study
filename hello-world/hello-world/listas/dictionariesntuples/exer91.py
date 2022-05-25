import random as rd
from time import sleep
from operator import itemgetter
jogador = {}
ranking = list()
for c in range(1,5):

    jogador[c] = rd.randint(1,6)
for k,v in jogador.items():
    print(f'O jogador {k} tirou {v} no dado')
    sleep(1)
print()
ranking = sorted(jogador.items(), key = itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'O jogador {v[1]} ficou em {i+1}° lugar')
