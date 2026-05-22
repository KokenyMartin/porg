def beolv():
    f=open("resztvevok.txt", encoding="UTF8")
    t=[]
    elso=f.readline().strip().split(';')
    sorok=f.readlines()
    for sor in sorok:
        st=sor.strip().split(';')
        t.append((st[0],st[1],st[2],int(st[3]),st[4]))
    f.close
    return t, elso

def alatok(lista,alat):
    db=0
    for i in range(len(lista)):
        if(lista[i][4]==alat):
            db+=1
    return db

def main():
    adat=beolv()
    f1=adat[0]
    f2=adat[1]

    alat=alatok(f1,f2[1])
    print(alat)

main()