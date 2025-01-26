#python imprime los codigos en orden 
#VARIABLES EJM
#como hacemos para tener q cambiar jorge por otro nombre y la edad
nombre= "Juan" #esto se puede cambiar mas rapido que ir linea por linea y cambiarlo
edad= "35"
es_hombre= True #VALORES BULEANOS TRUE AND FALSE 

print(f"Habia una vez un hombre llamado {nombre}")
print(f"tenia {edad} años")

nombre= "pedro" #las variables se pueden cambiar y pueden quedar asignadas como en el principio y luego con otro nombre
print(f"le gustaba mucho su nombre: {nombre}") #le gustaba mucho su nombre: pedro
print(f"pero no le gustaba tener {edad}")

print("arepa\npanquecas") #\n es para ponerlos en dos lineas tipo como en asteriscos
#.isupper() o .islower() le preguntas a python si es str esta en mayus o minus y te da un valor buleano 
#.isnumeric() o 

#podemos saber la longitud de una variable o sea cuantos numeros o characteres tiene
print(len("arepas panquecas")) #RESPUESTA: 16 DA EL NUMERO D LETRAS Y CUENTA EL ESPACIO
print("arepa"[0]) #imprime la primera letra de la palabra TODO SIEMPRE EMPIEZA EN 0
#Si no sabemos donde esta un numero o letra en especifico podemos usar index 
print("arepa".index("p")) #respuesta: 3 pq contamos desde 0

#NUMEROS
print(pow(3,2)) #pow es elevado entonces primero pones el num y luego a cuanto lo quieres elevar 
x=9
print(pow(x,2)) #tmb se puede con variables

#todos los inputs deben ser archivados en una variable

#CREAR UNA CALCULADORA
# num_1= input("ingrese un num")
#num_2= input("ingrese otro")
# resultado= float(num_1) + float(num_2)
#print(resultado)

#LISTAS
numeros=[2, 3, 5, 8, 43, 25]
friends =["ivanna", "ivanna", "ivanna", "camilah", "chip", "maria", "elena"] 
print(friends) 
print(friends[1:])#imprimir los elementos de la lista apartir d uno
print(friends[1:3]) #imprime solo hasta chip pq es excluyente 

#FUNCTIONS
#para juntat dos listas ponemos .extend(y el nombre d la otra lista)
#friends.extend(numeros)
#print(friends) #['ivanna', 'camilah', 'chip', 'maria', 'elena', 2, 3, 5, 8, 43, 25]

#AÑADIR ELEMENTOS A UNA LISTA 
friends.append("juan") #se tiene q poner antes d print
print(friends)  #solo se añade al finañ

#para poner el nombre en un lugar especifico 
friends.insert(1, "sara") #ponemos el lugar y luego lo q vamos a añadir
print(friends)

#PARA ELIMINAR UN ELEMENTO
friends.remove("sara")
print(friends) #ya sara no esta en la lista

#RESETEAR LA LISTA
#friends.clear()
#print(friends) #se borro completamente

#PARA BORRAR EL ULTIMO ELEMENTO
friends.pop()
print(friends) # se borro juan que era el ultimo

#PARA CONTAR LOS ELEMENTOS IGUALES EN UNA LISTA 
print(friends.count("ivanna")) #da el numero d las veces que ibvanna esta repetido

#PARA PONERLO EN DE MENOR A MAYOR Y POR ORDEN ALFABETICO
numeros.sort()
print(numeros) #[2, 3, 5, 8, 25, 43]

#copiar listas
#friends_2= friends.copy()
#print(friends_2)

#FUNCIONES
#decir hola 
def decirola(): #todo lo q escribamos despues va a estar dentro d decirola
    print("hola user")
print("top")
decirola() #no es necesario poner print pq dentro del code se esta especificando
print("bottom") #cuando termina arriba pasa a la siguiente instruccion

def decirnombre(nombre, edad): #lo que esta dentro es lo que exije la funcion para que corra
    print(f"hola {nombre} y {edad}") #ves nombre funciona como una variable
#edad es otra variable
decirnombre("laura", 18) #aqui le indicamos lo que va a poner dentro de esa variable 
decirnombre("maria", 47) #imprime dos veces pq son dos variables distintas

#QUE COÑO ES EL RETURN AJA BASICAMENTE LA VAINA TE DICE UN ELEMENTO Q QUIERAS SABER COMO SALIO

def alcubo(numero):
    return pow(numero,3) #ahora va a devolver el resultado de la operacion
    
    #pow(numero,3) si lo pones asi con el return abajo
    #return numero esto va a devolver la variable no la operacion
#despues del return no se puede piner nada
#listo con el return ya no dice none

print(alcubo(3)) #DICE NONE NO IMPRIME EL RESULTADO

#CONDICIONALES PARA HACER TAREAS ESPECIFICAS SI ESTO HACES ESTO SI ES OTRA COSA HACES ESO
#COMO FUNCIONAN CON VALORES BULEANOS
#me despierto
#si tengo hambre #no sabes si esto es verdad o falso pero si es verdad desayuno si es falso skipeamos ese paso
    #entonces como 

#salgo de mi casa
#si esta lloviendo #si esto es verdadero se cumple 
    #entonces me llevo un paraguas
#sino #si la condicion es falsa ocurre otra cosa
    #entonces llevo lentes

#tengo hambre
#si quiero carne #si esto es V se cumple lo de abajo
    #entonces pido un bistec
#pero si quiero pasta #SI LO D ARRIBA ES F EXISTE OTRA CONDICION
    #entonces pido carbonara
#sino 
    #pido ensalada #si las dos d arriba son F pasamos a la ultima 

#####################################################################
es_masc= True #si esto lo cambiamos a F no va a hacer nada lo d abajo solo funciona con V
es_alto= True
#if es_masc or es_alto: #se va a imprimir pq ya estamos asumiento q es verdadero
    #print("hello mate") #or se cumple si 2 o 1 es verdadero
#else:
    #print("no eres")
    
if es_masc and es_alto: #este no funciona porque 1 es falso
    print("eres altisimo") #and ambos tienen que ser verdad
elif es_alto and not es_masc:
    print("ok eres alt@")
elif not es_alto and es_masc:
    print("shortking")
else: #si los dos son falsos 
        print("no eres ninguno") #ahora si es falso hace otra cosa

#COMPARAR
def max_num(num_1, num_2, num_3): #establecemos que queremos 3 nums
     if (num_1 >= num_2) and (num_1>= num_3): #los parentecis dan buleanos
          print(num_1)
     elif( num_2 >= num_1) and (num_2>= num_3):
          print (num_2)
     elif (num_3 >=num_1) and (num_3 >= num_2):
          print(num_3)
     else: #poruqe esto no funciona
          return("tienen que ser distintas cantidades")         
max_num(1, 10, 5)

#Calc mejorada
num_1= float(input("pon un numero: "))
op= input("di que quieres (+,-,/,*) : ")
num_2= float(input("pon un segundo numero: "))

if op == "+":
     print(num_1 + num_2)
elif op == "-":
     print(num_1-num_2)
elif op == "/":
     print (num_1 / num_2)
elif op == "*":
     print(num_1 * num_2)
else:
     print("esa opcion no esta ")