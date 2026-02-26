def Adat():
    lista=[]
    db=int(input())
    for i in range(db):
        st=input().split(";")
        lista.append((st[0],st[1],st[2],int(st[3]),int(st[4]),int(st[5])))
    return lista

def darab(lista):
    oszeg=0
    for i in range(len(lista)):
        oszeg+=lista[i][3]
    return oszeg

def legtobbetTelepitet(lista):
    maxi=0
    for i in range(len(lista)):
        if(lista[i][3]>lista[maxi][3]):
            maxi=i
    return maxi

def varos(lista,varos):
    i=0
    while(i<len(lista) and lista[i][0] !=varos):
        i+=1
    vane=i<len(lista)
    return vane

def main():
    adat=Adat()
    # print(adat)

    db=darab(adat)
    print(db)

    legtobb=legtobbetTelepitet(adat)
    print(adat[legtobb][0],adat[legtobb][5])

    varost=input()
    vane=varos(Adat,varost)
    if(vane):
        print("van")
    else:
        print("nincs")
main()