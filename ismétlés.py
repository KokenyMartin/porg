import random

lista = []
n = 13
for index in range(0,n,1):
    a = random.randint(1000,9999)
    veletlen = random.randint(1,3)
    if(veletlen == 1):
        lista.append(a*10+3)
    elif(veletlen == 2):
        lista.append(a*10+5)
    else:
        lista.append(a*10+7)

print(lista)

harom = 0
ot = 0
het = 0
for index in range(0,len(lista),1):
    if(lista[index] % 10 == 3):
        harom += 1
    elif(lista[index] % 10 == 5):
        ot += 1
    else:
        het += 1
print(harom)
print(ot)
print(het)



