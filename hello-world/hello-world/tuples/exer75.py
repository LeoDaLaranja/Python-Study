#Ler quatro valores pelo teclado e guardar em uma tupla 
n = (int(input('Informe um número ')),
     int(input('Informe outro número ')),
     int(input('Informe outro número ')),
     int(input('Informe o último número '))
    )
print(f'Você informou os seguintes números {n}')
if 3 in n:
    print(f'O número nove apareceu {n.count(9)} vezes')
else:
    print('Não foi informando nenhum valor correspondente a 3')
print(f'O valor 3 apareceu na {n.index(3)+1}° posição')
p = 0
for c in n:
    if c %2 == 0:
        p+=1
print(f'A quantidade de números pares é {p}')