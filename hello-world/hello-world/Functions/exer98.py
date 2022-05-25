def contador(i,f,p):
    print('')
    print('*'*40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    cont = i
    if p<0:
        p*=-1
    if p==0:
        p = 1
    if i<f:
        while cont<=f:
            print(f'{cont} | ',end='', flush= True)
            cont+=p
        print('')
        print('*'*40)
    else:
        cont = i 
        while cont >=f:
            #sem o flush ele não funciona, isso foi uma função lançada a pouco tempo atrás 
            print(f'{cont} | ',end='', flush= True)
            cont-=p
        print('')
        print('*'*40)
    

contador(1,10,1)
contador(1,10,2)
print('')
print('-'*20)
print('Contagem personalizada')
print('-'*20)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('De quanto em quanto? '))
contador(i,f,p)
