#tuplas son para poner cordenadas(numeros imaginarios)
#son inmutables y ordernadas- se leen igual que las listas
ub= (10.499, -66.784)
print(ub[0]) #10.499

dimen= 20, 100, 90 #los parentesis son opcionales #sigue siendo una tupla no se pueden cambiar hay q definir una nueva
#dimen[0]= 21 no funciona no da (21, 100, 90) sino que hay que crear una nueva 
largo, ancho, alto= dimen #tuple unpacking es dividir el resultado(dimen) en variables
print("las dimensiones son {}, {}, {}".format(largo, ancho, alto)) #respuesta las dimensiones son 20x100x90 FORMAT es lo mismo que f al principio

#sets mutables y desordenadas LA IDEA ES QUE NO TENGA REPETIDOS
num={1, 2, 1, 1, 3, 4, 5, 4} #es un conjunto
print(num) #{1, 2, 3, 4, 5} elimina los repetidos y los ordena diferentes 

#para añadir un numero se usa la funcion .add()

#DICCIONARIOS= conjunto q contiene duplas
dic ={"hidrogeno": "1", "helio": 2, "carbon": 6}
print(dic["carbon"]) #para ir directamente a la seccion que quiero que me de lo que esta dentro de ella RESPUESTA=6

#tambien se puede 
dic_2 ={1: "hidrogeno", 2: "helio", 6: "carbon"} #para que los numeros tmb impriman el nombre 

#COLECCIONES 

