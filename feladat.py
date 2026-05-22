söveg="kecskeméten van egy kutya"
print(söveg)
for karakter in söveg:
    if karakter !=" ":
        print(karakter,end="")
    else:
        print()
print()


db=int(input())
while(not(db<=len(söveg) and db>=1)):
    print(f"adjomegeszámot [1 {len(söveg)}] közöt:")
    db=int(input())
ujszoveg=""
for i in range(0,db,1):
    ujszoveg+=söveg[i]
print(ujszoveg)

print(f"adjameg hányadik karktertöl iduljon [1,{len(söveg)}]")
mettol=int(input())
while( not(mettol<=len(söveg)-db and mettol>=1)):
    print("hibás szám")
    print(f"adjameg hányadik karktertöl iduljon [1,{len(söveg)}]")
    mettol=int(input())

for i in range(mettol-1,mettol+db,1):
    print(söveg[i],end="")
