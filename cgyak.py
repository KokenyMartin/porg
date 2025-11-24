import random
db=0


r = random.randint(10,99)
print(r)
a = int(input("irj be egy számot :"))
while(a !=r):
    a=int(input("Probáld ujra :"))
    if (a>r):
        print("a szám nagyob")
    elif(a<r):
        print("a szam kisebb")
    else:
        print("Eltaláltat")

