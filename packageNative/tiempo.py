from datetime import datetime
import time
import os

while True:
    fecha = datetime.now()
    hora_actual = fecha.strftime("%H:%M:%S")  # Formato: horas:minutos:segundos
    print("__________________________________________________________")
    print(hora_actual)    
    print("__________________________________________________________")
    time.sleep(1)
    os.system('cls')

    
    
