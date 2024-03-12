#lo que se hara aca es controla con keyboard un servomotor en el puerto serial

#utilizaremos la libreria pyserial y keyboard para el teclado
import serial
import keyboard
import time
#objeto para la comunicacion serial
ser = serial.Serial('COM7', baudrate=9600,timeout=1)
print("Para controlar el servomotor se usa 3 comandos")
time.sleep(1)
print("tecla derecha-mover a hacia 0")
print("tecla izquiera-mover a hacia 180")
print("esc salir-salir")
time.sleep(2)
print("Programa iniciado")

#creamos la funcion para el evento
def on_key_event(e):#este es el calback para la tecla
    print(f"Tecla presionada: {e.name}")
    if e.name == 'esc':  # Detener el programa si se presiona la tecla 'esc'
        return True  # Devuelve False para salir del bucle

keyboard.hook(on_key_event)#se crea un evento de teclado

def controlarServoByTecla(tecla):
    if(tecla == "flecha derecha"):
         dato = 1  # Número entero
         ser.write(dato.to_bytes(1, byteorder='little'))
    
    if(tecla == "flecha izquierda" ):
        dato = 0  # Número entero
        ser.write(dato.to_bytes(1, byteorder='little'))

while True:
    if  keyboard.is_pressed('esc'):  # Verifica si la tecla 'esc' no está presionada
        break
    else:
        continue
  

keyboard.unhook_all()#eliminar el evento

