import socket

# Configuración del servidor
HOST = 'localhost'  # Usa 'localhost' para pruebas locales
PORT = 3001         # Puerto en el que escucha el servidor

# Función para manejar las conexiones de los clientes
def handle_client_connection(client_socket):
    html_response = """
    <html>
    <head><title>Hola Mundo</title></head>
    <body>
    <h1>Hola Mundo</h1>
    <p>Este es un servidor simple de Python usando sockets accesible desde cualquier red.</p>
    </body>
    </html>
    """
    client_socket.sendall(html_response.encode())
    client_socket.close()

# Crea un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Enlaza el socket a la dirección y puerto especificados
    server_socket.bind((HOST, PORT))
    print(f"Servidor escuchando en {HOST}:{PORT}...")

    # Escucha conexiones entrantes (máximo 1 en cola)
    server_socket.listen(2)

    while True:
        # Acepta la conexión entrante
        client_socket, client_address = server_socket.accept()
        print(f"Conexión entrante desde {client_address}")

        # Maneja la conexión del cliente
        handle_client_connection(client_socket)

except KeyboardInterrupt:
    print("\nServidor detenido manualmente.")

finally:
    # Cierra el socket del servidor
    server_socket.close()
