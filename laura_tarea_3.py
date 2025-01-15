#Definir la función de regiones
def region_fav(region):
    
    #hacemos un diccionario con listas donde se encuentren las opciones
    opciones={
        "italia":["pizza","pasta","roma"],
        "españa":["paella","musica","madrid"],
        "francia":["idioma","vino","paris"]
    }
    
    if region.lower() in opciones: #se establece .lower() para que sea igual a los nombres de los paises
        print(f"Yo también adoro {region.title()} ¿Qué te gusta más de ese lugar?")
        for opcion in opciones[region.lower()]: #opcion equivale a lo que esta dentro [] for e in hace que se revise cada una d ellas
            print(f"- {opcion}") #aqui muestran las palabras que pusimos dentro de la lista

        opcion_elegida= input("¿Cuál escoges? ") 
        if opcion_elegida in opciones[region.lower()]:
            print("Listo. Tu usuario ha sido creado ¡Muchas gracias!")
        else:
            print("Disculpa, esa opción no esta en la lista")
    else:
        print("Tienen que ser las regiones presentadas")

#saludo 
print("¡Bienvenido! Hoy crearemos tu usuario")
usuario=input("ingrese su nombre de usuario:")
usuario_mayus=usuario.title()

#colocar el usuario en mayuscula 
if usuario == usuario_mayus:
    print(f"{usuario_mayus}, es un placer tenerte en nuestro programa")

#se define el siguiente dato
    sexo= input("indique su sexo (F/M)").strip().upper()
    if sexo== "F":
        print(f"Bienvenida {usuario_mayus} faltan pocos pasos para que estes registrada")
        region_f= input("Necesitamos saber cuál de las siguientes regiones es tu preferida (Italia, Inglaterra, España):").strip().upper()
        
        region_fav(region_f) #ponemos region_f y no region pq region es como una x y region_f es el numero con la cual la sustituimos
    elif sexo== "M":
        print(f"Bienvenido {usuario_mayus} faltan pocos pasos para que estes registrado")
        region_f= input("Necesitamos saber cuál de las siguientes regiones es tu preferida (Italia, Inglaterra, España):").strip().upper()

        region_fav(region_f)
    else:
        print("Sexo no identificado. El programa no seguirá")
        exit() #se sale del programa queria poner systemexit pero no funcionaba 
else:
    print("Debe escribir su usuario con la primera inicial en mayúscula")