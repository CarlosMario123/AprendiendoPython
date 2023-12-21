import base64

def save_base64_image(base64_string, file_name):
    # Separar la cadena base64 para obtener solo los datos de la imagen
    _, base64_image = base64_string.split(',', 1)
    
    # Decodificar la cadena base64 en datos binarios
    image_data = base64.b64decode(base64_image)
    
    # Escribir los datos binarios en un archivo
    with open(file_name, 'wb') as file:
        file.write(image_data)
        print(f'Imagen guardada como {file_name}')
    
    
save_base64_image("data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7","archivo.gif")   