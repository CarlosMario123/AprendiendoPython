from random import shuffle
from modelos.Carta import Carta
class Baraja:
    def __init__(self):
        self.cartas = []
        self.formarMazo()

    def barajear(self):
        # Baraja las cartas en el lugar
        shuffle(self.cartas)
        return self.cartas

    def formarMazo(self):
        tipos = ["espada", "bastos", "copa", "oro"]
        numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        for tipo in tipos:
            for numero in numeros:
                self.cartas.append(Carta(tipo, numero))