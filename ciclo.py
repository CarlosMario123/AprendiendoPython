import multiprocessing
import os

def worker_process(number):
    print(f"Proceso {number}: ID: {os.getpid()} - Proceso padre ID: {os.getppid()}")

if __name__ == "__main__":
    processes = []

    # Crear e iniciar 4 procesos
    for i in range(4):
        process = multiprocessing.Process(target=worker_process, args=(i,))
        processes.append(process)
        process.start()

    # Esperar a que todos los procesos terminen
    for process in processes:
        process.join()

    print("Todos los procesos han terminado.")

