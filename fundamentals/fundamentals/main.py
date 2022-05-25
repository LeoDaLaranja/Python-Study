from functions import converteJson
import csv

#vamos ver o que é preciso para resolver esse problema 
'''
1- Ler o arquivo 
2- Agrupar items/ qual seria a melhor forma de fazer isso?
2.1- Agrupar por região, manter apenas regiões com mais de 2 tipos de infrações 
2.2- Manter o número de crimes/contabilizar crimes com mais de 10 ocorrências na região 
3-Colocar o horário em que foi feito o processamento -> dd/MM/yyyy HH:mm
4-Saida tem que ser em um formato JSON
Exemplo de saída
{"process_time": "01/09/2021 16:01", "region": "South West", "crimes": [{"crime": "All other theft offences", "count": 25959}, {"crime": "Bicycle theft", "count": 3090}]}

{"process_time": "01/09/2021 16:02", "region": "East", "crimes": [{"crime": "All other theft offences", "count": 8797}, {"crime": "Bicycle theft", "count": 719}]}
'''
#vou rodar com a testes 
## depois eu rodo com a padrão
try:
    with open('fundamentals/tabela-crimes.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        temp_count = 0
        crime = []
        
        crimes = {'crime': ' ', 'count': ''}
        header = next(csv_reader)
        l_region = ''
        for line in csv_reader:
            #index 0 = date
            #index 1 = PFA
            #index 2 = Region
            #index 3 = Offence
            #Index 4 = Number of offences
            temp = l_region
            
            
            
            l_region = line[2]
            l_offence = line[3]
            l_num_offence = line[4]
            
           
            
            temp_count +=1
            
            if temp == '':
                crimes['crime']= l_offence
                crimes['count'] = l_num_offence

                crime.append(crimes.copy())

            elif l_region == temp:
                
                crimes['crime'] = l_offence
                crimes['count'] = l_num_offence
                crime.append(crimes.copy())
                
            elif l_region != temp:
                converteJson(crime,temp)
                crime.clear()
                crimes.clear()
                crimes['crime'] = l_offence
                crimes['count'] = l_num_offence
                crime.append(crimes.copy())
                
               
            
        
except Exception as e:
    print('Error ',e)




