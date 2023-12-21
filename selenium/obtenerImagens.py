#hay errores todavia

import base64
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Directorio para guardar las imágenes
folder_path = 'directorio_donde_guardar_imagenes'

# Configurar opciones de Firefox
firefox_options = Options()
firefox_options.headless = True

# Configurar el servicio de GeckoDriver
gecko_driver_path = 'ruta_al_geckodriver'
service = Service(gecko_driver_path)

# Iniciar el controlador del navegador Firefox
driver = webdriver.Firefox(service=service, options=firefox_options)

# Abrir la URL
url = 'https://www.mercadolibre.com.mx/'  # Reemplaza esto con la URL correcta
driver.get(url)

# Encontrar elementos de imagen
imagenes = driver.find_elements(By.TAG_NAME, 'img')

# Crear el directorio si no existe
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Guardar imágenes en el directorio especificado
for i, imagen in enumerate(imagenes):
    src = imagen.get_attribute('src')
    if src and src.startswith('data:image'):
        # Imprimir la URL de la imagen para verificar
        print(f"Procesando imagen {i}: {src}")

        # Obtener la cadena base64 de la imagen y extraer la extensión del tipo de archivo
        _, base64_str = src.split(',', 1)
        ext = base64_str.split(';')[0].split('/')[-1]

        # Decodificar la cadena base64 y guardar la imagen con nombre descriptivo
        image_data = base64.b64decode(base64_str)
        file_path = os.path.join(folder_path, f'image_{i}.{ext}')
        with open(file_path, 'wb') as file:
            file.write(image_data)
            print(f"Imagen {i} guardada como '{file_path}'.")

# Cerrar el navegador al finalizar
driver.quit()
