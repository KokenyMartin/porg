import math

def prim(szam):
    a=2
    b=math.sqrt(szam)
    while(a<math.sqrt(szam) and szam % a !=0):
        a+=1
    return a>=b

def lnko(szam1,szam2):
    kisebb=szam1
    if(szam1>szam2):
        kisebb=szam2
    while(kisebb>=1 and not(szam1 %kisebb==0 and szam2 % kisebb==0)):
        kisebb-=1
    return kisebb


def main():
    a=131
    b=26
    # for i in range(1000000,1002000,1):
    #     if prim(i):
    #         print(i)
    print(prim(a))
    print(lnko(a,b))
main()
