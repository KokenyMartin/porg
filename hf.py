import random

def listaFetoltes():
    lista=[]
    for i in range(0,17,1):
        valsz=random.randint(0,100)
        if(valsz>=50):
            lista.append(random.randint(12,200))
        else:
            lista.append(random.randint(50,120))
    return lista

def listaAtlag(lista):
    oszeg =0
    for i in range(0,len(lista),1):
        oszeg+=lista[i]
    atalag=oszeg/len(lista)
    return atalag

def listaMximum(lista):
    maxe=lista[0]
    for i in range(1,len(lista),1):
        if(lista[0]>maxe):
            maxe =lista[i]
    return maxe

def listaMinimum(lista):
    mine=lista[0]
    for i in range(1,len(lista),1):
        if(lista[0]<mine):
            mine =lista[i]
    return mine

def listaTerjedelme(lista):
    maximum=listaMximum(lista)
    minimum=listaMinimum(lista)
    return maximum - minimum

def vaneMaxpont(lista):
    n= 200
    isdex=0
    while(isdex<len(lista) and lista[isdex] !=200):
        isdex+=1
    vane=isdex<len(lista)
    return vane

def dontobejutotak(lista):
    db=0
    for i in range(0,len(lista),1):
        if(lista[i]/200*100 >=70):
            db +=1
    return db

def ertek50Index(lista):
    i =0
    while(i<len(lista) and lista[i] !=50):
        i+=1
    vane=i<len(lista)
    if(vane):
        return i
    else:
        return -1


def main():
    pontok =listaFetoltes()
    print(pontok)

    atlag =listaAtlag(pontok)
    print(round(atlag,2))

    terjedelem=listaTerjedelme(pontok)
    print(terjedelem)
    
    vane= vaneMaxpont(pontok)
    if(vaneMaxpont):
        print("van")
    else:
        print("nincs")

    darab=dontobejutotak(pontok)
    print(darab)

    index=ertek50Index(pontok)
    if(index == -1):
        print("nincs")
    else:
        print(f"van {index +1}")
main()