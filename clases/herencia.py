class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass#cuando agregamos pass al metodo de la superclase esta se podra sobreesribir

class Perro(Animal):#cuando queremos heredar utilizamos parentesis clase a heredar
    def hablar(self):
        return "Woof!"

class Gato(Animal):
    def rasgar(self):
        print("el gato te ha rasgado")
    def hablar(self):
        return "Meow!"

perro = Perro("Buddy")
gato = Gato("Whiskers")

print(perro.nombre)  # Salida: "Buddy"
print(perro.hablar())  # Salida: "Woof!"

print(gato.nombre)  # Salida: "Whiskers"
print(gato.hablar())  # Salida: "Meow!"