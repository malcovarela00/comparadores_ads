## Recorrer lista de links
import requests
import urllib
from urllib.request import urlopen

urls = open('urls.txt', 'r')
urls = [_.rstrip('\n') for _ in urls.readlines()]

def recorrer_url_con_urlib(lista_urls):
    for i in urls:
        print(i)
        r = urllib.request.urlopen(i)
        print('completado')
        print('\n')

def recorrer_url(lista_urls):
    for i in urls:
        print(i)
        r = requests.get(i)
        print('completado')
        print('\n')

def recorrer_url_con_urlopen(lista_urls):
    for i in urls:
        print(i)
        r = urlopen(i)
        print('completado')
        print('\n')

recorrer_url(urls)