from datetime import datetime

def generar_nombre_archivo(identificador):
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()
    
    # Formatear la fecha y hora
    fecha_formateada = fecha_hora_actual.strftime("%Y%m%d")
    hora_formateada = fecha_hora_actual.strftime("%H%M%S")
    
    # Concatenar los elementos para crear el nombre del archivo
    nombre_archivo = f"{identificador}_{fecha_formateada}_{hora_formateada}"
    
    return nombre_archivo

# Ejemplo de uso
identificador = "archivo"
nombre_generado = generar_nombre_archivo(identificador)
print(nombre_generado)
