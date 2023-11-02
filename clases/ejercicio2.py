""" Crea una superclase llamada Vehiculo con atributos como marca, modelo, año, y métodos como encender y apagar. 
Luego, crea subclases como Coche y Moto que hereden de Vehiculo y 
tengan atributos y métodos adicionales específicos para cada tipo de vehículo."""

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas

    def abrir_puertas(self):
        print(f"Las puertas del coche {self.marca} {self.modelo} están abiertas.")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def acelerar(self):
        print(f"La moto {self.marca} {self.modelo} está acelerando.")

# Crear un coche y una moto
mi_coche = Coche("Toyota", "Corolla", 2022, 4)
mi_moto = Moto("Honda", "CBR 600", 2021, "600 cc")

# Encender el coche
mi_coche.encender()
print(f"¿El coche está encendido? {mi_coche.encendido}")

# Acelerar la moto
mi_moto.acelerar()

# Abrir las puertas del coche
mi_coche.abrir_puertas()
