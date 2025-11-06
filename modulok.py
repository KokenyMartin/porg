import math
import random

a = 2
gyoka = math.sqrt(a)
print("gyök ("+ str(a)+") = ", gyoka)
felkerekit = math.ceil(gyoka)
print("felkerekit", felkerekit)
lekerekit = math.floor(gyoka)
print("lekerekit", lekerekit)
kerekites = round(gyoka,2)
print("kerekites", kerekites)
hatvanyozas1 = math.pow(gyoka, 2)
print("hatványozás", hatvanyozas1)

alap = 2
kitevo = 5
#hatvanyozas2 = math.pow(alap, kitevo)
hatvanyozas2 = alap ** kitevo
print(alap,"^",kitevo,"=",hatvanyozas2)
vszam1 = random.randint(2,10)