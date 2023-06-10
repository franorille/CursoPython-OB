import time

# Obtiene la fecha y hora actual
fecha_actual = time.strftime("%d/%m/%Y")
hora_actual = time.strftime("%H:%M:%S")

# Obtiene la hora actual en formato de 24 horas
hora = int(time.strftime("%H"))
minutos = int(time.strftime("%M"))

if hora >= 19:
    print("Es hora de ir a casa.")
else:
    # Calcula el tiempo restante de trabajo
    if (19-hora)==1:
        tiempo_restante = 60 - minutos # Convierte las horas restantes a minutos
    else:
        tiempo_restante = ((23 - hora) * 60) + (60 - minutos)
    print(f"Aún quedan {tiempo_restante} minutos de trabajo.")

print("Fecha actual:", fecha_actual)
print("Hora actual:", hora_actual)