"""
En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

"""
import pickle

class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo

    def __str__(self):
       return self.marca + " " + self.modelo


miVehiculo=Vehiculo("Honda","S2000")

serializar_objeto = open("objSerializadoEj2.bin","wb")
pickle.dump(miVehiculo,serializar_objeto)
serializar_objeto.close()

lectura_objeto = open("objSerializadoEj2.bin","rb")
objeto_deserializado= pickle.load(lectura_objeto)
print(type(objeto_deserializado))
print(objeto_deserializado)


