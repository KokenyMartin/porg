# Jancsi és Juliska autós kártyát gyűjtenek. Hogy ne legyen vita és gyorsan meg tudják különböztetni melyik autó kié, ezért a következőt találták ki.
#  Mivel minden autó végsebessége 3 jegyű, ezért megnézik a középső számot. Ha páros akkor Jancsié, ha páratlan akkor Juliskáé. 
# Van összesen 30 kártyájuk. Szeretik egymás mellé rakni a kártyákat. Szimuláld a feladatot!
# Írj egy programot, ami kigenerál [300, 499] között egy számot úgy, hogy minden páros helyen Jancsi kártyája van, minden páratlan helyen Juliskáé!
# Add meg Jancsi autóinak végsebességének átlagát!
# Add meg hány darab autója van Juliskának, ami 380-nál nagyobb a végsebessége!
import random
import math

kartya=[]
n = 30
for i in range(0,n,1):
    elso=random.randint(3,4)
    masodik=-1
    if(i%2 ==1):#jamcsi szam
        masodik= random.randint(0,4)*2
    else:#juliska szam
        masodik= random.randint(0,4)*2+1
    harmadik=random.randint(0,9)
    végsebessége =elso*100 + masodik *10 +harmadik
    kartya.append(végsebessége)

print(kartya)



oszeg=0
for i in range(1,len(kartya),2):
   #print(kartya[i])
   oszeg += kartya[i]

db= len(kartya)
atlag= oszeg // db
print("Jancsi autóinak végsebességének átlaga", atlag)

joszeg=0
for i in range(0,len(kartya),2):
    if(kartya[i]>380):
        joszeg += 1

print(joszeg)