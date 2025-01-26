#WHILEEE LOOP ESO SE VA A REPETIR MIENTRAS LA CONDICION SE CUMPLA 

i =1 #iterador va iterando numeros por eso se nesecita sumar 1
while i <= 10: #1 es menor q 10= TRUE 
    print(i) #se imprime 1
    i += 1 #sumamos 1= 2 si no estuviera esto solo se printea 1
#hay un momento en el que i va a ser 11 y ahi es donde el code termina 
print("termino el loop")

#guessing game
palabra= "secreto"
guess= ""
guess_count= 0
guess_limit= 3
sin_guesses= False #toavia tienen oportunidades
while guess != palabra and not(sin_guesses):
    if guess_count <= guess_limit:
        guess= input ("pon la palabra secreta ")
        guess_count += 1
    else:
        sin_guesses= True

if sin_guesses:
    print("perdiste")
else:
    print("ganaste")

#FOR LOOP 

for letter in "laura": #por cada letra en laura
    print(letter) #imprime cada letra 
#letter es una variable que cambia cada vez que el loop se repite
#letter puede tener cualquier nombre 
friends=["juana", "maria", "petra"]
for nombre in friends: 
    print(nombre)

#RANGE
for num in range(10): #range empieza en 0 y excluye 10
    print(num)

for friend in range(len(friends)):#por cada amigo en el rango de la longitud d friends
    print(friends[friend]) #imprime de friends[cada amigo]

for n in range(5):
    if n ==0:
        print("este es el primero")
    else:
        print("son los demas") 
#lo que hace es for es recorrer cada numero desde 0 al 4 y printear segun la instruccion 

def exp(n,e):
    result= 1 #aqui vamos a guardad el resultado de la multiplicacion
    for x in range(e): #por cada num hasta rango del exp
        result= result * n #multiplica n por si mismo o sea si estaba en 1 ahora va pasar a ser el num q ingresaste
    return result
#todo esto va a seguir hasta el num del exponente 

print(exp(2,3))

#MATRIZ
matriz= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for fila in matriz:
    for col in fila:
        print(col) #accedemos a cada valor dentro de las listas de la matriz

 
