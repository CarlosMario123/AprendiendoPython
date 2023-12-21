def StopDoublePoint(string):
    indice = 0
    
    while indice < len(string) and string[indice] != ':':
        indice += 1
    
    if indice < len(string):
        return string[:indice + 1]  # Incluimos el carácter ":"
    else:
        return None  # Retorna None si no se encuentra ":"

# Ejemplo de uso:
""" 
cadena = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
resultado = StopDoublePoint(cadena)

if resultado:
    print(f"El substring encontrado es: '{resultado}'")
else:
    print("No se encontró ':' en el string.")
"""

