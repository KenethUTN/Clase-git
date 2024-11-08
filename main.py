from estudiantes import ejemplo
from estudiantes import paula
from estudiantes import keneth

if __name__ == '__main__':
    estudiante = ejemplo.Estudiante("Ejemplo", 00)
    estudiante.saludar()
    
    KENETH= keneth.Keneth("keneth", 21)
    KENETH.saludar() 
    
    PAULA = paula.paula("Paula", 21)
    PAULA.saludar()