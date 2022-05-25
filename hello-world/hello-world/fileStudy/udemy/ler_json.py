import json

with open('filestudy/udemy/pessoa.json','r') as file:
    d1_json = file.read()
    #transforma json em algo que de para percorrer

    d1_json = json.loads(d1_json)

    for k,v in d1_json.items():
        print(k)
        for k1,v1 in v.items():
            print(k1,v1)
