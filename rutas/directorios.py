from pathlib import Path#para trabajar con el path

path = Path("./rutas/carpeta")#asi creamos carpeta dentro de ruta
path.exists()
#path.mkdir()

for p in path.iterdir():#iterador de carpeta y archivos
    print(p)
    
    
print("Archivos encontradoss")    
for p in path.glob("*.txt"):
    print(p)    
    