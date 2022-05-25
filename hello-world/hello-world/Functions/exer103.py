#programa que verifica apenas integers
def verInt(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor
    
x = verInt('Verifica o num: ')
print(f'Você acabou de digitar o número {x}')

