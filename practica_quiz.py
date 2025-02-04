#LISTAS
#ejercico 3.1 guia

"""numero= input("ingrese un numero: ")
while (not numero.isnumeric()) or (int(numero)<1):
    numero= input("ingrese un numero entero positivo: ")

numero= int(numero)

while numero >= 10: #como 3 no es >= q 10 se salta el bloque y printea d una vez
    suma= 0 #creamos una variable donde vamos a almacenar los numeros
    for num in str(numero):
        suma += int(num)
    numero= suma #esto es por si n sigue siendo mayor q 10 y el ciclo siga iterando

print (numero)"""

#ejercicio 3.4
"""numero= input("ingrese un numero: ")
while (not numero.isnumeric()) or (int(numero)<1):
    numero= input("ingrese un numero entero positivo: ")
sucesion: []

for num in range(numero +1): #se pone numero+1 para q sea el numero ingresado sino lo deja hasta un numero antes
    if num == 0:
        sucesion.append(num)
    elif num == 1:
        sucesion.append(num)
    else:
        sucesion.append((num-1)+(num-2))

print(sucesion)"""

#NO FUNCIONA LO D ARRIBA

#ejercicio 3.5

"""n= input("ingrese un numero: ")

while not n.isnumeric():
    n= input("ingrese un numero: ")

n= int(n)

#si es primo/compuesto
primo=True

for numero in (2,n):
    if n%numero == 0:
        print("es compuesto")
        primo= False
        break

if primo:
    print("es primo")

#oblongo
for numero in (1,n):
    if numero*(numero +1)== n:
        print("es oblongo")
    else:
        print("no es oblongo")    
    break

#palindromo
n_str= str(n)

if n_str== n_str[::-1]:
    print("es palindromo")

#perfecto / abundante / deficiente

div =[]

for numero in range(1,n):
    if n%numero == 0:
        div.append(numero)

if sum(div)== n:
    print("es perfecto")
elif sum(div) > n:
    print("es abundante")
else:
    print("es deficiente")

# es libre de cuadrados o es cuadrado

cua= False
for numero in range(2,n):
    if numero**2== n:
        print("es cuadrado")
        cua=True
        break

if not cua:
    print("libre de cuadrados")"""

#TUPLAS Y SETS
