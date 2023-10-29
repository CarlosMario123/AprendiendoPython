"""
    para hacer un mapeo primero paso encapsulamos todo dentro de una funcion 
    La función map() en Python se utiliza para aplicar una función a cada elemento de un iterable (como una lista, una tupla, etc.) y
    devuelve un objeto map, que es un iterable que
    contiene los resultados de aplicar la función a cada elemento del 
    iterable original. La sintaxis general de map() es la siguiente:
    map(función, iterable)
    ejemplos: 
 """
 
# Ejemplo usando map() con una función lambda
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x**2, numeros)

# cuadrados ahora es un objeto map, para ver los resultados, conviértelo en una lista
cuadrados = list(cuadrados)
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]


""" veamos el ejemplo de udemy"""

users = [
    ["usuario1",15],
    ["usuario2",17],
    ["usuario3",16],
    ["usuario4",13],
]

print("ejemplo de udemy")
#procedemos a mapear solo numero del arreglo user
soloNumero =  map(lambda user: user[1],users)
# Convierte el objeto map en una lista para ver los resultados
soloNumero = list(soloNumero)
print(soloNumero)

print("ahora imprimiremos solo los nombres")
soloName = list(map(lambda user:user[0],users))
print(soloName)