import urllib
import urllib.request


try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except:
    print('Não foi possivel acessar esse site no momento ')
else:
    print('Esse site está acessível no momento')