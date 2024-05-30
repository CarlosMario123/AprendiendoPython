from datetime import datetime, timedelta

# Obtener la fecha y hora actual
fecha_actual = datetime.now()

# Crear un timedelta de 5 días
intervalo = timedelta(days=5)

# Sumar el timedelta a la fecha actual para obtener una nueva fecha
nueva_fecha = fecha_actual + intervalo

print("Fecha actual:", fecha_actual)
print("Nueva fecha después de 5 días:", nueva_fecha)
