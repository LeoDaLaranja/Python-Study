import json

pessoa = '{"nome": "Rafael","idade": 29,"cidade":"SP"}'
pessoa_dict = json.loads(pessoa)

print(type(pessoa_dict))
print(pessoa_dict)
print(pessoa_dict['idade'])

print('\n------------//---------------//------------//---------')
print("Convertendo Python para JSON ")
'''
Para isso usamos json.dumps()
o s é de string 
'''

data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])
