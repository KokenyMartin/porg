# 1.a Írjon egy fv-t, ami visszaadja egy számról, hogy milyen az előjele. 
# Poz: 1 
# Neg: -1 
# Nulla: 0
# 1.b Írjon egyljárást, ami ellenőrzi az előző feladat működését, egy [-5,5] intervallumon kigenerált számot írassaon ki és írja ki az előjelét!
# pl. Szám: -2 előjele: -1
# pl. Szám: 3 előjele: 1
# pl. Szám: 0 előjele: 0

# 2.a Írjon egy fv-t, ami feltölt egy listát, úgy számokkal, hogy addig teszi bele a véletlen kétjegyű páratlan számokat, amíg 7-tel osztható számot nem kap!
# 2.b Írassa ki a fő (main) eljárásban a listát és külön a héttel osztható számot!
# 2.c Írjon egy fv-t, ami megnézi egy listának hány darab 3-ra végződő eleme van?
# 2.d a fő eljárásában ellenőrizze a 2.c feladat működését!

import random

def elojelSzam(szam):
    if szam > 0:
        return 1
    elif szam < 0:
        return -1
    else:
        return 0

def elojelEllenorzo():
    vel = random.randint(-5,5)
    elojel = elojelSzam(vel)
    print(f"Szám: {vel} előjele: {elojel}")

def main():
    elojelEllenorzo()

main()