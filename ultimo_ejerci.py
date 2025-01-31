import math

p=(0,0)
ps = {(-2,1), (1,1), (2,1), (1,2), (3,2), (5,1)}
primer_calc=True #primer calculo es verdadero

x1= p[0]
y1= p[1]
aux2= True

for tupla in ps:
    x2= tupla[0]
    y2= tupla[1]
    aux = (x1-x2)**2 + (y1-y2)**2
    d = math.sqrt(aux)

    if aux2:
        aux2= False
        dmin= d
        tmin= tupla

    else:
        if d < dmin:
            tmin = tupla

print(tmin)

