#aca aprenderemos a comprimir archivos
#principalmente usamos path para asiganar una ubicacion en nuestros archivos
from pathlib import Path
#para hacer la compresion utilizamos zipfile
from zipfile import ZipFile

#para trabajar con zipfile utilizamos with 
#dentro de la funcion zipfile(/ira la ruta del comprimido)


"""
listar path de los archivos que esten en la ruta especifica
for path in Path().iterdir():
    print(path)
"""
Path("archivos").mkdir(parents=True, exist_ok=True)
#arroja los los archivos disponible en archivos
for path in Path().rglob("*.*"):
    print(path)
print("ahora si trabajaremos con compresion")
with ZipFile("compri.zip","w") as zip:
    #agremos los archivos al zip del path con
    for path in Path().rglob("*.py"):
        print(path)
        if str(path) != "compri.zip":
             zip.write(path)

print("leer el zip ")

with ZipFile("compri.zip","r") as zip:
    for file in zip.namelist():
        print(file)    