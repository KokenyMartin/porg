

        




sz = input("adj meg egy szot :")
index =0
while(index<len(sz)-1 and not(sz[index] == "c" and sz[index+1] =="s")):
    index +=1
print(index)
if(index <len(sz)-1):
    print("van bene cs")
else:
    print("nicsbene cs")


szo = input("irj egy szot :")
db=0
while(db<len(szo)-1 and not(szo[db]=="s" and szo[db] =="z")):
    db +=1
print(db)
if(db <len(szo)-1):
    print("van bene sz")
else:
    print("nincs bene sz")