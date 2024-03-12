import serial

# Abre la conexión con el puerto serial (COM7 en Windows)
ser = serial.Serial('COM7', baudrate=9600,timeout=1)

if ser.is_open:
    print("Conexión establecida al puerto COM7")
  
    # Envía datos al dispositivo conectado
    #ser.write(dato.encode())

    # Lee datos del dispositivo conectado
    data = 500
    while(data > 15):
        data = ser.readline()
        print('Datos recibidos:', data.decode())
        data = int(data.decode())
    
   

    # Cierra la conexión serial
    ser.close()
else:
    print("No se pudo abrir la conexión al puerto COM7")
