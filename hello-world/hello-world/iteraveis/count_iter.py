'''
count - Itertools
'''


from itertools import count

contador = count() #sem passar parametro o count é infinito

contador = count(start = 5, step = 0.1)

for valor in contador:
    print(round(valor,2))
    if valor >=10.0:
        break
contador = count()
#essa maravilha tambem faz isso, cria indices
lista = ['Luiz','João','Maria']
lista = zip(contador, lista)
print(list(lista))