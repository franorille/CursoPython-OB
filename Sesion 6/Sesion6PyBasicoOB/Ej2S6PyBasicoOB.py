"""
Enunciado del ejercicio:

En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.


"""

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota



    def datosAlumno(self):
        aprobado = ""
        if self.nota < 5:
            aprobado = " suspenso."

        else:
            aprobado = " aprobado."

        print("El nombre del alumno es",self.nombre,",ha obtenido una nota de", self.nota,",por lo que está",aprobado)

alumno1 = Alumno("Francisco",10)
print(alumno1.datosAlumno())

