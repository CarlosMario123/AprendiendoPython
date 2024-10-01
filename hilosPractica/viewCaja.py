import threading
import time
import random
import tkinter as tk

# Capacidad máxima de la cola
MAX_COLA_SIZE = 5

# Semáforos para controlar el número de cajas disponibles
semCajas = threading.Semaphore(3)

# Semáforos para controlar el acceso a la cola de clientes
colaGente = []
colaLock = threading.Semaphore(1)  # Semáforo para asegurar acceso exclusivo a colaGente
colaEspacios = threading.Semaphore(MAX_COLA_SIZE)  # Semáforo para controlar el número de espacios en colaGente

run = True

def actualizar_estado():
    global colaGente
    # Actualiza la cola de clientes en espera
    colaGente_texto = f"Clientes en espera: {', '.join(map(str, colaGente))}"
    cola_label.config(text=colaGente_texto)

    # Actualiza el estado de las cajas
    for i, estado in enumerate(caja_estados):
        estado_label[i].config(text=estado)

    ventana.after(100, actualizar_estado)  # Actualizar cada 100 ms

def atenderGente(id):
    global run
    while run:
        semCajas.acquire()  # Esperar hasta que haya una caja disponible
        caja_estados[id - 1] = "Atendiendo..."
        ventana.update_idletasks()
        
        time.sleep(random.randint(2, 3))  # Simula el tiempo de atención

        colaLock.acquire()  # Adquirir acceso exclusivo a la cola
        if colaGente:
            value = colaGente.pop(0)
            colaEspacios.release()  # Liberar espacio en la cola después de atender
            caja_estados[id - 1] = f"Atendido {value}"
        else:
            caja_estados[id - 1] = "Disponible"
            semCajas.release()  # Liberar la caja si no había clientes
        colaLock.release()  # Liberar el acceso a la cola
        
        ventana.update_idletasks()
        semCajas.release()  # Liberar la caja después de atender

def genteLlegando():
    global run
    while run:
        colaEspacios.acquire()  # Esperar hasta que haya un espacio en la cola
        value = random.randint(1, 100)
        colaLock.acquire()  # Adquirir acceso exclusivo a la cola
        colaGente.append(value)
        colaLock.release()  # Liberar el acceso a la cola 
        colaEspacios.release()  # Liberar el espacio en la cola
        print(f"Persona {value} llegó")
        ventana.update_idletasks()
        time.sleep(5)  # Simula el tiempo entre llegadas

def stop_all_threads():
    global run
    time.sleep(15)  # Ejemplo de tiempo de ejecución, ajusta según necesites
    run = False
    semCajas.release()
    colaEspacios.release()
    colaLock.release()

# Crear la ventana de tkinter
ventana = tk.Tk()
ventana.title("Simulación de Supermercado")

# Crear y colocar los widgets
cola_label = tk.Label(ventana, text="Clientes en espera: ")
cola_label.pack()

# Etiquetas para las cajas
estado_label = []
caja_estados = ["Disponible"] * 3
for i in range(3):
    estado_label.append(tk.Label(ventana, text=f"Caja {i+1}: {caja_estados[i]}", bg="lightgrey", width=20))
    estado_label[i].pack(pady=5)

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

# Iniciar actualización del estado de la cola de clientes
ventana.after(100, actualizar_estado)

# Ejecutar la interfaz gráfica
ventana.mainloop()

caja1.join()
caja2.join()
caja3.join()
gente.join()
