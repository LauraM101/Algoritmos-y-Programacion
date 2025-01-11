print("hola hoy vamos a calcular el volumen de una arepa en cucharaditas")

tazas_agua= input("ingrese la cantidad de tazas de agua:")
numero_agua= float(tazas_agua)
tazas_harina= input("ingrese la cantidad de tazas de harina PAN:")
numero_harina= float(tazas_harina)
cdtas_sal= input("ingrese la cantidad de cucharaditas de sal:")
numero_sal= float(cdtas_sal)
cdas_aceite= input("ingrese la cantida de cucharadas de aceite:")
numero_aceite= float(cdas_aceite)

#convertimos las unidades a cdtas

conversion_taza_cucharadita= float (48)
conversion_cda_cdta= float (3) 


cdtas_agua= numero_agua * conversion_taza_cucharadita #se utiliza el 48 por la multiplicación de 16 cdas (equivalente a 1 taza) * 3 cdtas
cdtas_harina= numero_harina * conversion_taza_cucharadita #tuve que borrar el 48 y hacer una nueva variable float para que funcione
cdta_aceite= numero_aceite * conversion_cda_cdta

volumen_inicial= float(cdtas_agua+cdtas_harina+cdta_aceite+numero_sal) #dios tenia mas este codigo como mil veces pq habia puesto cdtas sal en lugar de numero 

#Ahora se restamos 10% de la evaporación
volumen_respuestafinal= float (volumen_inicial * 0.10)  

print(f"El volumen de tu arepa después de la evaporación son {volumen_respuestafinal} cdtas") #hubo un error habia puesto los resultados como int pero no me di cuenta que el 10% era float asi q los tengo que cambiar 

#ahora el resultado no da dios mio da 10.0 pero deberia dar 30.0