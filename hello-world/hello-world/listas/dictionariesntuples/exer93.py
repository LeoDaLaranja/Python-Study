jogador = dict()
info = list()
clube = list()
while True:
    jogador['nome'] = str(input('Nome: '))
    jogador['posição'] = str(input('Posição: '))
    jogador['partidas'] = int(input('Partidas jogadas: '))  
    c=0
    for x in range(0,jogador['partidas']):
        gols = int(input(f'Informe a quantidade de gols na {x+1}° partida: '))
        c = gols+c
        jogador['total de gols'] = c
    
    info.append(jogador.copy())
    
    n = input('Deseja continuar? ').upper()
    if n == 'N':
        break
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*60)
for k,v in enumerate(info):
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
print('-'*60)




