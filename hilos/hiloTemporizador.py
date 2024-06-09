import threading


""" 

Para lograr esto podemos hacer uso de la clase Timer. Crearemos una instancia e i
ndicaremos en el constructor el tiempo de espera inicial, la función que ejecutara el hilo, parámetro function, y
los parámetros a dicha función (args o kwargs).

Veamos un ejemplo sencillo:

import threading
"""
def ejecutar():
    print(f'{threading.current_thread().name} te saluda')

# creamos un temporizador
temporizador = threading.Timer(5, function=ejecutar)  # creamos el hilo con temporizador
temporizador.start()  # el hilo empezará cuando pasen 5 segundos

print("Ejecucion finalizada hilo principal")