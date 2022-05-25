pessoa = ()

grupo = ()
mai = men = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(grupo) == 0:
        mai = men = pessoa[1]
    else:
        if grupo[1]>mai:
            mai = grupo[1]
        if grupo[1]<men:
            men = grupo[1]
    


    grupo.append(pessoa[:])
    
    grupo.clear()
    a = str(input('Quer continuar? '))
    if a in 'Nn':
        break



print(f'Ao todo foram cadastradas {len(grupo)}')
print(f'As pessoas com o maior peso {mai} KG')
for p in grupo:
    if p[1] == mai:
        print(f'{p[0]}')
    if p[1] == men:
        print(f'{p[0]}')
print(f'As pessoas com o maior peso {men} KG')
