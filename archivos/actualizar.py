import csv
import os

def actualizar():
    with open("archivo.csv", "r") as r, open("archivoTemp.csv", "w", newline='') as w:
        reader = csv.reader(r)
        writer = csv.writer(w)
        filas_escritas = 0  # Contador de filas escritas
        total_filas = sum(1 for _ in reader)  # Número total de filas en el archivo original
        r.seek(0)  # Reiniciar el lector a la posición inicial

        for indice, linea in enumerate(reader, 1):
            if linea[0] == '3':  # Corregir la comparación para que sea una cadena
                writer.writerow(['3', "paco", "tilla"])
                filas_escritas += 1
            elif any(field.strip() for field in linea if field):  # Verificar si la fila tiene algún contenido
                writer.writerow(linea)
                filas_escritas += 1

            # Evitar escribir una fila en blanco al final si la última fila es una fila en blanco
            if filas_escritas < total_filas and indice == total_filas:
                w.truncate(w.tell())  # Eliminar la última fila en blanco si existe

    # Después de hacer los cambios, eliminamos y renombramos los archivos
    os.remove("archivo.csv")
    os.rename("archivoTemp.csv", "archivo.csv")

# Ejecutamos nuestra función
actualizar()

    
    
#ejecutamos toda nuestras funciones
actualizar()        

#leeremos lo que hay en el csv
with open("archivo.csv","r",newline="") as archivos:
    lector = csv.reader(archivos)
    for linea in lector:
        print(linea)        

    

    

           
       
    