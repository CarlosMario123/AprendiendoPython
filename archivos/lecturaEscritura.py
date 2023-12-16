from pathlib import Path

#lo que vamos hacer horita es leer un archivo
archivo = Path("./archivos/prueba.txt")
print("-------------------------------------------------------------------------------")
print(" contenido del texto")
print("-------------------------------------------------------------------------------")
print(archivo.read_text())

print("dividir texto por salto de linea")
archivoLine = archivo.read_text("utf-8").split("\n")
#al hacer eso convietio en un arreglo por parrafos
print(archivoLine)
print("---------------------------------------------------------------------------------------------")
#etidaremos el archivoLine
archivoLine.insert(0,"Texto añadido")

#editamos el archivo
#primer parametro el contenido en string segundo parametro el tipo de codificacion
archivo.write_text("\n".join(archivoLine),"utf-8")

#volvemos a leer
print("-------------------------------------------------------------------------------")
print("Archivo renombrado y nuevo contenido")
print("-------------------------------------------------------------------------------")
print(archivo.read_text("utf-8"))
