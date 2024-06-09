import serial
import serial.tools.list_ports
import time

# 221220
# 223184
# 223249
# 223231

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "Arduino" in p.description:  # Busca una descripción que contenga "Arduino"
            return p.device
    return None

# Encuentra el puerto del Arduino
arduino_port = find_arduino_port()
if arduino_port is None:
    print("No se encontró ningún Arduino.")
else:
    print(f"Arduino encontrado en el puerto: {arduino_port}")
    
    # Configuración del puerto serial
    baudrate = 9600
    timeout = 1

    try:
        # Inicializa la conexión serial
        serie = serial.Serial(arduino_port, baudrate, timeout=timeout)
        time.sleep(2)  # Espera a que el puerto serial esté listo

        print("Conectado al puerto serial:", arduino_port)

        while True:
            # Lee una línea de datos del puerto serial
            cadena = serie.readline().decode('utf-8').rstrip()
            if cadena:  # Solo imprimir si se recibió algo
                print(cadena)

    except serial.SerialException as e:
        print(f"Error abriendo el puerto serial: {e}")

    finally:
        # Cierra el puerto serial al finalizar
        if 'serie' in locals() and serie.is_open:
            serie.close()

