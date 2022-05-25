nome = input('Informe seu primeiro nome: ')
len_nome = len(nome)
if len_nome <= 4:
    print(f'Seu primeiro nome é curto, possui apenas {len_nome} letras')
elif len_nome > 4 and len_nome <=6:
    print(f'Seu nome é normal, possui um total de {len_nome} letras')
else:
    print(f'Seu nome é giganteee,possui {len_nome} letras')