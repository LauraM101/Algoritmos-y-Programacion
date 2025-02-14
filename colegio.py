from prepa import Alumno

class Colegio():
    def __init__(self):
        self.alumnos= []

    def showalumnos(self):
        for s in self.alumnos:
            print(s.show())

    def top5(self):
        return

    def showpromedio(self):
        suma=0
        for n in self.alumnos:
            suma += n.promedio
        prom= suma/ len(self.alumnos)
        print(f"promedio es {prom}")

    def showaprobados(self):
        aprob1= []
        aprob2= []
        reprobados= []

        for s in self.alunmos:
            if s.promedio <= 20 and s.promedio >= 16:
                aprob1.append(s)

            elif s.promedio < 16 and s.promedio >= 10:
                aprob2.append(s)

            else:
                reprobados.append(s)

        print(f"aprobados d 16 a 20= {len(aprob1)}\
              aprobados d 10 a 15= {len(aprob2)}\
                reprobados= {len(reprobados)}")

    def register(self):
        name= input("ingrese el nombre ")
        grado= input("ingrese el grado ")
        promedio= input("ingrese el promedio ")
        direccion= input("ingrese la direccion ")
        representante= input("ingrese el representante ")
        tlf= input("ingrese el numero ")
        new= Alumno(name, grado, int(promedio), direccion, representante, tlf)
        self.alumnos.append(new)
    
    def mainMenu(self):
        while True:
            op= ["mostrar informacion de los alumnos", "mostrar top 5", "mostrar promedio colegio", "mostrar alumno aprobados", "salir"]
            
            for i in range(len(op)):
                print(f"{i+1} - {op[i]}")

            x = input("Ingrese el num d la op")

            if x == "1":
                self.showalumnos()

            elif x== "2":
                self.top5()
            
            elif x== "3":
                self.showpromedio()

            elif x== "4":
                self.showaprobados()
            else:
                break