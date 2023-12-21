#identificae que elemento no se repite
def primer_no_repetido(lista):
    tabla_hash = {}
    
    # Primera pasada para contar la frecuencia de cada elemento
    for elemento in lista:
        if elemento in tabla_hash:
            tabla_hash[elemento] += 1
        else:
            tabla_hash[elemento] = 1

    # Segunda pasada para encontrar el primer elemento no repetido
    for elemento in lista:
        if tabla_hash[elemento] == 1:
            return elemento
    
    return None  # Retorna None si no hay elementos no repetidos

# Ejemplo de uso
mi_lista = [3, 5, 2, 7, 5, 3, 8, 2]
resultado = primer_no_repetido(mi_lista)
print("El primer elemento no repetido es:", resultado)
