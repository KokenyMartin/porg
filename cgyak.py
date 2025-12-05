import random
db=1


r = random.randint(10,99)
print(r)

a = int(input("irj be egy számot :"))
while(a !=r):
    a=int(input("Probáld ujra :"))
    if(a>9 and a<100):
        if (a>r):
            print("a szám nagyob")
        elif(a<r):
            print("a szam kisebb")
        db +=1
    else:
        print("nem kétjegyű")

print("eltaláltad")
print(db)

