"""
Enunciado del ejercicio:

En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
Color
Ruedas
Puertas

Por otro lado, crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
Velocidad
Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
"""


class Vehiculo:
    color = "rojo"
    ruedas = 4
    puertas = 5


class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 2.0

    def muestraAtributos(self):
        print("La velocidad del vehículo es ", self.velocidad, ", su cilindrada es: ",
              self.cilindrada, ", el color del coche es: ", self.color, ", tiene ", self.ruedas, " ruedas y ", self.puertas , " puertas")


miCoche = Coche()
miCoche.muestraAtributos()
