l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]

print(ex1) # aqui ele simplesmente vai printar os mesmos valores de l1
print('')
print('')
ex2 = [v * 2 for v in l1] # aqui ele multiplica todos os valores de l1
ex3 = [(v,v2) for v in l1 for v2 in range(3)] #cria uma tupla de coordenadas
print(ex3)

print()

l2 = ['Luiz', 'Mauro', 'Maria']

ex4 = [v.replace('a','@').upper() for v in l2] # verifica se valores 'a' estão contidos e transforma em @

print(ex4)

tupla = (
    ('chave','valor'),
    ('chave2','valor2'),
)
ex5 = [(v,c) for c,v in tupla ] #inverte as posiçõess
print()
print(ex5)

l3 = list(range(100))
print()
ex6 = [v for v in l3 if v%3==0 if v % 8 == 0  ]# apenas números que satisfazem o if
print(ex6)


ex7 = [v if v% 3 == 0 else 0 for v in l3]
print(ex7)