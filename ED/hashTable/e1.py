"""
Ejemplo 1: Contar la frecuencia de elementos en una lista
Dada una lista de elementos, contar la frecuencia de cada 
elemento utilizando una tabla hash y luego imprimir los resultad
"""
def contarFrecuencia(lista):
    frecuencia = {}  # Crear una tabla hash vacía para almacenar la frecuencia de elementos

    # Contar la frecuencia de cada elemento en la lista
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1  # Incrementar la frecuencia si el elemento ya está en la tabla hash
        else:
            frecuencia[elemento] = 1   # Agregar el elemento a la tabla hash si es la primera vez que aparece

    return frecuencia

# Lista de ejemplo
mi_lista = [1, 2, 2, 3, 4, 1, 2, 4, 5, 1, 3, 3]

# Obtener la frecuencia de elementos en la lista
resultado = contarFrecuencia(mi_lista)

# Imprimir los resultados
for elemento, frec in resultado.items():
    print(f"El elemento {elemento} aparece {frec} veces")
