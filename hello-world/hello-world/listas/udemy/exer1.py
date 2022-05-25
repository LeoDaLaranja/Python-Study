'''
Considerando duas lista de inteiros ou floats
(lista A e lista B) 
Some os dois valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
======================
lista_soma = [2,4,6,8]
'''
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

lista_soma = zip(lista_b, lista_a)
new_lista = []
for c,v in lista_soma:
    x = c+v
    new_lista.append(x)


print(new_lista)

lista_soma = [x+y for x,y in zip(lista_a,lista_b)]
print(lista_soma)