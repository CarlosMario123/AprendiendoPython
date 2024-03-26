from selenium import webdriver
from selenium.webdriver.common.by import By#esto importante nos permitira trabajar con los selectores
driver = webdriver.Firefox()
import time
driver.get("https://www.facebook.com/")


#vamos buscar usando xpath
#primer paramatro el selector a trabajar el segundo es el valor

user = driver.find_element(By.XPATH,"//input[@id='email']")#lo que vamos hacer aca es buscar un input con firstName
user.send_keys("Correo")#aca llenaremos eso
passw = driver.find_element(By.XPATH, "//input[@id='pass']")

time.sleep(1)
passw.send_keys("password")
time.sleep(2)
driver.find_element(By.NAME, "login").click()
time.sleep(4)

#codigo para extraer url de imagenes
img_elements = driver.find_elements(By.XPATH, "//img")
img_urls = [img.get_attribute("src") for img in img_elements]

# Imprimir las URL de las imágenes
for url in img_urls:
    print(url)
    print()
    
driver.close()