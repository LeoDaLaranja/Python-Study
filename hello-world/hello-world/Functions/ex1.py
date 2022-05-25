def dobra(lst):
    c = 0 
    while c<len(lst):
        lst[c] *= 2
        c+=1

def soma(a,b):
    print(f'Somando os valores {a}+{b}')
    s = a+b
    print(f'A soma foi {s}')


soma(4,6)
soma(6,7)
valores = [1,2,3,4,5,6,7]
dobra(valores)
print(valores)
