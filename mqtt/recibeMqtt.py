import paho.mqtt.client as mqtt

# Definir los parámetros del servidor MQTT
broker_address = "srv502440.hstgr.cloud"
port = 1883
topic = "prueba/"
username = "esp32"  # Reemplaza con tu nombre de usuario
password = "1234"  # Reemplaza con tu contraseña

# Callback que se ejecutará cuando el cliente se conecte al servidor
def on_connect(client, userdata, flags, rc):
    print("Conectado con el código de resultado: " + str(rc))
    # Suscribirse al tema una vez que se ha establecido la conexión
    client.subscribe(topic)

# Callback que se ejecutará cuando se reciba un mensaje en el tema suscrito
def on_message(client, userdata, msg):
    print(f"Mensaje recibido en el tema {msg.topic}: {str(msg.payload)}")

# Crear un cliente MQTT
client = mqtt.Client()

# Configurar las funciones de callback
client.on_connect = on_connect
client.on_message = on_message

# Configurar las credenciales de usuario y contraseña
client.username_pw_set(username, password)

# Conectar al servidor MQTT
client.connect(broker_address, port, 60)

# Mantener el cliente en ejecución para recibir mensajes
client.loop_forever()
