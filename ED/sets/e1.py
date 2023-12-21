import string

def palabras_unicas(texto):
    # Eliminar puntuaciones y convertir a minúsculas
    texto = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Dividir el texto en palabras y obtener las palabras únicas usando un set
    palabras = set(texto.split())
    
    return palabras

# Ejemplo de uso
texto_ejemplo = "Este es un ejemplo de texto. Ejemplo de texto que contiene palabras repetidas."
palabras = palabras_unicas(texto_ejemplo)
print("Palabras únicas en el texto:", palabras)
