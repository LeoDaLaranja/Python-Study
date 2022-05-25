'''
Zip - Unindo iteráveis 
Zip_longest - Itertools

'''
from itertools import zip_longest,count

indice = count()
cidades = ['São Paulo', 'Belo Horizontes','Salvador','Monte Belo']

estados = ['SP', 'MG','BA']

cidades_estados = zip(cidades, estados)

#print(next(cidades_estados))# primeiro valor, infelizemnte não é a melhor pratica
#melhor forma
for valor in cidades_estados:
    print(valor, end = '')

print()
#ao usar um print(cidades_estados) é retornado um objeto, já que isso é um gerador 
print(cidades_estados)
#para retornar o valor completo ->
# print(list(cidades_estados))

cidades_estados = zip(
    indice,
    estados,
    cidades)
est= 'SP'

for indice,estado, cidade in cidades_estados:
    print(indice, estado, cidade)
    if est in estado:
        print(f'indice: {indice}| ciadade: {cidade}')


#também é possivel retornar um dicionario 
print(dict(cidades_estados))
