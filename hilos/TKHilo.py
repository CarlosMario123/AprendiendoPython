#En esta pequeña practica usaremos hilos junto con tkinter para
#ver el uso de timer de threading

import tkinter as tk
import threading 

#crearemos una funcion que sera para ejecutar nuestro hilo que cambiare el nombr del label

def changeLabel(label):
    label.config(text="EL hilo se ha ejecutado")
    
    

window = tk.Tk()
window.title("Hola Mundo")


label = tk.Label(window, text="Hola Mundo!")
temporizador = threading.Timer(5, function=changeLabel,args=(label,))
temporizador.start()

label.pack(side=tk.TOP, anchor=tk.CENTER, padx=20, pady=20)


window.mainloop()
