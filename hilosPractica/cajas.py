import threading
import time
import random

# Semáforo para controlar el número de cajas disponibles
semCajas = threading.Semaphore(3)

# Semáforos para controlar el acceso a la cola de clientes
colaGente = []
colaLock = threading.Semaphore(1)  # Semáforo para asegurar acceso exclusivo a colaGente
colaEspacios = threading.Semaphore(10)  # Semáforo para controlar el número de espacios en colaGente

run = True

def atenderGente(id):
    global run
    while run:
        semCajas.acquire()  # Esperar hasta que haya una caja disponible
        colaLock.acquire()  # Adquirir acceso exclusivo a la cola
        if colaGente:
            value = colaGente.pop(0)
            print(f"caja {id} atendió al número {value}")
            colaEspacios.release()  # Liberar espacio en la cola después de atender
        else:
            colaLock.release()  # Liberar el acceso a la cola si está vacía
            semCajas.release()  # Liberar la caja si no había clientes
            print(f"caja {id} Esperando gente")
            continue
        colaLock.release()  # Liberar el acceso a la cola
        time.sleep(random.randint(2, 3))  # Simula el tiempo de atención
        semCajas.release()  # Liberar la caja después de atender

def genteLlegando():
    global run
    while run:
        
        colaEspacios.acquire()  # Esperar hasta que haya un espacio en la cola
        value = random.randint(1, 100)
        colaLock.acquire()  # Adquirir acceso exclusivo a la cola
        time.sleep(0.4)  # Simula el tiempo entre llegadas
        colaGente.append(value)
        colaLock.release()  # Liberar el acceso a la cola
        print(f"persona {value} llegó")
        

def stop_all_threads():
    global run
    time.sleep(10)  # Ejemplo de tiempo de ejecución, ajusta según necesites
    run = False
    semCajas.release()
    colaEspacios.release()
    colaLock.release()

# Iniciar hilos
threading.Thread(target=stop_all_threads).start()

caja1 = threading.Thread(target=atenderGente, args=(1,))
caja2 = threading.Thread(target=atenderGente, args=(2,))
caja3 = threading.Thread(target=atenderGente, args=(3,))
gente = threading.Thread(target=genteLlegando)

caja1.start()
caja2.start()
caja3.start()
gente.start()

caja1.join()
caja2.join()
caja3.join()
gente.join()
