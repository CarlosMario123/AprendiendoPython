"""en python tambien existe un concepto que son los metodos de clases
es decir ese metodo le pertecene a esa clase pero para hacer uso de ellos 
utilizamos un notacion convecional que seria

@classmethod
def metodo(cls,parametros)
"""

class Perro:
    #esta es una propiedad de clase
    patas = 4
    # Constructor de nuestra clase
    def __init__(self, nombre,edad):
        # Dentro de los parámetros de las funciones, agregamos la palabra 'self'
        self.nombre = nombre
        self.edad = edad
        
    @classmethod
    def ladrar(cls):
        print("gua gua")
        
    def verInformacion(self):
        print(f"Hola mi nombre es: {self.nombre} y tengo {self.edad} años") 