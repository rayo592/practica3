class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No asignada")
        if self.notas:
            print("Notas:", self.notas)
        else:
            print("Notas: No asignadas")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.notas.append(nota)


# Creamos un objeto de la clase Alumno
alumno1 = Alumno("Marcelo", 201202)

alumno1.display()

alumno1.setAge(19)

alumno1.setNota(11)
alumno1.setNota(13)
alumno1.setNota(20)

alumno1.display()