import random as rd
from time import sleep
def somaPar(l):
    soma = 0
    print(f'Analisando os valores passados... ')
    for x in range(len(l)):
        print(f'{l[x]} ',end='', flush=True)
        sleep(0.3)
        if l[x]%2==0:
            soma += l[x]
        
    print(f'A sua soma é {soma}')

def sorteia(l):
    for i in range(1,5):
        l.append(rd.randint(1,100))
    somaPar(l)


l = []

sorteia(l)