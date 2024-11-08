from estudiantes import ejemplo
from estudiantes import daniel
from estudiantes import keneth

if __name__ == '__main__':
    estudiante = ejemplo.Estudiante("Ejemplo", 00)
    estudiante.saludar()

    KENETH = keneth.Keneth("Keneth", 21)
    KENETH.saludar()
    
    DANIEL = daniel.Daniel("Daniel", 22)
    DANIEL.saludar()