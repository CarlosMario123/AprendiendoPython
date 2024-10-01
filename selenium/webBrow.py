import pyautogui
import pyperclip as pyc
import time
import webbrowser

# Mensaje a enviar
mensaje_inicial = "Hola, ¿cómo estás?"

# Abre WhatsApp Web en el navegador
webbrowser.open('https://web.whatsapp.com/send?phone=+529651214832')

# Espera a que WhatsApp Web se cargue
time.sleep(15)

# Envía el mensaje 100 veces
for i in range(50):
    pyc.copy(mensaje_inicial)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)

