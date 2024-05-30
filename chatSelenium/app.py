from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializar el navegador
driver = webdriver.Firefox()

# Abrir la página web
driver.get("https://chat.openai.com/")
time.sleep(3)

# Encontrar el cuadro de entrada de texto
findInput = driver.find_element(By.ID, "prompt-textarea")

# Esperar un momento para asegurar que la página se cargue completamente
time.sleep(1)

# Enviar un mensaje inicial
findInput.send_keys("puedes simular ser el scrum master de la empresa mad-code y nosotros te preguntaremos cosas del proyecto ")

# Esperar un momento antes de enviar el mensaje
time.sleep(1.5)

# Encontrar y hacer clic en el botón de enviar
btnSend = driver.find_element(By.XPATH, "//*[@data-testid='send-button']")
btnSend.click()

# Bucle infinito para enviar mensajes continuamente
print("********************************************************")
print("                 My scrum")
print("********************************************************")
while True:
    # Solicitar al usuario que ingrese un mensaje
    text = input("Escribe tu mensaje: ")

    # Esperar un momento antes de enviar el mensaje
    time.sleep(1.5)

    # Encontrar el cuadro de entrada de texto nuevamente
    findInput = driver.find_element(By.ID, "prompt-textarea")

    # Escribir el mensaje en el cuadro de entrada de texto
    findInput.send_keys(text)

    # Esperar un momento antes de enviar el mensaje
    time.sleep(1.5)

    # Encontrar y hacer clic en el botón de enviar nuevamente
    btnSend = driver.find_element(By.XPATH, "//*[@data-testid='send-button']")
    btnSend.click()

    # Esperar un momento para que aparezca el nuevo mensaje
    time.sleep(1.5)

    # Encontrar todos los elementos <p> que contienen los mensajes
    messages = driver.find_elements(By.TAG_NAME, "p")
    time.sleep(5)
    # Imprimir el texto del último mensaje
    if messages:
      print("Scrum: ",messages[len(messages) - 2].text)
      print("Scrum: ",messages[len(messages) - 1].text)

      

# Cerrar el navegador (esto nunca se ejecutará debido al bucle infinito)
driver.quit()
