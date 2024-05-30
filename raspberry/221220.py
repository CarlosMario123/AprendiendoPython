from gpiozero import LEDBoard
from time import sleep

# Practica atenuacion de luz


leds = LEDBoard(5, 6, 13, 19, 26, 16, 20, 21, pwm=True)

matricula_binaria = {
    "0": (0, 0, 0, 0, 0, 0, 0, 0),
    "1": (0, 0, 0, 0, 0, 0, 0, 1),
    "2": (0, 0, 0, 0, 0, 0, 1, 0),
    "3": (0, 0, 0, 0, 0, 0, 1, 1),
    "4": (0, 0, 0, 0, 0, 1, 0, 0),
    "5": (0, 0, 0, 0, 0, 1, 0, 1),
    "6": (0, 0, 0, 0, 0, 1, 1, 0),
    "7": (0, 0, 0, 0, 0, 1, 1, 1),
    "8": (0, 0, 0, 0, 1, 0, 0, 0),
    "9": (0, 0, 0, 0, 1, 0, 0, 1),
}

# Matrícula: 221220
matricula = "221220"


brillo_niveles = [1.0, 0.5, 0.3]

while True:
    for nivel in brillo_niveles:
        for digit in matricula:

            leds.value = tuple(nivel * val for val in matricula_binaria[digit])
            sleep(1)
            # Apagar todos los LEDs
            leds.value = (0,) * len(leds)
            sleep(1)
