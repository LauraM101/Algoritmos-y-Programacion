class Alumno():
    def __init__(self, name, grado, promedio, direccion, representante, tlf):
        self.name= name
        self.grado= grado
        self.promedio= promedio
        self.direccion= direccion
        self.representante= representante
        self.tlf= tlf
        self.beca = self.esBecado()

    def esBecado(self):
        return self.promedio>= 18
    
    def show(self):
        return f"""\n1 {self.name} \n2 {self.grado} \n3 {self.promedio} \n4 {self.direccion} \n5 {self.representante} \n6 {self.tlf} \n7 {self.beca}"""