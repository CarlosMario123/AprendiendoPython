"""@property es útil para validar y asegurarse de que los datos de entrada cumplan con ciertos 
criterios antes de asignarlos a un atributo. 
Aquí, aseguramos que la edad sea un número positivo:"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser negativa")

persona = Persona("Alice", 30)


