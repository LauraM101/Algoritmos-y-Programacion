"""nums = [2,7,11,15] 
ob=9
salida=[]
for x in range(len(nums)): #por cada numero 0 al 4= 4 siendo todos los numeros de la lista
    for n in range((x+1), len(nums)): #por cada numero de la posicion anterior al 4 que es la longitud
        if nums[x] + nums[n] == ob: #si el numero en la primera posicion mas el numero en la suegunda dan ob
            salida.append(x) #añade solo la posicion a la lista 
            salida.append(n)
        
        break

print(salida)"""
   
"""nums = [1,2,3,1,1,3]
pares=0
for n in range(len(nums)):
    for y in range((n+1),len(nums)):
        while nums[n]== nums[y] and ([n]< [y]):
            pares+=1
            break
        
        
print(pares)"""

"""nums = [8,1,2,2,3]
menores= []

for n in range(len(nums)):
    cont= 0
    
    for y in range(len(nums)):
        if (n!=y) and (nums[y]< nums[n]):
            print(cont)
            cont += 1
    menores.append(cont)      
        
print(menores)"""

#############################################
#ejercicio #1 de la guia

"""saldo = 3480

print(f'2020/04/10 tu saldo inicial es de ${saldo}')
dinero_retirado = 96
saldo = saldo - dinero_retirado

print(f'Se han retirado ${dinero_retirado}')
print(f'2020/04/11 tu saldo actual es de ${saldo}')

saldo += 1200
print(f'2020/04/17 tu saldo actual es de ${saldo}')

saldo = saldo + (saldo * 0.03) # Suma el 3% de intereses
print(f'2020/04/30 tu saldo actual es de ${saldo}')

dinero_retirado = 51
saldo = saldo - dinero_retirado
print(f'Se han retirado ${dinero_retirado}')
print(f'2020/05/02 tu saldo actual es de ${saldo}')"""

#ejercicio 2 DICCIONARIOS 6.3
"""residentes = {"Julia Rodríguez": {"Edad": 21, "Género": "M", "Ocupación":"Estudiante"},\
    "Santiago López": {"Edad": 33, "Género": "H", "Ocupación":"Abogado"}, \
    "Luis González": {"Edad": 8, "Género": "H", "Ocupación":"Estudiante"}, \
    "Luisana González": {"Edad": 5, "Género": "M", "Ocupación":"Estudiante"},\
    "Martina Reverón de González": {"Edad": 37, "Género": "M","Ocupación": "Ingeniero"}, \
    "Sergio González": {"Edad": 37, "Género": "H","Ocupación": "Ingeniero"},\
    "Abel Araujo": {"Edad": 81, "Género": "H","Ocupación": "Médico"},\
    "Roberto Mendoza": {"Edad": 56, "Género": "H","Ocupación": "Profesor"},\
    "Bárbara Zapatero de Piñera": {"Edad": 32, "Género": "M", "Ocupación": "Psicólogo"},\
    "Leonardo Piñera": {"Edad": 31, "Género": "H","Ocupación": "Administrador"},\
    "Gustavo Álvarez": {"Edad": 14, "Género": "H","Ocupación": "Estudiante"},\
    "Guillermo Álvarez": {"Edad": 38, "Género": "H","Ocupación": "Médico"},\
    "Laura Paz de Álvarez": {"Edad": 38, "Género": "M","Ocupación": "Desempleado"},\
    "Ignacio Salcedo": {"Edad": 19, "Género": "H","Ocupación": "Estudiante"},\
    "Saúl Salcedo": {"Edad": 22, "Género": "H","Ocupación": "Estudiante"},\
    "Romina Salcedo": {"Edad": 25, "Género": "M","Ocupación": "Administrador"},\
    "Elena Pinto de Salcedo": {"Edad": 52,"Género": "M", "Ocupación": "Abogado"},\
    "Mauricio Salcedo": {"Edad": 52,"Género": "H", "Ocupación": "Ingeniero"},\
    "Tatiana Echeverría": {"Edad": 68,"Género": "M", "Ocupación": "Médico"},\
    'Marcelo Gonçalves': {"Edad": 27, "Género": "H", "Ocupación": "Administrador"},\
    "Jessica Franco de Gonçalves":{"Edad": 26, "Género": "M", "Ocupación": "Profesor"},\
    "Valerio Fiore": {"Edad": 97, "Género": "H", "Ocupación": "Desempleado"},\
    "Giuliana Rossi de Fiore": {"Edad": 95, "Género": "M", "Ocupación": "Desempleado"},\
    "José Castro": {"Edad": 35, "Género": "H", "Ocupación": "Abogado"},\
    "Samantha Correa de Castro": {"Edad": 35, "Género": "M", "Ocupación": "Abogado"},\
    "Ángel Castro": {"Edad": 7, "Género": "H", "Ocupación": "Estudiante"},\
    "Antonieta Marín": {"Edad": 58, "Género": "M", "Ocupación": "Profesor"},\
    "Lorenzo Blanco": {"Edad": 77, "Género": "H", "Ocupación": "Abogado"},\
    "Vanessa Blanco de Bustamante": {"Edad": 37, "Género": "M", "Ocupación": "Médico"},\
    "Raúl Bustamante": {"Edad": 39, "Género": "H", "Ocupación": "Médico"},\
    "Carolina Alcalá": {"Edad": 24, "Género": "M", "Ocupación": "Ingeniero"},\
    "Juan Alcalá": {"Edad": 60, "Género": "H", "Ocupación": "Psicólogo"},\
    "Ingrid Gil de Alcalá": {"Edad": 60, "Género": "M", "Ocupación": "Profesor"},\
    "Francesca Costa de Gil": {"Edad": 88, "Género": "M", "Ocupación": "Médico"},\
    "Giancarlo Gil": {'Edad': 89, "Género": "H", "Ocupación": "Psicólogo"}, "César Lovera":
{"Edad": 64, "Género": "H", "Ocupación": "Administrador"}, "Natalia Lovera":
{"Edad": 64, "Género": "M", "Ocupación": "Desempleado"}}

print(f"TOTAL RESIDENTES:{len(residentes)}")

edades_hombres =[]
prom_H_age=0
age_M=[]
prom_M_age=0
edades=[]
for persona, datos in residentes.items(): #permite acceder a los minis diccionarios 
    if datos["Género"] == "M":
        age_M.append(datos["Edad"])
        edades.append(datos["Edad"])
    if datos["Género"] == "H":
        edades_hombres.append(datos["Edad"])
        edades.append(datos["Edad"])
prom_H_age= sum(edades_hombres)// len(edades_hombres)
prom_M_age= sum(age_M)// len(age_M)
print(f"HOMBRES PROMEDIO: {prom_H_age}")
print(f"MUJERES PROMEDIO: {prom_M_age}")


for persona, datos in residentes.items():
    if datos["Edad"] ==min(edades):
        print(f"PERSONA MAS JOVEN: {persona} tiene {datos["Edad"]} años")

for persona, datos in residentes.items():
    if datos["Edad"]== max(edades):
        print(f"PERSONA MAS VIEJA: {persona} tiene {datos["Edad"]} años")

medicos=0
profesores=0
ingenieros=0
administradores=0
psicologos=0
abogados=0
desempleados=0
estudiantes=0

for persona, datos in residentes.items():
    if datos["Ocupación"]== "Médico":
        medicos+=1
    elif datos["Ocupación"]== "Profesor":
        profesores+=1
    elif datos["Ocupación"]== "Ingeniero":
        ingenieros+=1
    elif datos["Ocupación"]== "Administrador":
        administradores+=1
    elif datos["Ocupación"]== "Psicólogo":
        psicologos+=1
    elif datos["Ocupación"]== "Abogado":
        abogados+=1
    elif datos["Ocupación"]== "Desempleado":
        desempleados+=1
    else:
        estudiantes+=1

print(f"CANTIDAD SEGUN OCUPACION: \n medicos: {medicos} \n profesor: {profesores} \n ingeniero: {ingenieros}\
     \n administrador: {administradores} \n psicologos: {psicologos} \n abogado: {abogados} \n desempleados: {desempleados} \n estudiantes: {estudiantes}")"""

#ejercicio FACTURAS 6.7

"""facturas ={}
cobrado=0
pendiente =0

while True:
    print("Bienvenido:\n1 Nueva Factura \n2 Pagar Factura \n3 Terminar")
    opcion= input("INGRESE EL NUMERO de su operacion: ")
    while (not opcion.isnumeric()) or (not int(opcion)in range(1,4)):
       opcion= input("INGRESE EL NUMERO QUE SE MOSTRO EN PANTALLA de su operacion: ") 
    
    if opcion == "1":
        num= input("ingrese el num d factura: ")
        if num in facturas.keys():
            print(f"{num} ya se encuentra registrado y su monto es {facturas[num]}")
        else:
            monto= input("Ingrese cuanto cuesta su factura: ")
            while (not monto.isnumeric()) or (int(monto) < 0):
                monto= input("Ingrese cuanto cuesta de verdad su factura: ")
            
            facturas[num]= float(monto) #ASI SE AGREGA UN KEY Y UN VALUE A UN DICCIONARIO
            pendiente += float(monto)
    elif opcion == "2":
        num= input("ingrese el num d factura: ")
        if num not in facturas.keys():
            print(f" {num} no esta registrado")
        else:
            pendiente -= facturas[num]
            cobrado += facturas [num]
            facturas.pop(num)
    else:
        break
    print(f" cobrado:{cobrado} y pendiente: {pendiente}")"""

#ejercicio ai
"""Vamos a crear una agenda de contactos donde:

Puedas agregar contactos con su nombre, edad y ciudad
Ver todos los contactos
Agregar más información a un contacto existente"""

"""agenda_contactos={}
while True:
    print("Bienvenido:\n1 Agregar contacto \n2 Contacto existente \n SALIR")
    opcion= input("INDIQUE LA OPCION: ")
    while (not opcion.isnumeric()) or (int(opcion) not in range (1,4)):
        opcion= input("INDIQUE LA OPCION: ")
    if opcion =="1":
        nombre= input("Ingrese su nombre: ")
        edad= input("ingrese su edad: ")
        while (not edad.isnumeric()) or (int(edad) <0):
            edad= input("ingrese su verdadera edad: ")
        ciudad= input("ingrese su ciudad: ")
        
        agenda_contactos[nombre]= {"edad":edad, "ciudad": ciudad}
        print("contacto registrado")
        
    elif opcion =="2":
        if agenda_contactos:
            for nombre,dato in agenda_contactos.items():
                print(f"DATOS DE {nombre} \n EDAD: {dato["edad"]} \n CIUDAD: {dato["ciudad"]}")
    
    else:
        break"""

##########################################################
#Ejercicios de la guia
#2.5 UPPER & LOWER

"""palabra= input("Ingrese una palabra: ")
vocales= ["a", "e", "i", "o", "u"]
resultado=""
for p in palabra:
    if p.lower() in vocales:
        palabra=palabra.replace(p, p.upper())

print(palabra)"""

#2.7 CÁLCULO DE ÁREAS

"""
print("QUE FORMA DESEA CALCULAR: \n1 Circulo \n2 Cuadrado \n3 Triangulo")

forma= input("Ingrese el numero deseado: ")
while(not forma.isnumeric()) or (int(forma)< 1):
    forma= input("Ingrese el numero deseado: ")

if forma == "1":
    print("Para calc el area se necesita\n1 radio \n2 diametro")
    resp= input("selecione cual tiene: ")
    while(not forma.isnumeric()) or (int(forma)< 1):
        resp= input("Ingrese el numero de cual tiene: ")
    pi= 3.14
    if resp=="1":
        r= input("Cual es el radio: ")
        r= float(r)
        area= pi*pow(r,2)
        print(f"su area es de {area}")
    else:
        d= input("ingrese el diametro:")
        d= float(d)
        area= pi*pow(d/2,2)
        print(f"su area es de {area}")

elif forma == "2":
    l= input("Ingrese uno de los lados del cuadrado: ")
    l= float(l)
    area= pow(l,2)
    print(f"su area es de {area}")

else:
    b= float(input("Ingrese la base del triangulo: "))
    h= float(input("Ingrese la altura: "))
    area= b*h/2
    print(f"su area es de {area}")"""

#2.12 CINE
#ademas calcular la cantidade de entradas si el numero es par/impar 
"""
edad= input("Ingrese su edad: ")
cantidad= 0
costo=0

while (not edad.isnumeric()) or (int(edad)<1):
    edad= input("Ingrese su edad: ")

edad= int(edad)
if edad <= 4:
    print(f"la entrada es gratis su monto a pagar es {costo}")

elif edad >4 and edad<= 18:
    print("Debe pagar 10$")
    cantidad= int(input("Cuantas entradas quiere: "))
    costo= 10*cantidad
    print(f"El monto a pagar es: {costo}")

    if costo%2 == 0:
        print("te ganaste un caramelo")
    else:
        print("es triste")

elif edad > 18 and edad <100:
    print("Debe pagar 14$")
    cantidad= int(input("Cuantas entradas quiere: "))
    costo= 14*cantidad
    print(f"El monto a pagar es: {costo}")
    
    if costo%2 == 0:
        print("te ganaste un caramelo")
    else:
        print("es triste")"""

#3.1 SUMA DE DÍGITOS 

"""num= input("Ingrese un numero: ")
suma= 0
while (not num.isnumeric) or (int(num) < 1):
    num= input("Ingrese un numero entero positivo: ")
num= int(num)

while num >= 10:
    for n in str(num):
        suma += int(n)
        num= suma
print(num)"""

#CONTADOR DE SÍLABAS
"""contador=0
x = "Outside of that, Hu argues that the royalties can be more reliable than\
the entropy of Wall Street. No matter what happens to the stock market, people\
are always going to be listening to music."

palabra= x.split()
for p in palabra:
    if "at" in p: 
        contador +=1

print(f"at se repite {contador} veces")""" #lo de los indices no supe hacerlo


#3.3 DADOS
"""num= input("ingrese un numero del 2 al 12: ")


while(not num.isnumeric()) or (int(num) < 2):
    num= input("ingrese un numero del 2 al 12: ")

num=int(num)

for n in range(1,(num//2)+1):
    n_2= num-n
    if n_2 < 12:
        print(n,n_2)"""

#3.7 Factoriales
"""x= input("Ingrese un numero:")

while (not x.isnumeric) or (int(x)<1):
  x= input("Ingrese un numero:")

x=int(x)
factorial= 1

for n in range(1,x+1):
    factorial = factorial*n
    
print(factorial) """ 

#3.10 NÚMEROS DE DÍGITOS INCREMENTALES 
x= input("ingrese un numero de 3 digitos: ")
lista=[]

while (not x.isnumeric()) or (int(x)<100):
    x= input("ingrese un numero de 3 digitos: ")

lista.append(x)
lista.sort()
for n in lista:
    if n ==n:
        lista.pop(int(n))
    print(lista)

    
    



        

    

