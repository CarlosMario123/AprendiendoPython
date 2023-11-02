
class Perro:
    #esta es una propiedad de clase
    patas = 4
    # Constructor de nuestra clase
    def __init__(self, nombre,edad):
        #para hacer privado un nombre usamos -> __ antes del nombre del atributo
        
        self.__nombre = nombre
        self.__edad = edad
        
    @classmethod
    def ladrar(cls):
        print("gua gua")
        
    def verInformacion(self):
        print(f"Hola mi nombre es: {self.__nombre} y tengo {self.__edad} años") 
        
        
perro = Perro("solovino",12)

#si se desea acceder a un atributo privado marcara un error
print(perro.__edad)

       