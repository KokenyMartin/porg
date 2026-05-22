def tr(sor):
    print(sor)
    ts=sor.strip().split(';')
    print(ts)
    datum=ts[2].split('.')
    print(datum)
    ido=ts[3].split(':')
    print(ido)
    st=(ts[0],ts[1],int(datum[0]),int(datum[1]),int(datum[2]),int(ido[0]),int(ido[1]),float(ts[4]))
    print(st) 

def main():
    sor="kis pista;4232176;2000.02.03;12:30;5.9"
    tr(sor)
    
main()