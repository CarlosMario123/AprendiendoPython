#en esta parte trabajaremos con json
import json
from pathlib import Path

#escribiremos el json

productos = [
    #tecnicamente es parecido a un diccionario
    {"id":1,"name":"bicicleta"},
    {"id":2,"name":"motocicleta"},
    {"id":3,"name":"automovil"},
    {"id":4,"name":"surfBoard"},
]

"""

json.dumps() es una función en Python que convierte 
un objeto Python (diccionario, lista, tupla, etc.) 
en una cadena de texto en formato JSON 
"""

data = json.dumps(productos)
#ahora creamos el un json con path
Path("archivos/archivo.json").write_text(data)

#ahora para leer 
datos = Path("archivos/archivo.json").read_text(encoding="utf-8")
#ahora pasamos de json a un diccionario con json.load
products = json.loads(datos)
print(productos)
#imprimir con for
for product in products:
    print(product) #prodemos imprimr el contenido por el objeto
    print(product["name"])#como es un dicionario podemos imprimir a travez de su llave para que nos de su valor

     
#modificar json
#queremos modificar automovil por un skate
#1-acedemos en que posicionn esta en ese caso en el 2-->1
#y utilizamo su clave valor a modificar
products[1]["name"] = "skate"

#volvemos a parsear a json
data = json.dumps(products)
#volvemos a escribir al archivo.json
Path("archivos/archivo.json").write_text(data)
#si queremo leer parseamos de json a diccionario
datos = Path("archivos/archivo.json").read_text(encoding="utf-8")
products = json.loads(datos)
#mostramos de nuevo
print("json modficado")
print(products)
