import paho.mqtt.client as mqtt
import tkinter as tk
import threading

class MQTTClient:
    def __init__(self, broker, port, topic):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()

        # Lista de eventos para ejecutar cuando llegue un mensaje MQTT
        self.eventos = []

        # Asignar las funciones callback
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"Conectado con el código de resultado {rc}")
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        msgGlobal = f"Mensaje recibido en el tema {msg.topic}: {msg.payload.decode()}"
        
        # Ejecutar eventos registrados
        for event in self.eventos:
            event(msgGlobal)

    def start(self):
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_forever()

    def add_evento(self, evento):
        self.eventos.append(evento)

    def desconectar(self):
        self.client.disconnect()

# Crear una instancia de la aplicación Tkinter
window = tk.Tk()
window.title("Hola Mundo")

# Crear el label en la ventana
label = tk.Label(window, text="Esperando mensajes MQTT...")
label.pack(side=tk.TOP, anchor=tk.CENTER, padx=20, pady=20)

# Función para actualizar el label cuando llegue un mensaje MQTT
def update_label(msg):
    label.config(text=msg)

# Crear una instancia del cliente MQTT y comenzar en un hilo separado
mqtt_client = MQTTClient(broker="broker.hivemq.com", port=1883, topic="/tkTest")
mqtt_client.add_evento(update_label)
mqtt_thread = threading.Thread(target=mqtt_client.start, name="hilo mqtt")
mqtt_thread.start()

# Función para manejar el cierre de la ventana
def on_cerrar_ventana():
    mqtt_client.desconectar()
    window.destroy()

# Configurar el evento de cierre de la ventana
window.protocol("WM_DELETE_WINDOW", on_cerrar_ventana)

# Bucle principal de la interfaz gráfica
window.mainloop()
