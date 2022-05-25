pessoa = dict()
trabalhador = list()


pessoa['nome'] = str(input("Nome: "))
pessoa['nasc'] = int(input("Ano de nascimento: "))
pessoa['ctps'] = int(input("CTPS: "))
trabalhador.append(pessoa.copy())
if pessoa['ctps'] !=0:
    pessoa['contra'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    trabalhador.append(pessoa.copy())
    age_now = 2021 - pessoa['nasc']
    age_contra = 2021 - pessoa['contra']
    if age_now >= 65 and age_contra>15:
        pessoa['status'] = 'Aposentado'
        trabalhador.append(pessoa.copy())
        print('Voce já pode se aposentar!')
    elif age_now<65 and age_contra>15:
        apo = 65 - age_now
        pessoa['status'] = 'Em andamento'
        pessoa['Apo'] = apo+2021
        pessoa['ida_apo'] = apo
        trabalhador.append(pessoa.copy())
        print(f'Falta {apo} para você se aposentar e você se aposentar ano ano de {apo+2021}')
    else:
        apo = 65 - age_now
        age_to = 15 - age_contra
        pessoa['status'] = 'Em andamento'
        pessoa['Apo'] = apo+2021
        pessoa['ida_apo'] = apo
        pessoa['contri'] = age_to
        trabalhador.append(pessoa.copy())
    
        print(f'Você precisa contribuir mais {age_to} anos, para se aposentar com {apo} no ano de {apo+2021}')


print('Cadastro Finalizado com sucesso')

    
print('-='*20)
for k,v in pessoa.items():
    print(f'{k} = {v}')
    
    