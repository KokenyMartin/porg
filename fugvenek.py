"""
fügvények 
előredefiniált folyamatok amik külsőértéktő fügetlen végrehajtják belső utasítasra
def fugvenyNev():
    #fugvény tartalma

fugvenyNev() #fügvénybehivása
"""
#viszatérési értéknélküli fgv
#általában kiiratáskor használju

def oszeadas():
    a=12
    b=17
    print(a+b)

def oszeadasparam(a,b):
    c=a+b
    print(c)

oszeadas()
oszeadasparam(12,17)

#vszatéréslrendelkező fgv
def kettoaatizediken():
    #a=math.pow(2,10)
    a=2**10
    return a

valtozo=kettoaatizediken()
print(valtozo)

def oszeadasvizsateresel(a,b):
    c= a + b
    return c
print(oszeadasvizsateresel(12,18))
