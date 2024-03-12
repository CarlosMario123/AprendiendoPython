import paho.mqtt.publish as publish
import json

# Configuración del servidor MQTT
broker_address = "54.172.38.119"
port = 1883
topic = "prueba/"
username = "esp32"  # Reemplaza con tu nombre de usuario
password = "1234"  # Reemplaza con tu contraseña

# Mensaje a publicar
message = {
     "temperatura": 35,
     "iluminacion": 140
}

# Convertir el mensaje a formato JSON
json_message = json.dumps(message)

# Publicar el mensaje con credenciales
publish.single(topic, json_message, hostname=broker_address, port=port, auth={'username': username, 'password': password})
