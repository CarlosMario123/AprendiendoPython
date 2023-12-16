"""
Los archivos CSV (Comma-Separated Values) son un formato de archivo utilizado 
para almacenar datos tabulares en forma de texto plano. En un archivo CSV, 
cada línea del archivo representa una fila de datos, y cada valor dentro de 
esa línea (fila) está separado por un delimitador, comúnmente una coma (,), 
aunque también se pueden utilizar otros delimitadores como punto y coma (;), 
tabulaciones u otros caracteres.
"""
import csv

#abriremos un archivo csv en modo escritura

with open("archivo.csv", "w", newline='') as archivo:
    writer = csv.writer(archivo)
    filas = [
        ["id", "nombre", "apellido"],
        [1, "carlos", "ruiz"],
        [2, "cesar", "ruiz"],
        [3, "checha", "ruiz"]
    ]
    writer.writerows(filas)
# Datos de la nueva fila a agregar

nueva_fila = [5, "jose2", "juan"]

# Abrir el archivo CSV en modo de adición ('a')
with open("archivo.csv", "a", newline='') as archivo:
     writer = csv.writer(archivo)
    # Escribir la nueva fila en el archivo
     writer.writerow(nueva_fila)    
    