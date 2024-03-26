from selenium import webdriver
from selenium.webdriver.common.by import By#esto importante nos permitira trabajar con los selectores
driver = webdriver.Firefox()
import time
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
time.sleep(2)

#vamos buscar usando xpath
#primer paramatro el selector a trabajar el segundo es el valor

nom = driver.find_element(By.XPATH,"//input[contains(@id,'firstName')]")#lo que vamos hacer aca es buscar un input con firstName
nom.send_keys("cato")#aca llenaremos eso
apellido = driver.find_element(By.XPATH,"//input[contains(@id,'lastName')]")
time.sleep(1)
apellido.send_keys("Maro")
time.sleep(2)
#ahora daremos click a un boton
driver.find_element(By.XPATH,"//button[contains(@id,'submit')]").click()
#js en selenium 
# Ejecutar código JavaScript para generar un alert
driver.execute_script("alert('¡Hola desde Selenium!');")
time.sleep(4)
driver.close()