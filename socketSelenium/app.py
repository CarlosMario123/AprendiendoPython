from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit
import time
from pageScrape import Driver
import json

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')

@socketio.on('requestSelenium')
def handle_my_custom_event(data):
    # Obtener el ID de la sesión del cliente que envió el mensaje
    session_id = request.sid
    
    emit('responseSelenium',"tu informacion esta cargando no salga de la pagina", room=session_id)
    driver = Driver("https://www.mercadolibre.com.mx/")
    
    datos = driver.get_all_urls()
    driver.driver.close()
    
    sendJson = {
        "datos" : datos
    }
    
    # Enviar una respuesta al mismo cliente que envió el mensaje
    emit('responseSelenium',json.dumps(sendJson) , room=session_id)    
    
if __name__ == '__main__':
    socketio.run(app, debug=True)    