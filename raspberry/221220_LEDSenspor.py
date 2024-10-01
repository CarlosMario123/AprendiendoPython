import tkinter as tk
import RPi.GPIO as GPIO
import time
import threading

# Definición de pines para el sensor y los LEDs
TRIG = 17
ECHO = 27
LED_PINS = [5, 6, 13, 19]  # Ajusta estos valores según tu configuración

label1 = None
label2 = None
label3 = None
label4 = None
cmText = None
hist = None
texto = ""
blink = False

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    for pin in LED_PINS:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

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

def create_round_label(parent, text):
    label = tk.Label(parent, text=text, bg='gray', fg='white', padx=10, pady=5)
    label.config(relief=tk.RAISED, borderwidth=1, width=15, height=2, anchor='center', font=('Arial', 12))
    return label

def main():
    global label1, label2, label3, label4, cmText, hist, texto
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
    
    # Crear un frame para el Text widget y el Scrollbar
    text_frame = tk.Frame(frame)
    text_frame.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
    
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    cmText = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, height=10, width=40)
    cmText.pack(side=tk.LEFT, fill=tk.BOTH)
    
    scrollbar.config(command=cmText.yview)
    
    sensor_thread = threading.Thread(target=leerSensor, name="SensorThread")
    sensor_thread.daemon = True
    sensor_thread.start()
    
    root.mainloop()

def leerSensor():
    global texto, blink, count
    
    while True:
        dist = distance()
        
        texto += f"Distancia: {dist:.1f} cm\n"
        print(f"Distancia: {dist:.1f} cm")
        
        count += 1
        if count >= 50:
            texto = ""
            count = 0
        
        cmText.delete(1.0, tk.END)  # Limpiar el Text widget
        cmText.insert(tk.END, texto)  # Insertar el texto actualizado
        
        if dist < 5:
            update_labels_and_leds(["gray"] * 4)
            blink = False
        elif 5 <= dist <= 10:
            update_labels_and_leds(["red", "gray", "gray", "gray"])
            blink = False
        elif 10 < dist <= 20:
            update_labels_and_leds(["red", "red", "gray", "gray"])
            blink = False
        elif 20 < dist <= 30:
            update_labels_and_leds(["red", "red", "red", "gray"])
            blink = False
        elif 30 <= dist <= 45:
            blink = True
            blink_labels()
        elif dist > 45:
            update_labels_and_leds(["red"] * 4)
            blink = False
        
        time.sleep(1)

def update_labels_and_leds(colors):
    global label1, label2, label3, label4
    labels = [label1, label2, label3, label4]
    for i, (label, color) in enumerate(zip(labels, colors)):
        label.config(bg=color)
        if color == "red" or color == "blue":
            GPIO.output(LED_PINS[i], GPIO.HIGH)
        else:
            GPIO.output(LED_PINS[i], GPIO.LOW)

def blink_labels():
    global blink
    
    for _ in range(4):
        update_labels_and_leds(["blue"] * 4)
        for pin in LED_PINS:
            GPIO.output(pin, GPIO.HIGH)  # Encender todos los LEDs
        time.sleep(0.2)
        update_labels_and_leds(["gray"] * 4)
        for pin in LED_PINS:
            GPIO.output(pin, GPIO.LOW)  # Apagar todos los LEDs
        time.sleep(0.2)

if _name_ == '_main_':
    try:
        count = 0
        setup()
        main()
    except KeyboardInterrupt:
        print("Medición detenida por el usuario")
        GPIO.cleanup()