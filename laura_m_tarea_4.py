print("Hola el día de hoy vamos a calcular los años bisiestos de 1900 a 2199 ")
año= (input("Indique el año de 1900 a 2199 "))
año_usario= int(año)

if año == año_usario:
    año_limite= int(1900)
    año_mayor= int(2199)
    n=0

    while año_usario>= año_limite and año_usario<= año_mayor:
        if año_usario%4 ==0:
            if año_usario%100 == 0 and año_usario%400 !=0:
                pass
            else:
                n+=1
        año_limite+=1

else:
    print("tiene que ser un año")