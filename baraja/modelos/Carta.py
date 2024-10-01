class Carta:
    def __init__(self, tipo, numero):
        self.tipo = tipo
        self.numero = numero

    def __str__(self):
        return self.mostrar()
    
    def mostrar(self):
        return f"{self.numero} de {self.tipo}"