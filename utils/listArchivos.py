from pathlib import Path
def reemplazar_backslash_por_slash(cadena):
    # Utilizamos el método replace() para reemplazar '\'
    cadena_actualizada = cadena.replace('\\', '/')
    return cadena_actualizada

# Ejemplo de uso
ruta = input("Pegue su ruta absoluta: ")
ruta = reemplazar_backslash_por_slash(ruta)

print("desea agregar un tipo de extension")
print("1-si")
print("otro-No, pero listara todo los archivos")
bandera = input("selecione una opcion: \n")
extension = "*"

if(bandera == "1"):
    extension = input("seleciione un tipo de extension: ")




ruta_absoluta = Path(ruta)

# Verificar si la ruta existe y es un directorio
if ruta_absoluta.is_dir():
    # Listar todos los archivos y directorios en la ruta absoluta
    for archivo in ruta_absoluta.rglob(f"*.{extension}"):
        print(archivo.name)
else:
    print("La ruta no es un directorio válido.")