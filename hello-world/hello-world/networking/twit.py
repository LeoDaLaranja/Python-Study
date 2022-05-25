import urllib.request, urllib.parse, urllib.error
import json
#import twurl
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    acct = input('Twitter account: ')
    if len(acct) <1 : break
    #url = twurl.argument(TWITTER_URL,
    #{'screen_name':acct, 'count': '5'})
    #print('Retrieving', url)
#então é o seguinte, não dá para fazer muita coisa aqui,
#sem entender o que é essa twurl 
#é uma api que não dá para ser referenciada de um jeito normal
#simplesmente eu deveria usar outra 
#GRANDE DIA!