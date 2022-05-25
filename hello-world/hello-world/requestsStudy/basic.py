import requests
import json
'''
r = requests.get('https://api.github.com/events')

r = requests.post('https://httpbin.org/post', data ={'key','value'})

r = requests.put('https://httpbin.org/put', data={'key': 'value'})

r = requests.delete('https://httpbin.org/delete')

r = requests.head('https://httpbin.org/get')

r = requests.options('https://httpbin.org/get')
'''
'''
nice caveria play, but also, this is what Requests can do 

Passing parameterers in URLs

Requests allows you to provide these arguments as a dictionary of strings, using the params keyword argument.
'''

user_name = input('User name: ')


r = requests.get('https://httpbin.org/get', params=user_name)

print(r.url)

