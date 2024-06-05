import cv2

# Crear un objeto VideoCapture para capturar video desde la cámara
cap = cv2.VideoCapture(0)

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Definir el códec y crear un objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Puedes cambiar 'XVID' por otros códecs si es necesario
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    # Capturar frame por frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: No se pudo leer el frame.")
        break

    # Voltear el frame horizontalmente para corregir la inversión
    frame = cv2.flip(frame, 1)

    # Escribir el frame en el archivo de salida
    out.write(frame)

    # Mostrar el frame capturado
    cv2.imshow('frame', frame)

    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el objeto VideoCapture y VideoWriter y cerrar todas las ventanas
cap.release()
out.release()
cv2.destroyAllWindows()
