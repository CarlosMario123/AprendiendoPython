import csv

#ahora para leer
with open("archivo.csv","r") as archivo:
    reader = csv.reader(archivo)
    print("listarlo como arreglo")
    print(list(reader))
    #tambien podemos iterarlo
    archivo.seek(0)#para que el puntero se reinice
    print("listarlo con for")
    for texto in reader:
        print(texto)
    
    