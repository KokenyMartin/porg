"""
fügvények 
előredefiniált folyamatok amik külsőértéktő fügetlen végrehajtják belső utasítasra
def fugvenyNev():
    #fugvény tartalma

fugvenyNev() #fügvénybehivása
"""
#viszatérési értéknélküli fgv
#általában kiiratáskor használju
import random
def oszeadas():
    a=12
    b=17
    print(a+b)

def oszeadasparam(a,b):
    c=a+b
    print(c)

oszeadas()
oszeadasparam(12,17)

#vszatéréslrendelkező fgv
def kettoaatizediken():
    #a=math.pow(2,10)
    a=2**10
    return a

valtozo=kettoaatizediken()
print(valtozo)

def oszeadasvizsateresel(a,b):
    c= a + b
    return c
print(oszeadasvizsateresel(12,18))

def veletlenszam(db):
    for i in range(0,db,1):
     print(random.randint(100,999),end=" ")
    print()
veletlenszam(5)

def szovegvisza(szoveg):
    for i in range(len(szoveg)-1,-1,-1):
        print(szoveg[i], end="")
    print()

szovegvisza("kalapács")

viszaszoveg = ""
def szvegviszafele(szoveg):
    for i in range(len(szoveg)-1,-1,-1):
        viszaszoveg += szoveg[i]
    return viszaszoveg

print(szovegvisza("kalapasc"))

i=0
def palindorom(szo):
    while(i <=len(szo)//2 and szo[i] == szo[len(szo)]-1-i):
        i +=1
    

        
print(palindorom("ada"))
