
"""x= input("escriba un numero: ")"""

#verificar que sea un numero
"""while (not x.isnumeric()) or (int(x)<1):
    x= (input("debe ser un numero: "))
    break"""
#esto no funciona pq el simbolo negativo lo toma como un str
#convertimos en num a float y fijamos las variables 
"""x= float(x)
par= x % 2 ==0
positivo = x>0"""

"""print(par)
print(f"{positivo} es positivo")""" #verificar que se cumplen las variables 

#establecemos las codiciones
"""if par and positivo:
    print(f"{x} es par y es positivo")
if par and not positivo:
    print(f"{x} es par y es negativo")
if not par and positivo:
    print(f"{x} es impar y positivo")
if not par and not positivo:
    print(f"{x} es impar y negativo")"""

    
########################################################
#EJERCICIO 2
#pedimos los numeros
"""a= int(input("ingrese un numero"))
b= int(input("ingrese otro numero"))
c= int(input("finalmente un numero"))

#fijamos las sumas 
suma_1= a+b
suma_2= b+c
suma_3= a+c

#comparamos los resultados
if suma_1 > suma_2 and suma_3:
    print(f"{suma_1} es la mayor")

if suma_2 > suma_1 and suma_3:
    print(f"{suma_2} es la mayor")

else:
    print(f"{suma_3} es la mayor")"""

######################################################
#EJERCICIO 3

"""nombre= input("ingrese su nombre: ")
edad= input("ingrese su edad: ")

while (not edad.isnumeric()) or (int(edad) < 1):
    edad= input("ingrese su verdadera edad: ")
    

edad= int(edad)

if edad <= 4:
    print(f" {nombre} y tu edad es {edad} entonces tu entrada será GRATIS")
elif edad <= 18:
    print(f" {nombre} y tu edad es {edad} entonces tu entrada será $1.50")
elif edad >= 60:
    print(f" {nombre} y tu edad es {edad} entonces tu entrada será $1")
else:
    print(f" {nombre} y tu edad es {edad} entonces tu entrada será $2.00")"""

###################################################################################
#EJERCICIO 4
"""pts= input("ingresa el numero d puntos que ganaste: ")
while (not pts.isnumeric()) or (int(pts) <1):
    pts= input("ingresa el numero d puntos que ganaste: ")

pts= int(pts)
while pts > 200:
    pts= int(input("ese rango d pts funciona. Ingresa otro: "))
    continue

if pts <= 50: 
    print(f"No hay premios para {pts} pts")
if pts > 51 and pts <= 150:
    print(f"Felicitaciones, Ganaste la medalla de Bronze por haber tenido {pts} pts!")
if pts > 150 and pts <= 180:
    print(f"Felicitaciones, Ganaste la medalla de Plata por haber tenido {pts} pts!")
if pts > 180 and pts <= 200:
    print(f"Felicitaciones, Ganaste la medalla de Oro por haber tenido {pts} pts!")"""

#############################################################
#EJERCICIO 5
jug_1= input("piedra\npapel\ntijera \n Elije tu opcion: ")
print("ahora el segundo jugador")
jug_2= input("piedra\npapel\ntijera \n Elije tu opcion: ")

if jug_1.lower() == "papel" and jug_2.lower() == "tijera":
    print("GANA JUGADOR 2")
if jug_1.lower() == "papel" and jug_2.lower() == "piedra":
    print("GANA JUGADOR 1")
if jug_1.lower() == "piedra" and jug_2.lower() == "tijera":
    print(f"GANA PIEDRA")
if jug_1.lower() == jug_2.lower():
    print("NO HAY GANADOR")
