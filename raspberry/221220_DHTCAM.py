import numpy as np
import cv2
import RPi.GPIO as GPIO
import dht11
import time
import tkinter as tk
import threading
from PIL import Image, ImageTk
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
sensor = dht11.DHT11(pin=4)
cap=cv2.VideoCapture(0)
def showcamera():
     if not cap.isOpened():
         print("No se puede abrir la camara")
     while True:
          ret,frame=cap.read()
          cv2.imshow('camara',frame)
          if cv2.waitKey(1) & 0xFF == ord('x'):
               cap.release()
               cv2.destroyAllWindows()
               break
          


def funcleer():
  try:
    while True:
        result = sensor.read()
        if result.is_valid():
         
            listbox.insert(tk.END, "Temperatura: "+str(result.temperature)+"C")
            listbox.insert(tk.END, "Humedad: "+str(result.humidity)+"%")
            
        else:
            print("Error: {0}".format(result.error_code))
        time.sleep(4)
  except KeyboardInterrupt:
    print("Programa terminado")
  finally:
    GPIO.cleanup()
    return
    



     
def update_frame():
    try:
        if not cap.isOpened():
            print("No se puede abrir la camara")
        while True:
            ret, frame = cap.read()
           

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)
            frame_label.config(image=img)
            frame_label.image = img
    except KeyboardInterrupt:
        print("Programa terminado")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        return

master = tk.Tk()
master.title("Sensor de temperatura   UPChiapas")
master.geometry("600x300")
message_label = tk.Label(master, text="Mensajes recibidos del sensor de proximidad:")
frame_label = tk.Label(master)
frame_label.grid(row=0, column=0, rowspan=7)
listbox = tk.Listbox(master)
listbox.grid(row=8, column=0, columnspan=4)

message_label.grid(row=7, column=0, columnspan=4)
threading.Thread(target=update_frame).start()
threading.Thread(target=funcleer).start()
master.mainloop()