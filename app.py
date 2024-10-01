import multiprocessing
import threading
import os
import time

# Función que será ejecutada por cada hilo
def worker_thread(thread_num):
    print(f"Hilo {thread_num} en proceso {os.getpid()} está trabajando.")
    time.sleep(1)  # Simula trabajo con una pausa
    print(f"Hilo {thread_num} en proceso {os.getpid()} ha terminado.")

# Función que será ejecutada por cada proceso
def worker_process(process_num):
    print(f"Proceso {process_num} iniciado con ID {os.getpid()}.")
    
    threads = []
    for i in range(2):  # Creando 2 hilos por proceso
        thread = threading.Thread(target=worker_thread, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()  # Espera a que todos los hilos terminen
    
    print(f"Proceso {process_num} ha terminado.")

if __name__ == "__main__":
    processes = []
    
    for i in range(3):  # Crear 3 procesos
        process = multiprocessing.Process(target=worker_process, args=(i,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()  # Espera a que todos los procesos terminen
    
    print("Todos los procesos y hilos han terminado.")
