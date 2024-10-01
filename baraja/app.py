from modelos.Baraja import Baraja

baraja = Baraja()

cartas = baraja.barajear()

jugadores = {
    "j1": [],
    "j2": [],
    "j3": [],
}


for jugador in jugadores:
    for _ in range(9):  # Se reparten 9 cartas a cada jugador
        jugadores[jugador].append(cartas.pop(0))

print("cartas por jugador")
for jugador in jugadores:
    print("\n\ncartas del jugador: ",jugador,"")
    for carta in jugadores[jugador]:
        print(carta)



