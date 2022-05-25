
from datetime import datetime, timedelta,timezone



data = datetime.now()

gp_m = open('fileStudy/basic.csv','r')




#Formatando a data 
def getLocaltime(data):
    #Está funcionando
    diferenca = timedelta(hours=-3)
    tz = timezone(diferenca)
    data = data.astimezone(tz)
    data_format = data.strftime('%d/%m/%Y %H:%M')
    return data_format



def converToJson(gp_m):
    try:
        converted = gp_m.to_json('fileStudy/basic.json')
    except Exception as e:
        print('error: '+e)
    return converted


def dataExit(convert,data_formated):
    '''
    Duas opções
    1° - Editar a linha do arquivo para colocar o horário da busca
    2° - Criar uma nova coluna onde será armazenado o horário, porém isso talvez demore e precise criar uma 
        string gigante 
        concatenar o horario com a linha em json 
    '''
    ref = open('fileStudy/basic.json','r')
    for linha in convert:
        valores = linha.split()
        print(data_formated+''+valores)
    ref.close()   

data_formated = getLocaltime(data)
convert = converToJson(gp_m)
data_exit = dataExit(convert)