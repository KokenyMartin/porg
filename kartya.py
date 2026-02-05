import random

def kartyaGeneralas():
    lista=[]
    for i in range(1,14,1):
        lista.append("i" +str(i))
        lista.append("p" +str(i))
        lista.append("k"+str(i))
        lista.append("s"+str(i))
    return lista

def keveres(pakli):
    for i in range(500):
        a=random.randint(0,51)
        b=random.randint(0,51)
        sv=pakli[a]
        pakli[a]=pakli[b]
        pakli[b]=sv

def lapIndexe(lap, pakli):
    index=0
    while(pakli[index] !=lap):
        index +=1
    return index

def main():
    pakli= kartyaGeneralas()
    keveres(pakli)
    print(pakli)
    lap = input("adjon meg egy lapot:")
    index=lapIndexe(lap,pakli)
    print(index)

main()