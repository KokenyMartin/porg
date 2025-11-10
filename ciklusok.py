import random as r
'''
cilusok ismétlés loop

számláló for ciklus
végig megy a megadot elemeken vagy intevallumokan
for elem in range (metol , medig hánszával):

for karakter

tesztelős while
'''

for elem in range(0,19,2):
    print(elem, end=" ")

söveg = "kecskemét"
print(söveg)
for karakter in söveg:
    print(karakter, end=",")
print()

#söveg [0]
#söveg [1]
#söveg [2]
for index in range(0, len(söveg)-1,1):
    print(söveg[index], end=",")
print(söveg[-5])


for elem in range(32,50,4):
    print(elem)
print()


for b in range(10,0,-1):
    print(b, end=" ")
print()

ujszöveg=""
for index in range(len(söveg)-1,-1,-1):
    ujszöveg +=söveg[index]
    print(söveg[index],end="")

print()

for index in range(0, len(söveg), 1):
    print(str(index+1)+söveg[index], end=" ")
print()
for db in range (0,5,1):
    sam=r.randint (0,3)
    print(söveg[sam], end=" ")
print()

print(ujszöveg)