'''
Da mesma forma que é possivel criar vários except, também é possivel criar vários try
Não sei se é uma forma muito boa de criar um código 
'''

try:
    a = int(input('Número: '))
    b = int(input("Número: "))
    r = a/b
except ZeroDivisionError:
    print('O usúario tentou realizar uma divisão por zero')
except (ValueError, TypeError):
    print('Tivemos um probnelma com os tipos de dados que você digitou')
except KeyboardInterrupt:
    print('O usúario preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {round(r,2)}')
finally:
    #acontece independente se deu erro ou não
    print('Volte sempre! muito obrigao!') 