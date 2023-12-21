#enseñanza del curso free code camp
import time
#importamos webdriver de selenium para realizar automatizaciones en el navegador
from selenium import webdriver
#importamos esto para estraer 
from selenium.webdriver.common.by import By
import requests
#como nos sirve google XD lo haremos en firefox
#abriremos en firefox
driver = webdriver.Firefox()
#usaremos driver ya que tenemos el contrlador geckodriver para firefox

#el metodo get del driver como nos dice nos permite traer informacion de una web
driver.get("https://www.facebook.com/")
driver.implicitly_wait(3)#esperamos a que cargue 3 segundos
""" 
el metodo finElement() del driver que proviene del web driver nos sirve para extraer un elemento
de esa web como podemos ver tiene doos parametros el primer parametro expecificamos que quiere que busque
en este caso se esta buscando por id per para realizar eso estamo realizando unas importaciones importamos esto
from selenium.webdriver.common.by import By ya que tenemos esto utilizado el atributo id del objeto By.
okey siguiendo con la funcion el segundo parametro del metodo driver agregamos el id toda esta funcion si lo 
encuentra nos retorna un elemento html que podemos interactuar como clickear etc
"""



"""
en facebook pasa algo raro es que el button de login siempre 
cambia su id 
por eso lo comentamos jajsjsj
#elemento = driver.find_element(By.ID,"u_0_5_tw")
"""
print("esperar....")
time.sleep(2)
elemento = driver.find_element(By.LINK_TEXT,"Crear cuenta nueva")
elemento.click()
print(elemento)

print("okey ahora traremos los tiulos de la pagina")
elementos = driver.find_elements(By.TAG_NAME,"div")

#imprimiremos el contenido de los elementos
for e in elementos:
    print(e.text)#con text traermos los textos de los elementos
    
#traeremos la imagen
# Encuentra el elemento img
elemento_img = driver.find_element(By.TAG_NAME,"img")

# Obtiene la URL de la imagen
url_imagen = elemento_img.get_attribute("src")
print(url_imagen) 
respuesta = requests.get(url_imagen)
name = "im"
# Guarda la imagen descargada en un archivo local

with open("imagenes/archivo.svg", "wb") as archivo:
    archivo.write(respuesta.content)
    print("guardando archivo espere....")
    time.sleep(1)
    print(f"La imagen se ha guardado como '{name}'.")

# Cierra el navegador al finalizar
driver.quit()