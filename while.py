edad=(input(" cuantos años tiene "))

while not edad.isnumeric() or int(edad) < 0:
    edad =input("tiene que ser una edad real")
    break

edad=int(edad)

if edad < 4:
    print("Entras gratis")
elif edad <=18 and edad>=4:
    print("tienes que pagar 10 bucos")
else:
    print("son 14 pavos")

