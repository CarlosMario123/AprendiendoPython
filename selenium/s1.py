from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Ruta al ejecutable geckodriver (asegúrate de que esté instalado y accesible)
gecko_driver_path = 'geckodriver'

# Opciones para ejecutar Firefox en modo sin cabeza
firefox_options = Options()
firefox_options.headless = True  # Ejecutar en modo sin cabeza

# Configurar el servicio de geckodriver
service = Service(gecko_driver_path)

# Iniciar el controlador del navegador Firefox
driver = webdriver.Firefox(service=service, options=firefox_options)

# Abrir una URL
url = 'https://www.mercadolibre.com.mx/'
driver.get(url)

# Ejemplo: encontrar un elemento en la página y extraer su texto
elemento = driver.find_element(By.TAG_NAME, 'h2')
print("Texto del elemento:", elemento.text)

# Cerrar el navegador al finalizar
driver.quit()

