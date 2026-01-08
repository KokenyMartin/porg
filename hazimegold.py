# számtani átlag
# mértani átlag
# 13, 17-re végződő szám, hany osztható 13, 17-tel
import random
import math
n = 31
lista = []

for i in range(0,n,1):
    szam = random.randint(1000,9999)
    veletlen = random.randint(1,2)
    if(veletlen == 1):
        lista.append(szam*100+13)
    else:
        lista.append(szam*100+13)
    
print(lista)


oszeg = 0
for elem in lista:
    oszeg +=elem
#atlag = oszeg / len(lista)
atlag = oszeg / n
print(round(atlag,2))

dba = 0
for i in range(0,n,1):
    if(atlag>lista[i]):
        dba +=1

print(dba)


szorzat = 1
for elem in lista:
    szorzat *= elem
matlag = math.pow(szorzat,1/n)

print(matlag)

mosze =0
for a in lista:
    if(matlag > a):
        mosze +=a

print(mosze)

# bekérsz egy hoszab szöveget hány da rab felhasználoáltal megadot betűvan bene
# bekész két szot mond meg adott indexen hány darab egyezés és külöbszg

szoveg = "bekérsz egy hoszab szöveget hány da rab felhasználoáltal megadot betűvan bene"
betu = input("adjon meg egy betüt: ")

dbbetu = 0
for karakter in szoveg:
    if(karakter == betu):
        dbbetu +=1
print(dbbetu)


szo1 = "alma"
szo2= "alkat"

kulumbseg =0
minumumhosz = 0
if(len(szo1)>len(szo2)):
    minumumhosz =len(szo2)
else:
    minumumhosz= len(szo1)
for i in range(0,minumumhosz,1):
    if(szo1[i] != szo2[i]):
        kulumbseg +=1

print(kulumbseg)