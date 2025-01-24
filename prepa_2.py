#diccionario tiene un valor key y value ejm Banco: {dinero[3, 2,]} key: banco value: dinero 

#identifique si el numero es las siguientes condiciones 

x = input("ingrese un numero")
x = int(x)

p= True #cuando iniciamos siempre es primo 
for d in range(2,x): #para cadad divisor en el rango d estos numeros, empieza en 2 y termina en x
    if x%d == 0: # si esta condicion se cumple entonces el numero no es p es compuesto
        p= False #entonces no es primo , es compuesto 
        print("es compuesto")
        break
if p: 
    print("es primo")

for d in range(1,x): #asta el numero que indique d=0 range llega hasta el anterior 
    if d*(d+1)==x:
        print("es oblongo")
        break

aux= str(x)[::-1] #sto invierte la variable- es un espejo y solo funciona con los str
if x ==int(aux):
    print("es palindromo")

a=0
for d in range(1,x):
    if x%d == 0:
        a+=d #la suma de sus divisores
if a == x:
    print("es perfecto")
elif a > x: #necesitamos que primero se cumpla esto
    print("es abundante")
else: #ese pq si no es mayor entonces es menor por lo tanto sino es mayor entonces
    print("es deficiente")

c= False  #yo no se si es cuadrado o no por eso false 
for d in range(x):
    if d**2 == x: #d es cualquier numero entonces  cualquier numero elevado me da el numero ingresado es cuadrado 
        c: True
        print(" es cuadrado")
        break
if not c: #si no es verdadero 
    print("no es cuadrado")

    





