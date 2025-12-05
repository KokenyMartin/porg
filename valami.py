"""
lista ginamikus 
-tudunk bele új elmeke raknicöketeni
létre bármien elemet
déklsrálás:
lista_name.append(ujelem)
elem törlés
lista_name.remove
"""

szamok =[3,2,5,7,1]
print("lista hosza :",str(len(szamok)))
print("lista 1 eleme", szamok[0])
print("utolsó eleme :", szamok[len(szamok)-1])








szoveg = "eze"
dube="sz" #Dupla betü
print(szoveg)
index = 0
while(index <len(szoveg)-1 and not(szoveg[index] == dube[0] and szoveg[index+1] == dube[1])):
    index +=1
if(index<len(szoveg)-1):
    print("benevan dupla betü")
else:
    print("nincs bene dupla betü")

ujszoveg = ""
for index in range(len(szoveg) -1,-1,-1):
    ujszoveg +=szoveg[index]
if(ujszoveg == szoveg):
    print("A szöveg paligrom")
else:
    ("A szöveg nem paligrom")

j = 0
while(j<len(szoveg)/2 and szoveg[j] ==szoveg[len(szoveg)-1-j]):
    j+=1
if(j<len(szoveg)/2):
    print("a szöveg palindrom")
else:
    print("nem palidrom")
