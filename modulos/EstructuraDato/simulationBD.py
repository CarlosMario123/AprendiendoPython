#para utilizar esto hay que exportarlo

class SimulationBd():
    def __init__(self):
        self.lista = []
    def guardar(self,element):
        self.lista.append(element)
        print("Elemento guardado correctamente")
    def getAll(self):
        return self.lista
               