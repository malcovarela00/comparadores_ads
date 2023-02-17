import urllib
import requests

urls = open('urls.txt', 'r')
urls = [_.rstrip('\n') for _ in urls.readlines()]

f1 = open("Ads.txt", 'r')
f1 = [_.rstrip('\n').replace(' ', '') for _ in f1.readlines()]

archivo = open("No_coincidentes.txt", 'w')
coincide = open("Coincidentes.txt", 'w')

for link in urls:
    
    archivo.write('\n')
    r = requests.get(link)
    f2 = r.text.split('\n')
    f2 = [_.rstrip('\n').replace(' ', '') for _ in f2]
    coincidentes = []
    
    for i in range(len(f1)):
        for j in range(len(f2)):
            if f1[i] == f2[j]:
                coincidentes.append(f1[i])
                break
    
    no_coincidentes = list(set(f1) - set(coincidentes))
    
    coincide.write('LISTA DE COINCIDENTES de ' + link + '\n''\n')
    coincide.write('\n'.join(coincidentes))
    coincide.write('\n')
    if no_coincidentes == []:
        archivo.write("Todas coinciden")
    else:
        archivo.write('LISTA DE NO COINCIDENTES de ' + link + '\n''\n')
        for i in no_coincidentes:
            archivo.write(i + '\n')


archivo.close()
coincide.close()
print("Archivo creado")
