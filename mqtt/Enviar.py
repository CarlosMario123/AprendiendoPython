import paho.mqtt.publish as publish
import json
import time

# Configuración del servidor MQTT
broker_address = "srv502440.hstgr.cloud"
port = 1883
topic = "prueba/"
username = "esp32"  # nombre de usuario
password = "1234"  # contraseña

# Mensaje a publicar
message = {
     "temperatura": 35,
     "iluminacion": 140
}

# Convertir el mensaje a formato JSON
json_message = json.dumps(message)

# Publicar el mensaje con credenciales
for i in range(5):
     time.sleep(2)
     print("enviando.....")
     publish.single(topic, json_message, hostname=broker_address, port=port, auth={'username': username, 'password': password})
     

