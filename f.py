import random

def radomnevek():
    nevek=["Venus", "Serena", "Richard", "Oracene", "Paul Cohen", "Rick Macci"]
    nevek2=["venus", "serena", "richard", "oracene", "paul cohen", "rick macci"]
    rnd=random.randint(0,999)
    oszeg=rnd//100+(rnd//100*100)//10+rnd%10
    maradek =oszeg%len(nevek)
    return nevek2[maradek],rnd

def edzesterv(napok):
    lista=[]
    for i in range(napok):
        szam=i*i
        if(i%3==0):
            szam+=50
            lista.append(szam)
    return lista

def esosNapok(utesek):
    nap=str(utesek)
    i=0
    while(i<len(nap) and nap !="0"):
        i+=1
        return i<len(nap)

def main():
    nev,rnd=radomnevek()
    print(rnd,nev)
    szam=int(input())
    
    edzes=edzesterv(szam)
    print(edzes)
    napokdzm=int(input())
    vote=esosNapok((edzes[napokdzm-1]))
    if(vote):
        print("volt")
    else:
        print("nem volt")
main()