from dados import produtos,pessoas,lista

#Serve para filtrar 

#as vezez você consegue usar apenas um list comprehension
#mesmo caso do maps, um LC já resolve em alguns casos
def filtro(produto):
    if produto['preco']>50:
        return produto
nova_lista = [x for x in lista if x>5]
nova_lista_filter = filter(lambda x: x>5, lista)
print('Usando LC',list(nova_lista))
print('Usando Filter',list(nova_lista_filter))

nova_lista = filter(lambda p:p['preco']>25, produtos)
nova_lista_funcao = filter(filtro, produtos)
for produto in nova_lista:
    print(produto)
print('Filter com função para filtrar')
for produto in nova_lista_funcao:
    print(produto)

def maior_idade(pessoa):
    if pessoa['idade'] > 18:
        return True

pessoas  = filter(maior_idade, pessoas)
print()
print('Pessoas maiores de idade')
for pessoa in pessoas:
    print(pessoa)
    