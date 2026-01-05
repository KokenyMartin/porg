n =13
import random

lista = []

for index in range(0,n,1):
    a = random.randint(0,20)
    lista.append(a)

oszeg =0
print(lista)
for index in range(0,len(lista),1):
    oszeg +=lista[index]
print(oszeg)