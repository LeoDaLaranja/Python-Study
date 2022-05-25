try:
    a = int(input('Número: '))
    b = int(input("Número: "))
    r = a/b
except Exception as e:
    print('Infelizmente tivemos um problema', e.__class__)
    #essas duas abaixo são opcionais
    # um mesmo try pode ter vários except 
except (ValueError, TypeError):
    print('Tivemos um probnelma com os tupos de dados que você digitou')
else:
    print(f'O resultado é {round(r,2)}')
finally:
    #acontece independente se deu erro ou não
    print('Volte sempre! muito obrigao!') 