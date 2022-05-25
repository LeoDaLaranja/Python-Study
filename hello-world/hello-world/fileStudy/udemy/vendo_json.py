import json

d1 = {
    'Pessoa 1':{
        'nome':'Lorena',
        'idade':20,
    },
    'Pessoa 2':{
        'nome':'Leo',
        'idade':20
    }
}
d1_json = json.dumps(d1, indent = True)

with open('fileStudy/udemy/pessoa.json','w+') as file:
    file.write(d1_json)
