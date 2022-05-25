from functools import reduce
from dados import pessoas,produtos,lista

soma_lista = reduce(lambda ac,i : i+ac, lista, 0 ) #lambda recebe um acumulador {ac} e um item {i}, o parametro e o início
print(soma_lista)

soma_preco = reduce(lambda ac,i : i['preco']+ac, produtos,0)
print(f'média de preço: {round(soma_preco/len(produtos),2)}')