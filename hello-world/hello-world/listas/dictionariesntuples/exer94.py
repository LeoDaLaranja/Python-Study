pessoa = dict()
grupo = list()
mulheres = list()
age_up = list()
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: '))
    pessoa['idade'] = int(input('Idade: '))
    soma+=pessoa['idade']
    grupo.append(pessoa.copy())
    n = str(input('Deseja continuar? '))
    if n in 'Nn':
        break

media = soma/len(grupo)

for k,v in pessoa.items():
    if pessoa['sexo'] == 'Ff':
        mulheres.append(pessoa['nome'],pessoa['idade'])
    if pessoa['idade'] > media:
        age_up.append(pessoa['nome'])

    
print(mulheres)
print(media)
print(age_up)