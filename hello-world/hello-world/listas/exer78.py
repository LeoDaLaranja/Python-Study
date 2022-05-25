l = []
for i in range(0,4):
    n = int(input('Informe um número '))
    l.append(n)

for i in range(len(l)):
    if l[i] == max(l):
        print(f'O maior valor é {max(l)} e está na posição {i+1}')
    elif l[i] == min(l):
        print(f'O menor valor é {min(l)} e está na posição {i+1}')

