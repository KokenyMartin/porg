def fajl():
    f=open("forgalom.txt")
    t=[]
    elsosor=f.readline()
    sorok=f.readlines()
    for sor in sorok:
        st=sor.strip().split(' ')
        t.append((int(st[0]),int(st[1]),int(st[2]),int(st[3]),st[4]))
    f.close()
    return t, elsosor



def main():
    f=fajl()
    f1=f[0]
    f2=f[1]
    print(f1,f2)
main()