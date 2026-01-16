import random

def szamlista(db):
    lista=[]
    for i in range(db):
        szam=random.randint(-10,50)
        lista.append(szam)
    return lista

def main():
    lista=szamlista(13)
    print(lista)   
main()

def pozitiv(lista):
    darab=0
    for i in range(len(lista)):
        if(lista[i]>0):
            darab+=1
    return darab
print(pozitiv)