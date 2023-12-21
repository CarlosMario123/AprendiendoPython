import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Driver:
    def __init__(self, url):
        # Creamos un driver adentro de Firefox
        self.driver = webdriver.Firefox()
        self.driver.get(url)
    
    # Método que trae las imágenes
    def get_imagenes(self):
        print("loading...")
        time.sleep(3)
        imagenes = self.driver.find_elements(By.CLASS_NAME, "promotion-item__img")
        urls = []
        for img in imagenes:
            urls.append(img.get_attribute("src"))
   
        return urls

        
        