'''
print(dict_name.values()) -> printa apenas os valores
print(dict_name.keys()) ->printa apenas as chaves
 chaves == identificação dos 
print(dict_name.itens()) -> printa ambos os valores acima
'''
pessoas = {
    'nome':'Gustavo',
    'sexo':'M',
    'idade': 22,
    'nome':'Leo',
    'sexo':'M',
    'idade': 19,
    'nome':'Ana',
    'sexo':'F',
    'idade': 20
}

print(pessoas)

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} e é do sexo {pessoas["sexo"]}')
print('')

print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

for k,v in pessoas.items():
    print(f'{k} = {v}')
print('')
print('')
estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input("Unidade federativa: "))
    estado['sigla'] = str(input("Sigla: "))
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}')

print("Ou")

print()
for e in brasil:
    for v in e.values():
        print(v, end = ' ')
    print()

