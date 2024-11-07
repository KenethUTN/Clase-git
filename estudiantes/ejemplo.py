#estudiante

class Estudiante():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Nombre: " + self.nombre)
        print("Edad de :" self.nombre " : " + self.edad)
