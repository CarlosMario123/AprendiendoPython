from pathlib import Path#para trabajar con el path

#esto es cuando trabajamos en windows
#ponemos r para que no lo tome como escape los /
#Path(r"C:\ejemploDeRuta")

#ahora para linux
#Path("/users/bin")#--->ruta absoluta
#Path("one/__init__.py")#-->ruta relativa por si estamos en alguna carpeta

ruta = Path("./path-py.py")
if ruta.exists():#el metodo existe comprueba de que la ruta exista
    print("El archivo existe")
else:
    print("El archivo no existe")
    
print("ruta absoluta")
print(ruta.absolute()) #absolute devuelve la ruta absoluta del archivo

print("comprobar si es un directorio")
print(ruta.is_dir())  

print("comprobar si es un archivo")
print(ruta.is_file()) 

print("crearDirectorio")

print("listando los archivos.py del directorio carpeta")

#guardamos en una variable


#imprimimos los archivos que esta en la variable de encontrados


