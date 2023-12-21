def obtener_subcadena_despues_de_punto_al_reves(cadena):
    indice = len(cadena) - 1  # Índice inicial al final de la cadena
    
    while indice >= 0:
        if cadena[indice] == '.':
            return cadena[indice + 1:]  # Retorna la subcadena después del punto
        
        indice -= 1  # Mueve el índice hacia atrás
    
    return ""  # Si no se encontró ningún punto, retorna una cadena vacía