from datetime import datetime
import time
import threading

ROJO = '\033[91m'
VERDE = '\033[92m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
BLANCO = '\033[97m'
RESET = '\033[0m'
def viewColores(color):
    for n in range(6000):
        hora = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"{color}#{n}: {hora}{RESET}")





if __name__ == "__main__":
    inicio = datetime.now()
    #ejecutaremos el codigo en hilos
    
    h1 = threading.Thread(name="Hilo 1",target=viewColores,args=(ROJO,))
    h2 = threading.Thread(name="Hilo 2",target=viewColores,args=(VERDE))
    h3 = threading.Thread(name="Hilo 3",target=viewColores,args=(AMARILLO,))
    h4 = threading.Thread(name="Hilo 4",target=viewColores,args=(MAGENTA,))
    h5 = threading.Thread(name="Hilo 5",target=viewColores,args=(CIAN,))
    
    #iniciomos los hilos
    h1.start()
    h2.start()
    h3.start()
    h4.start()
    h5.start()
    
    #obligamos a los que los hilos finalizen su ejecutcion para continuar
    h1.join()
    h2.join()
    h3.join()
    h4.join()
    h5.join()
    print(f"Programa finalizado en {(datetime.now() - inicio).total_seconds()} segundos")