from dados import produtos,pessoas,lista



def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05,2)
    return p
nova_lista = map(lambda x: x*2, lista)
print(list(nova_lista)) #o map não retorna uma list, mas sim um iterador
precos = map(lambda p: p['preco'],produtos)#o primeiro parametro é sempre uma expressão
precos_aumentados= map(aumenta_preco,produtos)

