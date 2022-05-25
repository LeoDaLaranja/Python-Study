d1 = {
    'str': 'valor',
    123 : 'Outro valor',
    (1,2,3,4) : 'Tupla'
}

print('str' in d1) 
print('str' in d1.keys()) #nesse ele checa as chaves
print('valor' in d1.values()) #nesse se existe valores com esse atributo passado


'''op = input('Verifica: ')

if op in d1:
    print('Existe')
else:
    print('Não existe')

for k,v in d1.items():
    if op in d1:
        print('Existe')

    print('Key:',k,'Value:',v)

'''
clientes = {
    'cliente 1': {
        'nome': 'Luiz',
        'sobrenome' : 'Otávio',
        'idade' : 16
    },
    'cliente 2':{
        'nome': 'Leo',
        'sobrenome' : 'Alves',
        'idade' : 20
    }
}

for cliente_k, cliente_v in clientes.items():
    print('=' * 10)
    print(f'Exibindo {cliente_k}')
    
    for dados_k, dados_v in cliente_v.items():
        print(dados_k,':', dados_v)

        
    if cliente_v['idade'] > 18:
        print(cliente_v['nome'],'é maior de idade')
