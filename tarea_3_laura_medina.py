print("Bienvenido, el día de hoy vamos a crear tu perfil de usuario")

#registro de los datos
nombre_usario= input("ingrese su nombre y apellido")
nombre_usario_mayus= nombre_usario.title()
if nombre_usario == nombre_usario_mayus:
    print(f"Un placer tenerte en nuestro programa,{nombre_usario_mayus}")
    sexo= input("Indique su sexo (F/M)").strip().upper()
    if sexo=="F":
         print(f"Bienvenida {nombre_usario_mayus}. Faltan pocos pasos para registrar tu usuario")
         region_fav= input("Necesitamos saber cual de las siguientes regiones es tu preferida (Italia, Inglaterra, España)")
         if region_fav== "italia":
             italia= input("Ciao carina. ¿Qué te gusta más? Pizza, Pasta o Roma") 
             if italia== ("pizza"or"pasta"or"roma"):
                 print("Listo. tu usario ha sido creado")
            else:
              print("Lo siento. Esa opción no está en la lista.")

    elif sexo=="M":
        print(f"Bienvenido {nombre_usario_mayus}. Faltan pocos pasos para registrar tu usuario")
    else: 
        print("Sexo no identificado. El programa se cerrará")
  
else:
    print("Debes ingresar tu nombre de usario con mayúsculas")

   
