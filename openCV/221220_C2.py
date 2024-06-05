import cv2
from datetime import datetime

def asignarFecha():
    fecha_actual = datetime.now()
    # Formatea la fecha sin caracteres especiales para el nombre del archivo
    fecha_formateada = fecha_actual.strftime('%d-%m-%Y_%H-%M-%S')
    return fecha_formateada

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se puede acceder a la cámara")
    exit()

while True:
    # Captura frame a frame
    ret, frame = cap.read()

    if not ret:
        print("Error: No se puede recibir frame (stream end?). Exiting ...")
        break

    # Muestra el frame resultante
    cv2.imshow('frame', frame)

    # Espera la tecla presionada
    key = cv2.waitKey(1)

    # Si se presiona '0', toma la foto
    if key == ord('0'):
        # Obtiene la fecha y hora actual formateada
        fecha_formateada = asignarFecha()
        # Genera el nombre del archivo con la fecha y hora actual
        nombre_archivo = f'foto_{fecha_formateada}.png'
        # Guarda la imagen
        cv2.imwrite(nombre_archivo, frame)
        print(f"Foto tomada y guardada como {nombre_archivo}")

    # Si se presiona 'q', sale del bucle
    elif key == ord('q'):
        break

# Cuando todo haya terminado, libera la captura
cap.release()
cv2.destroyAllWindows()
