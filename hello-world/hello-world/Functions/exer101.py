def voto(ano = 2000):
    from datetime import date
    atual = date.today().year
    idade = atual -ano
    if idade < 16:
        return print(f'Com {idade} anos: Não vota')
    elif 16<=idade <18 or idade > 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        return print(f'Com {idade} anos : O voto é OBRIGATÓRIO')
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
