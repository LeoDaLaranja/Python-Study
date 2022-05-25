def fatorial(num = 1,show = False):
    '''
    Função calcula o fatorial 
    n = número para qual será calculado o mesmo
    '''
    f = 1
    for c in range(num, 0,-1):
        if show:
            print(f'{c} x ', end='')
        f*=c
    return f 
n = int(input('Digite um número: '))

print(f'O fatorial de {n} é igual a {fatorial(n, show = True)}')

