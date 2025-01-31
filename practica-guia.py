#video de edd combinadas EJER 7.3-DECUENTOS
"""OUTPUT= Imprimir la factura del cliente (nombre, cédula, items comprados con su precio y
cantidad, y total a pagar después de aplicados los descuentos)."""

menu = {"Cachito": 4.00, "Empanada": 3.00, "Pasatelito": 3.50, "Sandwich": 2.50, "Pan tradicional (1 barra)": 1.00, \
        "Pan especial (1 barra)": 1.75, "Café": 1.25, "Jugo": 2.00, "Agua": 0.75, "Dulces (por kilo)": 6.00, "Galletas(por kilo)": 5.75, "Torta": 10.25}
#ESTA EN FROMA DE DICCIONARIO

cliente= {"Nombre":[] , "C.I":[], "Factura": [], "Compra": [], "Total": [], "Descuento": [], "Total con descuentos":[]} #Hacemos un diccionario con listas vacias para almacenar la info

while True: #como hay un while al final hay q poner un break
    print("\n1. Nueva factura\n2. Ver facturas\n3. Terminar")
    eleccion= input("ingrese un valor valido: ")
    while eleccion != "1" and eleccion != "2" and eleccion != "3":
        eleccion= input ("tiene que ser un valor valido: ")

    if eleccion == "1":
        nombre= input("ingrese su nombre:")
        while not (" ".join(nombre.split(" "))).isalpha(): #que coño hace esto #las comillas tienen q estar separadas
            nombre= input("ingrese un nombre valido")
        
        cedula= input("ingrese su c.i: ")
        while (not cedula.isnumeric()) or (int(cedula) < 1): #que coño hace esto
            cedula= input("ingrese c.i: ")

        factura = len(cliente["Nombre"]) + 1 #ESTO SIGNIFICA LA LEN SON CUANTOS NUMEROS HAY ENTONCES COMO M PIDEN EN NUMERO D FACTURA DEPENDIENDO DE CUANTOS NOMBRES HAY DA EL NUM Y ES MAS 1 PQ SIEMPRE EMPIEZA EN 0

        #LUEGO D REGISTRAR LOS DATOS LOS AÑADIMOS A LA LISTA DEL DICCIONARIO
        cliente["Nombre"].append(nombre.capitalize())
        cliente["C.I"].append(int(cedula))
        cliente["Factura"].append(factura)

        #pedido
        compras=[]
        total=0

        for num,producto in enumerate(menu):
            print(f"{num + 1}. {producto} cuesta {menu[producto]}")
        print("\n") #salto de linea
#LO DE ARRIBA VA A IMPRIMIR EL NUM ESO ES LO Q HACE EL ENUMERATE, ENUMERAR Y POR ESO TENEMOS Q ASIGNAR UN VALOR PARA EL NUM ANTES ENTONCES *1 
#(SE PONE +1 PQ NO QUEREMOS 0 CACHITO) MAS EL NOMBRE DE CADA PRODUCTO = CACHITO Y LUEGO 
#PARA ACCEDER AL PRECIO COMO ESTA DENTRO DE UN DICC LO LLAMAMOS CON KEY:VALUE ES DECIR EL NOMBRE DEL DICC: MENU LUEGO EN CORCHETES EL 
#NOMBRE DE CADA PRODUCTO QUE YA SE HIZO CON EL FOR Y ESO NOS VA A DAR EL VALUE DE CADA UNO
        while True:
            prod_num= input("Cual producto desea comprar")
            while (not prod_num.isnumeric()) or (int(prod_num) <1 ): 
                prod_num= input("un valor valido")

            cantidad= input("Cuanto desea comprar")
            while (not cantidad.isnumeric()) or (int(cantidad) <1 ): 
                cantidad= input("un valor valido")

            for num,producto in enumerate(menu):
                if int(prod_num) == num+1: #arriba se verifico que sea un num y ahora lo convertimos en uno para q pueda ser igual a num+1
                    prod= producto #o sea la variable qu estamos usando para ir al dicc
                    total_prod= menu[prod]* int(cantidad) #ahora ponemos prod pq lo igualamos al prod entonces eso nos va a dar el precio

            compras.append((prod, cantidad, menu[prod], total_prod)) #el append solo toma un item por eso hay q convertirlo en una tupla
            total += total_prod

            for i,cosas in enumerate(compras):
                print(f"- {cosas[0]}: {cosas[1]} x {cosas[2]} ") #esto muestra de la lista de compras el nombre de la cosas, pos=1, la cantidad y luego el precio 
                print(f"TOTAL: {total}")

            break
            


