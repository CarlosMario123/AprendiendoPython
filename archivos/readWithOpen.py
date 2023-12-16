#ahora usaremos solo lectura usando open
from io import open

archivos = open("prueba.txt","r",encoding="utf-8")
texto = archivos.read()
archivos.close()
print(texto)


#una alternativa para no cerrar cada cosas podemos usar with
#ya nos olvidamos de usar close

with open("prueba.txt","r",encoding="utf-8") as archivo:
    print(archivo.readlines())#.readLines() lo da como arreglo
    #tambien podemos iterarlo de esta manera
    print("imprimiendo con un for")
    for linea in archivo:
        print(linea)


#agregar texto sin modificar lo demas con open
with open("prueba.txt","+a",encoding="utf-8") as archivo:
    archivo.write("otro hola mundo")