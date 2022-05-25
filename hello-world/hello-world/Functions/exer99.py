from time import sleep
def maior(*x):
    '''
    -> Verifica o maior número de n números passados
    param n: os valores passados
    '''
    cont = maior = 0
    print('Analisando os valores passados... ')
    for v in x:
        print(f'{v} ', end='', flush = True)
        sleep(0.3)
        if cont == 0:
            maior = v
        else:
            if v>maior:
                maior = v
        cont +=1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(1,2,3,4,5,6)
maior(9,33,45,67,34)