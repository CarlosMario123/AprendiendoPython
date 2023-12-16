""" 

La inyección de dependencia es un patrón de diseño en el que las dependencias de un objeto se 
le proporcionan desde el exterior en lugar de ser creadas dentro del objeto mismo. 
En Python, la inyección de dependencia se puede lograr de varias maneras. A
quí tienes un ejemplo sencillo utilizando clases:
Supongamos que tienes una clase Servicio que d
epende de otra clase Logger para registrar información. En lugar de 
instanciar directamente la clase Logger dentro de Servicio, puedes inyectarla como una dependencia.
"""

class Logger:
    def log(self, mensaje):
        print(f"Registrando: {mensaje}")


class Servicio:
    def __init__(self, logger):
        self.logger = logger

    def ejecutar(self):
        # Hacer algo y registrar utilizando el logger inyectado
        self.logger.log("El servicio se está ejecutando.")


# Crear una instancia de Logger
logger = Logger()

# Inyectar Logger en la instancia de Servicio
servicio = Servicio(logger)

# Ejecutar el servicio
servicio.ejecutar()
