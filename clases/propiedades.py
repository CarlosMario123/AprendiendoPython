#en python existe un conceptos que es propiedades de clases 
#todas las clase que se instancien tendran el mismo atributo

class Perro:
    #esta es una propiedad de clase
    patas = 4
    # Constructor de nuestra clase
    def __init__(self, nombre,edad):
        # Dentro de los parámetros de las funciones, agregamos la palabra 'self'
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print("gua gua")
        
    def verInformacion(self):
        print(f"Hola mi nombre es: {self.nombre} y tengo {self.edad} años")  
        
#crearemos 2 perros
perro1 =  Perro("bobi",10)
perro2 =  Perro("solovina",12)

#mostramos la info de cada uno

perro1.verInformacion()
perro2.verInformacion()

print("patas del perro1: ",perro1.patas)   
print("patas del perro2: ",perro2.patas)         