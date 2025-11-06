# generáj ki rgy random sámot [-10, 10]
# irasd ki
import random
import math
vszam1= random.randint(-5, 5)*2
print(vszam1)
# vegyük a szám abszolut értékét
# ha a szám negetiv akor szám * -1 külömben önmaga
if vszam1<0 :
    print("asb :"+str(vszam1*(-1)))
else:
    print("abs :"+str(vszam1))
 
# irassa ki a számot gyökét

if(vszam1 >= 0):
    print("gyök(vszám) :" +str(math.sqrt(vszam1)))
else:
    print("A negativszám számnak nincs gyöke")
    #döncse el a számrol hogy pozitiv, negativ , nula
if(vszam1>0):
        print("poziív")
else:
    if(vszam1==0):
        print("nula")
    else:
        print("negativ")

#fehasználotol bekéré
szoveg =  input("adjon meg egy számot :")
print(szoveg)
#hf vörd pdf böll 8-13
#hf megoldás
sec = 3923
#1óra 5 perc 23 másodperc

ora = sec // 3600
perc = (sec - ora * 3600) // 60
mp =sec % 60
print (ora, str("Óra"))
print(perc, str("perc"))
print(mp)