from uteis import moeda as md

m = float(input('Informe a quantia de dinheiro: '))
t = str(input('Deseja converter essa moeda? S/N')).upper()
if t == 'N':
    t = False
else:
    t = True

print(f'O valor do dinheiro dobrado {md.dobra(m,t)}')
print(f'O valor da metade do dinheiro {md.metade(m,t)}')
print(f'O valor do dinheiro aumentado é {md.aumenta(m,t)}')