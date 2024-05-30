import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Driver:
    def __init__(self, url):
        # Creamos un driver adentro de Firefox
        self.driver = webdriver.Firefox()
        self.driver.get(url)
    
    # Método que trae las imágenes
    def get_all_urls(self):
        print("Cargando...")
        # Espera para asegurar que se cargue completamente la página
        time.sleep(3)
        
        urls = []  # Inicializa la lista de URLs
        
        # Desplázate hacia abajo para cargar más imágenes hasta que ya no haya más
        while True:
            # Desplazamiento hacia abajo en la página
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Espera para que se carguen las imágenes adicionales
            time.sleep(2)
            # Busca nuevamente todas las imágenes en la página
            imagenes = self.driver.find_elements(By.TAG_NAME, "img")
            # Verifica si hay nuevas imágenes
            if len(imagenes) == len(urls):
                break
            # Actualiza la lista de URLs con las nuevas imágenes
            urls = [img.get_attribute("src") for img in imagenes]
        
        return urls


