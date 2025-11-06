# valtozó deklerálasa innicialiálása
#letreholása
#vál neve = kezdöértéke
nev="Kökény Martin"
osztály="10.b"
dátum="2025.09.08"

print(nev,dátum,sep="\n")

# operátorok !!!

#konkatenálás concat kétsöveget öszefüg
osszefuzes = nev+osztály
print(osszefuzes)

#töbszörözés
soknev = nev * 5
print(soknev)
"""
elemi tipusok
-söveg - string -str
(- karaker)
-sám egész integer -int legtöbpontos tört float
-logika true false
"""

aEgesz = 123
bTort = 34,23
szSzam = "12"
logikai = True






# Egész operatorok
print(aEgesz + 2)
print(aEgesz-2)
print(aEgesz * 2)
print(aEgesz / 2)

# div egszrész mod modulus
# div - //
#mod  - %

print("a div 8 =", aEgesz // 8)
print("A mod 8 =", aEgesz % 8)

print(int(szSzam) + aEgesz)
print( szSzam+str(aEgesz))

print (str(aEgesz) + szSzam)
print(aEgesz+int(szSzam))