import random
def vol_cilindro(a,r):
    pi= 3.14 #antes no m daba pq puse el decimal con ,
    resul= a * pi * r**2
    return resul


y= vol_cilindro (int(input("introduzca una alt")), int(input("introduzca un rad"))) #para el imput se pone el nombre de la def y lo q queremos preguntar
print(y) #luego printeamos la variable 

#en los parametros el orden no importa, pero primero van los obligatorios y luego los opcionales
#parametros posicionales son los q se necesitan, los q ingresa el usuario
#parametros definidos son opcionales es como para una variable 

while True:
    i= random.randint(1,2)
    if i == 2:
        print (i +2)
    break
 
#NO SE VA A PRINTEAR PQ NO TIENEN LA VARIABLE YA QUE ESTA DENTRO DEL LOOP LO IDEAL ES PONERLA AFUERA

