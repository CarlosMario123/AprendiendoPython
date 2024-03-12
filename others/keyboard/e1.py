import keyboard

def on_key_event(e):#este es el calback para la tecla
    print(f"Tecla presionada: {e.name}")
    if e.name == 'esc':  # Detener el programa si se presiona la tecla 'esc'
        return False  # Devuelve False para salir del bucle

keyboard.hook(on_key_event)#se crea un evento de teclado

while True:
    if not keyboard.is_pressed('esc'):  # Verifica si la tecla 'esc' no está presionada
        continue  # Si no se presiona 'esc', continúa el bucle
    else:
        break  # Si se presiona 'esc', sale del bucle

keyboard.unhook_all()#eliminar el evento

