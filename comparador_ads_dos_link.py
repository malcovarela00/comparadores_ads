import urllib
import requests

link1 = input("Ingrese el primer link: ")
f1 = requests.get(link1)
f1 = f1.text.split('\n')
f1 = [_.rstrip('\n').replace(' ', '') for _ in f1]
f1 = [_.replace('\r', '') for _ in f1]


link2 = input("Ingrese el segundo link: ")
## Obtener el archivo de la url en una lista
f2 = requests.get(link2)
f2 = f2.text.split('\n')
f2 = [_.rstrip('\n').replace(' ', '') for _ in f2]
f2 = [_.replace('\r', '') for _ in f2]

coincidentes = []
no_coincidentes = []

for i in f1:
    for j in f2:
        if i ==j:
            coincidentes.append(j)

no_coincidentes = list(set(f1) - set(coincidentes))

print('LISTA DE COINCIDENTES')
print('\n'.join(coincidentes))
print('\n')
print('LISTA DE NO COINCIDENTES')
print('\n'.join(no_coincidentes))
