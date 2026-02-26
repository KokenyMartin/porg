# 5
# alma 12 500
# körte 10 600
# szilva 13 300
# cseresznye 8 1200
# meggy 6 1150


def listafetoltes():
    db=int(input())
    t=[]
    for i in range(db):
        sor=input()
        st=sor.split(" ")
        t.append((st[0],int(st[1]),int(st[2])))
    return t

def gumolcsSuj(lista):
    oszeg=0
    for i in range(len(lista)):
        oszeg += lista[i][1]
    return oszeg

def legnagyob(lista):
    maxi=0
    for i in range(len(lista)):
        if(lista[1][2]>lista[maxi][2]):
            maxi= i
    return maxi

def keresetgyumolcs(lista,gyumolcs):
    i=0
    while(i<len(lista) and lista[i] !=gyumolcs):
        i+=1
    vane=i<len(lista)
    if(vane):
        print("van")
    else:
        print("ninsc")



def main():
    adatok=listafetoltes()
    print(adatok)
    adat=adatok[2]
    print(adat[0])

    gumolcssuj=gumolcsSuj(adatok)
    print(gumolcssuj,"q")

    gyumolcs=keresetgyumolcs

    legnyabbar=legnagyob(adatok)
    print(adatok[legnyabbar][0])

    gyumolcs=input("irjbe egy gyümölcsot")
    kereseti=gyumolcs(adatok,gyumolcs)
    if(kereseti <0):
        print("ninsc")
    else:
        print(adatok[kereseti][1],adatok[kereseti][1])
main()