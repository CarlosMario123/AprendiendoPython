import tkinter as tk
import RPi.GPIO as GPIO
import time
import threading

# Definición de los pines GPIO
TRIG = 17
ECHO = 27

# Variables globales para la interfaz
label1 = None
label2 = None
label3 = None
label4 = None
cmLabel = None
hist = None
texto = ""
blink = False

# configuración inicial
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

# Función para medir la distancia
def distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    start_time = time.time()
    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()
    
    elapsed_time = stop_time - start_time
    dist = (elapsed_time * 34300) / 2
    return dist

# Función para crear labels redondos
def create_round_label(parent, text):
    label = tk.Label(parent, text=text, bg='gray', fg='white', padx=10, pady=5)
    label.config(relief=tk.RAISED, borderwidth=1, width=15, height=2, anchor='center', font=('Arial', 12))
    return label

# Función principal para la interfaz gráfica
def main():
    global label1, label2, label3, label4, cmLabel, hist, texto
    root = tk.Tk()
    root.title("Simulador proximidad leds")
    
    frame = tk.Frame(root)
    frame.pack(pady=40)
    
    label1 = create_round_label(frame, "led")
    label1.grid(row=0, column=0, padx=10, pady=10)
    
    label2 = create_round_label(frame, "led")
    label2.grid(row=0, column=1, padx=10, pady=10)
    
    label3 = create_round_label(frame, "led")
    label3.grid(row=0, column=2, padx=10, pady=10)
    
    label4 = create_round_label(frame, "led")
    label4.grid(row=0, column=3, padx=10, pady=10)
    
    cmLabel = tk.Label(frame, text="Leyendo mensajes", bg='gray', padx=10, pady=10)
    cmLabel.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
    
    hist = tk.Label(frame, text="", bg='gray', padx=10, pady=10)
    hist.grid(row=3, column=1, padx=10, pady=10, columnspan=2)
    
    root.after(1000, leerSensor)
    root.mainloop()

# Función para leer el sensor y actualizar la interfaz
def leerSensor():
    global texto, blink,count
    
    dist = distance()
    
    texto += f"Distancia: {dist:.1f} cm\n"
    print(f"Distancia: {dist:.1f} cm")
    
    if count >= 50:
        texto = ""
    
    cmLabel.config(text=f"Distancia: {dist:.1f} cm")
    hist.config(text=texto)
    
    if dist < 5:
        update_labels(["gray"] * 4)
        blink = False
    elif 5 >= dist <= 10:
        update_labels(["red", "gray", "gray", "gray"])
        blink = False
    elif 10 > dist <= 20:
        update_labels(["red", "red", "gray", "gray"])
        blink = False
    elif 20 > dist and dist <= 30:
        update_labels(["red", "red", "red", "gray"])
        blink = False
    elif dist > 45:
        update_labels(["red"] * 4)
        blink = False
    
    elif 30 > dist and dist <= 45:
        blink = True
        blink_labels()
    
    # Llama a esta función nuevamente después de 1 segundo
    cmLabel.after(1000, leerSensor)

# Función para actualizar el color de los labels
def update_labels(colors):
    global label1, label2, label3, label4
    labels = [label1, label2, label3, label4]
    for label, color in zip(labels, colors):
        label.config(bg=color)

# Función para hacer que los labels parpadeen
def blink_labels():
    global blink
    
    for _ in range(4):
        update_labels(["blue"] * 4)
        time.sleep(0.2)
        update_labels(["gray"] * 4)
        time.sleep(0.2)
        
    
    

if __name__ == '__main__':
    try:
        count = 0
        setup()
        h1 = threading.Thread(target=main, name="hilo vista")
        h1.start()
    except KeyboardInterrupt:
        print("Medición detenida por el usuario")
        GPIO.cleanup()
