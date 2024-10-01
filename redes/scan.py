import scapy.all as scapy

def scan_network(iface):
    """
    Escanea la red WiFi en busca de dispositivos conectados.

    Args:
        iface (str): Nombre de la interfaz de red WiFi.
    """

    # Crea un paquete ARP para solicitar información de los dispositivos conectados.
    arp_request = scapy.ARP(pdst="192.168.1.0/24")

    # Envía el paquete ARP y captura las respuestas.
    print("[Scanning...]")
    answered_list = scapy.srp(arp_request, timeout=10, verbose=False)[0]

    # Muestra la información de los dispositivos conectados.
    print("Dispositivos conectados:")
    for answer in answered_list:
        if answer[1].psrc is not None:
            print(f"  - IP: {answer[1].psrc} | MAC: {answer[1].hwsrc}")

if __name__ == "__main__":
    # Especifica la interfaz de red WiFi a escanear.
    iface = "wlan0"

    # Ejecuta la función para escanear la red.
    scan_network(iface)
