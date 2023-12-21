import time
#importamos webdriver de selenium para realizar automatizaciones en el navegador
from selenium import webdriver
#importamos esto para estraer 
from selenium.webdriver.common.by import By
import requests

#mis importacion
from utils.afterPointString import obtener_subcadena_despues_de_punto_al_reves

#funcion para guardar imagen

def saveLocalFile(url,typeFile):
    name = f"archivo.{typeFile}"
    respuesta = requests.get(url)
    time.sleep(1)
    with open(f"imagenes/{name}", "wb") as archivo:
        archivo.write(respuesta.content)
        print("guardando archivo espere....")
        time.sleep(1)
        print(f"La imagen se ha guardado como '{name}'.")


#abriremos en firefox
driver = webdriver.Firefox()

driver.get("https://www.mercadolibre.com.mx/")

print("esperar....")
time.sleep(2)

# Encuentra el elemento img
elemento_img = driver.find_element(By.TAG_NAME,"img")

url_imagen = elemento_img.get_attribute("src")
print("src de imagenes")
print(url_imagen) 
#extraeremos su tipo de archivo(png,svg,png)
typeFile = obtener_subcadena_despues_de_punto_al_reves(url_imagen)
print(typeFile)
#guardamos la imagen a travez dela funcion
saveLocalFile(url_imagen,typeFile)

driver.quit()