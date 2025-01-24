#sucesion de fibonacci
x= input("ingrese un numero")
sucesion = []

for i in range (x+1): #ra cada valor que vaya de 0 hasta el numero ingresado
if i == 0:
     sucesion.append(i) #append es incluirlo en la lista
elif i == 1:
    sucesion.append(i)
else:
     sucesion.append((i-1)+(i-2))

print(sucesion)
