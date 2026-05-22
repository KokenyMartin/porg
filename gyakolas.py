import random


def eldontes(szam):
    if(szam>0):
       return 1
    elif(szam<0):
       return -1
    else:
      return 0
    
# def szamok():
#     a=random.randint(-5,5)
#     return a
def elojelEllenorzo():
    vel = random.randint(-5,5)
    elojel = eldontes(vel)
    print(f"Szám: {vel} előjele: {elojel}")

def heteloszthatoe():
    heteloszt=[]
    vszam=random.randint(5,49)*2+1
    while(vszam%7 !=0):
       heteloszt.append(vszam)
       vszam=random.randint(5,49)*2+1
    return heteloszt, vszam

def megszamlalás(lista,szam):
    db=0
    for elem in lista:
        if(elem%10 ==szam):
         db +=1
    return db

def main():
    elojelEllenorzo()
    lista,hetel=heteloszthatoe()
    print(lista)
    print(hetel)
    print(megszamlalás(lista, 3))
main()