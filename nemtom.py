import random

def maximum(lista):
   maximum=lista[0]
   for i in range(1,len(lista),1):
      if(lista[i]>maximum):
         maximum+=i
   return maximum

def minimum(lista):
   minimum=lista[0]
   for i in range(1,len(lista),1):
      if(lista[i]<minimum):
         minimum+=i
   return minimum


def maxindex(lista):
   maxi=0
   for i in range(1,len(lista),1):
      if(lista[i]>lista[maxi]):
         maxi+=i
   return maxi

def pozitivAtlag(lista):
   db=0
   poszeg=0
   for i in lista:
      if(i>0):
         db+=1
         poszeg +=i
   patlag=poszeg/db
   return patlag

def listaAtlaga(lista):
   oszeg=0
   for elem in lista:
      oszeg+= elem
   atlag=oszeg / len(lista)
   return atlag

def veletlenlista(n):
   lista=[]
   for i in range(0,n,1):
      negatve=random.randint(0,1)
      vszam=random.randint(2,19)*50
      if(negatve==0):
         lista.append(-1*vszam)
      else:
         lista.append(vszam)
   return lista

def negti00ravegzodo(kiskutya):
   db=0
   for i in range(0,len(kiskutya),1):
      if(kiskutya[i]%100==0):
         db+=1
   return db
      

def main():
   list1=veletlenlista(13)
   print(list1)
   list2=veletlenlista(5)
   print(list2)

   print(negti00ravegzodo(list1))

   listaatlaga=listaAtlaga(list1)
   print(listaatlaga)

   pozitivatlag=pozitivAtlag(list1)
   print(pozitivatlag)

   maxielem=maxindex(list1)
   print(maxielem+1)

   maximumertek=maximum
   print(maximumertek(list1))
   minimumertek=minimum
   print(minimumertek(list1))

main()

