def fajlbeolvasas():
    t=[]
    f=open("eloadasok.txt")
    sork=f.readlines()
    for sor in sork:
        st=sor.strip().split('---')
        t.append((int(st[0]),st[1],st[2]))
    return t

def minimum(lista):
    mini=0
    for i in range(len(lista)):
        if(lista[i][0]>mini):
            mini=lista[i][0]
    return mini

def oszbevetel(lista):
    oszeg=0
    for i in range(len(lista)):
        oszeg+=lista[i][0]
    bevetel=oszeg*4300
    return bevetel

def main():
    adatok=fajlbeolvasas()
    # print(adatok)
    c=minimum(adatok)
    print(c)
    d=oszbevetel(adatok)
    print(d)
main()