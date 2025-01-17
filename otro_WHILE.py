n = input("ingrese una cadena")
i=0 #indice

while i < len(n)/2: #len es la longitud
    if n [i] == n [-(i+1)]: #verifica que 1 a 1 los numeros o las letras sean iguales ejm: 101 
        i+=1
        continue
    else:
        break

if i == len(n)/2 or i > len(n)/2:
    print(" es palidromo")
else:
    print("no es")
