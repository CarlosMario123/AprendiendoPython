import csv

newFila = [6,"pan","crema"]
#cuando deseamos añadir al final de la tabla
with open("archivo.csv", "a", newline='') as archivo:
    writer = csv.writer(archivo)
    # Escribir la nueva fila en el archivo
    writer.writerow(newFila)    