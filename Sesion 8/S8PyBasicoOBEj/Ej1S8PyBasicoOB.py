"""
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
lo abráis y escribáis dentro del archivo.
Para ello, tendréis que acceder dos veces al archivo creado.

"""

escritura = open("texto_Ej1_S8.txt","w")
lista= ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']

string="es un buen dia para estudiar Python\n"
domingo="¿Crees que por ser domingo vas a librar? Hoy te toca sesion doble de Python!!!\n"

for dia in lista:
    if dia != 'domingo':
        escritura.write(f"El {dia} {string}")
    else:
        escritura.write(domingo)

escritura.close()