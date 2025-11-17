import random as r
import math
'''
cilusok ismétlés loop

számláló for ciklus
végig megy a megadot elemeken vagy intevallumokan
for elem in range (metol , medig hánszával):

for karakter

tesztelős while
'''

for elem in range(0,19,2):
    print(elem, end=" ")

söveg = "kecskemét"
print(söveg)
for karakter in söveg:
    print(karakter, end=",")
print()

#söveg [0]
#söveg [1]
#söveg [2]
for index in range(0, len(söveg)-1,1):
    print(söveg[index], end=",")
print(söveg[-5])


for elem in range(32,50,4):
    print(elem)
print()


for b in range(10,0,-1):
    print(b, end=" ")
print()

ujszöveg=""
for index in range(len(söveg)-1,-1,-1):
    ujszöveg +=söveg[index]
    print(söveg[index],end="")

print()

for index in range(0, len(söveg), 1):
    print(str(index+1)+söveg[index], end=" ")
print()
for db in range (0,5,1):
    sam=r.randint (0,3)
    print(söveg[sam], end=" ")
print()

print(ujszöveg)
"""
elöl tesztelős vsgy while ciklus nem tudjuk hanyszor ismétel akorismétel ha feltétel igaz

while(feltétel):
    utasítások (szekvencia)
"""
velszam = r.randint(0,10)
print(velszam)
while(velszam != 0):
    velszam = r.randint(0,10)
    print(velszam, end=" ")
print()

osszeg = 0
db= 0
a = int(input("szám :"))
#osszeg += a
#db += 1
while(a !=0):
    
    osszeg +=a
    db += 1
    a = int(input("adjonmeg egy számot: "))
print(round(osszeg/db,2))

szo =input("irj egy szot vagy egy szöveget :")
