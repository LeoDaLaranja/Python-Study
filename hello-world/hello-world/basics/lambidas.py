def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)
print(var)

a = lambda x,y: x *y #essa funcao é a mesma que a de cima

print(a(2,2))

#odernação por um valor de uma lista dentro de uma lista

lista = [
    ['P1', 13],
    ['P2', 106],
    ['P3', 1],
    ['P4', 56],
    ['P5', 19],
    ['P6', 8]
    
]
def func(item):
    return item[1]

#ou usar uma lambda

x = lambda item: item[1]
#ou até mesmo passar direto na key
lista.sort(key= lambda item: item[1])
print(lista)

#existe tbm o operador sorted 

print(sorted(lista, key = lambda i: i[1], reverse= True)) # de forma reversa só de zoas