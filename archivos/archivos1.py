from pathlib import Path
from time import ctime

archivos = Path("prueba.txt")

print(archivos.stat())
print("fecha de la creacion del archivo",ctime(archivos.stat().st_atime))