import hashlib
import itertools


def calcular_hash(cadena, algoritmo='sha512'):
    if algoritmo == 'sha512':
        return hashlib.sha512(cadena.encode()).hexdigest()
    # Agregar más algoritmos de hash según sea necesario

def fuerza_bruta(hash_objetivo, longitud_maxima=500, caracteres='abcdefghijklmnopqrstuvwxyz'):
    for longitud in range(1, longitud_maxima + 1):
        for contraseña in itertools.product(caracteres, repeat=longitud):
            contraseña = ''.join(contraseña)
            hash_calculado = calcular_hash(contraseña)
            if hash_calculado == hash_objetivo:
                return contraseña
    return None

hash_objetivo = 'eyJpdiI6InB4Rlc4U3VUUnNjZm80Tmd2MWx6b0NkOUQyd2JNMTJSKzVxM3JnRUxpOTA9IiwidmFsdWUiOiJ1QVhJbkJMZk5Hc3JXNUcxeXliVzEyUEdJdzQxQmJDSEx0Mm9GNGpZclJOM0NhVVZIUWdOWkcyWVNvQUNKWURNdXlxZ29maXB3TTlFTkpqaEIxSU1HZz09IiwibWFjIjoiYzg5ZTYyNTIzZjI2MGMxNzgyNTA1YzMzZGE0M2M5YWU5MTU1NjRlNzgzNmFkNWRiMDk1MjJjNTYzNTQwYjY2NSJ9'  # Ejemplo de hash SHA-256
contraseña = fuerza_bruta(hash_objetivo)
if contraseña:
    print(f"La contraseña es: {contraseña}")
else:
    print("No se pudo encontrar la contraseña.")
