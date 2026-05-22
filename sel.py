def fajbeolvasas():
    f=open("szeleromu.txt",encoding="utf8")
    t=[]
    sorok=f.readlines()
    for sor in sorok:
        st=sor.strip().split(';')
        t.append((st[0],st[1],st[2],int(st[3]), int(st[4]), int(st[5])))
    f.close()
    return t

def eromuvek(lista,eve):
    oszeg=0
    for i in range(len(lista)):
       if(lista[i][5] ==eve):
           oszeg +=lista[i][3]
    return oszeg

def main():
    adat=fajbeolvasas()
    print(adat)
    eve=int(input())
    db=eromuvek(adat,eve)
    print(db)
main()