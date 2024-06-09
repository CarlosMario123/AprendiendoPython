import tkinter as tk
from gpiozero import Robot
from gpiozero.pins.pigpio import PiGPIOFactory
import serial.tools.list_ports
import pigpio
import threading


#221220
#223231
#223249
#223184

pin_factory = PiGPIOFactory()
robot = Robot(left=(17, 18), right=(22, 23), pin_factory=pin_factory)

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "Arduino" in p.description:
            return p.device
    return None

def read_serial(arduino_port):
    if not arduino_port:
        return
    
    try:
        ser = serial.Serial(arduino_port, 9600, timeout=1)
        while True:
            message = ser.readline().decode('utf-8').rstrip()
            if message:
                master.after(0, update_label, message)
    except serial.SerialException as e:
        print(f"Error al abrir el puerto serial: {e}")

def update_label(message):
    current_text = message_label.cget("text")
    new_text = current_text + "\n" + message
    message_label.config(text=new_text)

master = tk.Tk()
master.title("Robot UPChiapas")
master.geometry("600x300")

arduino_port = find_arduino_port()
port_label = tk.Label(master, text=f"Puerto Serial: {arduino_port if arduino_port else 'No se encontró ningún Arduino.'}")
port_label.grid(row=6, column=0, columnspan=4)

message_label = tk.Label(master, text="Mensajes recibidos del Arduino:")
message_label.grid(row=7, column=0, columnspan=4)

UPbutton = tk.Button(master, text="Adelante", bg="green", command=robot.forward)
UPbutton.grid(row=0, column=2)

DOWNbutton = tk.Button(master, text="Reversa", bg="green", command=robot.backward)
DOWNbutton.grid(row=3, column=2)

LEFTbutton = tk.Button(master, text="Izquierda", bg="green", command=robot.left)
LEFTbutton.grid(row=1, column=0)

RIGTHbutton = tk.Button(master, text="Derecha", bg="green", command=robot.right)
RIGTHbutton.grid(row=1, column=3)

STOPbutton = tk.Button(master, text="STOP", bg="green", command=robot.stop)
STOPbutton.grid(row=1, column=2)

Exitbutton = tk.Button(master, text="Exit", bg="red", command=master.destroy)
Exitbutton.grid(row=5, column=0)

if arduino_port:
    threading.Thread(target=read_serial, args=(arduino_port,), daemon=True).start()

master.mainloop()
