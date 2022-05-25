import json 
import requests

print("Sometimes you just dont want to send data that is not form-econded ")

url = 'https://api.github.com/some/endpoint'

payload = {'some':'data'}

#r = requests.post(url, data = json.dumps(payload))

#Instead of encodign the dict yourself, you can also pass it directly using the json parameter, it will be encoded automatically

r = requests.post(url, json =payload)

print(r)

print('\n-----------//-----------//----------//---------')

print("POST a Multipart-Encoded File")

url = 'https://httpbin.org/post'
'''#files = {'file': open('report.xls', 'rb')}

r = requests.post(url, files = files)

print(r.text)'''