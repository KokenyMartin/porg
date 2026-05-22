import random

def datum(datumid):
    szetszed=datumid.split(" ")
    daTum=szetszed[0].split(".")
    ido=szetszed[1].split(":")
    lista=[int(daTum[0]),int(daTum[1]),int(daTum[2]),int(ido[0]),int(ido[1])]
    return lista

def szamok(a,b):
   c=a/b
   tort=str(c).split(".") 
   return int(tort[1])

def prime(szam):
    a=2
    while( szam > a and szam%a !=0):
        a+=1
    return a==szam

def listafltolt():
    lista=[]
    for i in range(10):
        szam=random.randint(10,99)
        while(not prime(szam)):
            szam=random.randint(10,99)
        lista.append(szam)
    return lista

def vege(lista):
    db=0
    for i in range(len(lista)):
        if(lista[i]%10==9):
            db+=1
    return db

# def ismetles(lista):


def main():
    datumok=datum("2026.05.08 10:02")
    print(datumok)
    szam=szamok(10,8)
    print(szam)
    lista=listafltolt()
    print(lista)
    print(vege(lista))
main()