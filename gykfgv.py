def vaneketjegyualistaban(lista):
    i =0
    while(i<len(lista) and not (lista[i]>=10 and lista[i]<=99)):
        i +=1
    vane= i<len(lista)
    return vane

def main():
    szamok=[2,3,7,5,9,11,1,2,5]
    print(szamok)
    vaneketjegyu=vaneketjegyualistaban(szamok)
    print(vaneketjegyu)
    
main