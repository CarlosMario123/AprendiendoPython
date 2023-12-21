import base64
from pathlib import Path

def replace_backslash_with_forwardslash(path):
    # Convertir el objeto Path a una cadena y reemplazar '\' por '/'
    updated_path = str(path).replace('\\', '/')
    return updated_path

def base64_to_image(base64_string, nameFile):
    # Decodificar la cadena base64
    image_data = base64.b64decode(base64_string)

    # Guardar la imagen decodificada en un archivo
    with open(nameFile, 'wb') as file:
        file.write(image_data)
        print(f"Imagen guardada como '{nameFile}'.")

path = Path("imagenes")

for p in path.iterdir():
    if p.is_file():  # Verificar si es un archivo
        with open(p, 'r') as file:
            sinSlash = replace_backslash_with_forwardslash(p)
            base64_data = file.read()  # Leer el contenido del archivo
            base64_to_image(base64_data, sinSlash)
