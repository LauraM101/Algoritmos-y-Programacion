print("Hola el día de hoy vamos a calcular los años bisiestos de 1900 a 2199 ")
año= input("Indique el año de 1900 a 2199 ")

while not año.isnumeric() or int(año) < 0:
    año= input("tiene que ser un año de 1900 a 2199")
    
año= int(año) 

while not 1900 <= año <=2199 :
    año= input("este año no se encuentra en el rango. Ingrese de nuevo el número: ")

    año= int(año)
    año_limite= int(1900)
    año_mayor= int(2199)
    n=0

    while año_limite <= año <= año_mayor:
        if año_limite%4 ==0:
            if año_limite%100 == 0 and año_limite%400 !=0:
                pass
            else:
                 n+=1
        año_limite+=1
    print(f"estos son los años bisiesto: {n}")


