"""
La función filter() en Python se utiliza para filtrar elementos de un iterable (como una lista, una tupla, etc.)
que cumplan con una condición especificada en una función. La sintaxis general de filter() es la siguiente:

filter(función, iterable)

ejemplos
"""

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando filter() con una función lambda para filtrar los números pares
numeros_pares = filter(lambda x: x % 2 == 0, numeros)

# Convierte el objeto filter en una lista para ver los resultados
numeros_pares = list(numeros_pares)

print(numeros_pares)  # Salida: [2, 4, 6, 8, 10]


"""
Filtrar palabras largas:
Dada una lista de palabras, utiliza filter() para obtener una lista con solo las palabras que tienen más de cinco letras.
"""
palabras = ["perro", "gato", "elephant", "zebra", "tigre","ferrocarril"]
print("ejercicios filtrar palabras largas")
palabrasFil = list(filter(lambda x: len(x) > 5,palabras))
print("palabras filtradas",palabrasFil)

#filtrar elementos que empiezen con una letra en especifica

letra = input("ingrese una letra filtro para realizar la busqueda\n")

wordFill = list(filter(lambda x: x[0] == letra,palabras))
print(f"Esta son las palabras que empiezan con {letra}:")
print(wordFill)

#filtrar numeros negativos:
print("filtra numeros negativos")

numeros = [-1,3,4,-4,5,-5,-4,-2]

numbersNe = list(filter(lambda x: x < 0,numeros))
print("los numeros negativos son: ",numbersNe)

#filtrar elementos unicos
print("ejercicio elemtos unicos")
numeros = [1, 2, 2, 3, 3, 4, 4, 5, 5,7]
elementos_unicos = list(filter(lambda x: numeros.count(x) == 1, numeros))
print(elementos_unicos)