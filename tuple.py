# a = 23
# b="alma"
# c=True

# t=[a,b,c,[k1,k2]]
# t[0]

def legNagyobb(lista1):
    legnagyobb=0
    for i in range(0,len(lista1),1):
        if(lista1[i]>lista1[legnagyobb]):
            legnagyobb=i

    return legnagyobb

def legNagyobb2(lista,honapok):
    legnagyobb=0
    honap=honapok[0]
    for i in range(0,len(lista),1):
        if(lista[i]>lista[legnagyobb]):
            legnagyobb=i
            honap=honapok[i]

    return (legnagyobb,honap, lista[legnagyobb])

def main():
    honapok = ["Január","Február","Március","Április","Május","Június","Július","Augusztus","Szeptember","Október","November","December"]
    jani=[4.0,3.8,4.2,4.1,3.7,3.8,4.2,4.7,3.7,3.8,4.2,4.1,]

    legnagyobb=legNagyobb(jani)
    print(honapok[legnagyobb])

    valasz=legNagyobb2(jani,honapok)
    print(valasz)

    szoveg="jani 2000 10 03"
    print(szoveg)
    tordelt=szoveg.split(" ")
    adat=(tordelt[0], int(tordelt[1]), int(tordelt[2]), int(tordelt[3]))
    print(tordelt)
    print(adat)
    print(2026-int(tordelt[1]))


    szoveg2="2026.02.19 3 pogramozás".split(" ")
    datum=szoveg2[0].split(".")
    print(datum)
    februar=datum[1]
    print(februar)

    szoveg3="abcd-123,kis pista,k33586172,1991.03.10".split(",")
    datum=szoveg3[3].split(".")
    ev=datum[0]
    print(ev)
    nev=szoveg3[1].split(" ")
    vezeteknev=nev[0]
    print(vezeteknev)
    
#hf 
#keresztnév honap
st="abcd123 kis pista kj-33586172 1991.03.10".split(" ")
rendszam=st[0]
print(rendszam[3])


#nagy béla:2026_02_19 - 12:13:20
#nap ora kersztnév

main()