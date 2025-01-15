print("Bienvenido, el día de hoy vamos a crear tu perfil de usuario")

#registro de los datos
nombre_usario= input("ingrese su nombre y apellido")

nombre_usario_mayus= nombre_usario.title()
if nombre_usario == nombre_usario_mayus:
    print(f" Un gusto en saludarte{nombre_usario_mayus}")
else:
        print("debes colocar tu nombre en mayuscula")


