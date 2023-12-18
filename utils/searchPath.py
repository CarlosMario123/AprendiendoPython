from pathlib import Path
import re  # Importar el módulo de expresiones regulares

def reemplazar_backslash_por_slash(cadena):
    # Utilizamos el método replace() para reemplazar '\'
    cadena_actualizada = cadena.replace('\\', '/')
    return cadena_actualizada

# Ejemplo de uso
ruta = input("Pegue su ruta absoluta: ")
ruta = reemplazar_backslash_por_slash(ruta)
print(ruta)
nombre_archivo_buscado = input("Ingrese el nombre del archivo a buscar (puede ser una expresión regular): ")

ruta_absoluta = Path(ruta)

# Verificar si la ruta existe y es un directorio
if ruta_absoluta.is_dir():
    # Listar todos los archivos y directorios en la ruta absoluta
    for archivo in ruta_absoluta.rglob("*"):
        # Verificar si el nombre del archivo coincide con el patrón de expresión regular
        if re.search(nombre_archivo_buscado, archivo.name):
            print(archivo.name)
else:
    print("La ruta no es un directorio válido.")
