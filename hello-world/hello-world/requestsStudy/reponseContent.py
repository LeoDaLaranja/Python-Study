import requests

r = requests.get('https://api.github.com/events')

print(r.encoding)

print('\n-----------//-----------//----------//---------')
print('Custom headers')

url = 'https://api.github.com/some/endpoint'

headers = {'user-agent':'my-app/0.0.1'}

r = requests.get(url, headers= headers)

print(r)

print('\n-----------//-----------//----------//---------')
print('More complicated POST requests')

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("https://httpbin.org/post",data = payload)

print(r.text)

'''
The data argument can also have multiple values for each key. This can be done by manking data either a list of tuples
or a dictionary with lists as values.
'''

payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)

payload_dict = {'key1': ['value1', 'value2']}

r2 = requests.post('https://httpbin.org/post', data=payload_dict)

print(r1.text)

