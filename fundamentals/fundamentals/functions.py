from datetime import datetime, timedelta,timezone
import json
def converteJson(crime,l_region):
    dict_crimes = {
        'process_time' : exitData(datetime.now),
        'region' : l_region,
        'crimes' : ''
    }
    dict_crimes['crimes'] = crime
    return print(json.dumps(dict_crimes))

def exitData(data):
    data = datetime.now()
    diferenca = timedelta(hours=-3)
    tz = timezone(diferenca)
    data = data.astimezone(tz)
    data_format = data.strftime('%d/%m/%Y %H:%M')
    return data_format 