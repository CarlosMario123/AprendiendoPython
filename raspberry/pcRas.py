import tkinter as tk
import cv2
import serial
import time
import struct

# Configurar la interfaz de tkinter
master = tk.Tk()
master.title("Emisor de Imágenes")

# Inicializar la cámara con OpenCV
cap = cv2.VideoCapture(0)

# Función para enviar imágenes a través del puerto serial
def send_image():
    # Configurar el puerto serial (ajustar el puerto según tu configuración)
    ser = serial.Serial('COM3', 9600, timeout=1)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                continue
            
            # Convertir la imagen a JPEG
            _, img_encoded = cv2.imencode('.jpg', frame)
            img_bytes = img_encoded.tobytes()

            # Enviar el tamaño de la imagen primero
            ser.write(struct.pack('>L', len(img_bytes)))

            # Enviar la imagen
            ser.write(img_bytes)

            # Mostrar la imagen en la interfaz de tkinter
            photo = tk.PhotoImage(data=img_encoded)
            label.config(image=photo)
            label.image = photo

            # Esperar un momento antes de enviar la siguiente imagen
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Programa interrumpido.")
    finally:
        cap.release()
        ser.close()

# Crear una etiqueta para mostrar la imagen en tkinter
label = tk.Label(master)
label.pack()

# Iniciar el envío de imágenes
send_image()

# Ejecutar el bucle principal de tkinter
master.mainloop()
