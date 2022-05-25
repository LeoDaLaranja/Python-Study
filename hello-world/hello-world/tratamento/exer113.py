def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n
def leiaFloat(msg):
    while True:
        try: 
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        else:
            return n

num = leiaInt('Digite um valor: ')
num2 = leiaFloat('Digite um valor real: ')
print(f'O valor digitado foi {num} e é um inteiro, {num2} é um número real ') 