# Para crear una clase en Python usamos la palabra reservada 'class'
# Para las notaciones de nuestras clases, acostumbramos a usar la notación CamelCase

class Perro:
    # Constructor de nuestra clase
    def __init__(self, nombre,edad):
        # Dentro de los parámetros de las funciones, agregamos la palabra 'self'
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print("gua gua")
        
    def verInformacion(self):
        print(f"Hola mi nombre es: {self.nombre} y tengo {self.edad} años")    



        
#instanciomos la clase perro

miPerro =  Perro("bobi",10)

miPerro.ladrar()
miPerro.verInformacion()

#la funcion type nos detecta que tipo es nuestro objeto

print("el tipo es: ",type(miPerro))

""" en python no hay sobrecarga de constructores pero podemos realizar esta tecnica
""" 
class MiClase:
    def __init__(self, parametro1, parametro2=None):
        if parametro2 is None:
            # Si no se proporciona parametro2, realizar alguna acción predeterminada
            self.atributo = parametro1
        else:
            # Si se proporciona parametro2, realizar alguna acción diferente
            self.atributo = parametro1 + parametro2

# Crear instancias con diferentes números de argumentos
obj1 = MiClase(10)
obj2 = MiClase(10, 5)

print(obj1.atributo)  # Resultado: 10
print(obj2.atributo)  # Resultado: 15
       