from flask import Flask,request,jsonify
from flask_socketio import SocketIO
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
llaves = []

@app.route("/ids")
def identificadores():
    print(llaves)
    return jsonify({"llaves": llaves})

@socketio.on('connect')
def handle_connect():
    print("cliente conectado ",request.sid)


@socketio.on('mensaje')
def handle_message(data):
    diccionario = data
    ide = diccionario.get("id")
    command = diccionario.get("command")
    print("mensaje")
    if ide and command:
        socketio.emit(f'controlar{ide}', command)  
    else:
        print("E mensaje que recibiste no tiene id")

@socketio.on("recibirInfo")
def reciveMensaje(data):
    socketio.emit("recibirInfo", data)

    
@socketio.on('linea')
def inLine(data):
    print("en linea")
    
    hora = datetime.now().time()
    #procederemos almacenar la llaves junto con la hora de la informacion
    llaves.append({"key":data,"hora":str(hora)})
    socketio.emit("id",data)
    print(data)

if __name__ == '__main__':
   
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
