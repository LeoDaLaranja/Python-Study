bolachas = {
    'Marca 1' : {
        'nome' : 'Trakinas',
        'sabor' : 'chocolate',
        'validade' : 2022
    },
    'Marca 2' : {
        'nome' : 'Trakinas',
        'sabor' : 'morango',
        'validade' : 2018
    },
    'Marca 3' : {
        'nome' : 'Passatempo',
        'sabor' : 'chocolate',
        'validade' : 2019
    },
    'Marca 4' : {
        'nome' : 'Passatempo',
        'sabor' : 'limão',
        'validade' : 2018
    },
}


'''
O que eu quero fazer?
1- Pegar todos os sabores que o nome da marca é passatempo
2 - verificar a validade 
3 - printar todos
'''
sabores_trakinas = []
bolachas_vencidas = 0
for k,v in bolachas.items():
    print('=' * 20)
    print(f'{k}: {v["nome"]}')
    if v['validade'] <2022:
        v['validade'] = 'VENCIDO!'
        bolachas_vencidas +=1
    for bolacha_k,bolacha_v in v.items():
        print(f'{bolacha_k}: {bolacha_v}')
    
    if v["nome"] == 'Trakinas':
        sabores_trakinas.append(v["sabor"])
    


print(f'Os sabores das bolachas trakinas são {sabores_trakinas}')
print(f'Temos um total de {bolachas_vencidas} bolachas vencidas!')
