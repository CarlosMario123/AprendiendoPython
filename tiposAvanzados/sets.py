import time
"""
    un set es una estructura de datos que representa una colección desordenada de
    elementos únicos. Esto significa que, en un conjunto, no puede haber elementos duplicados 
    cada elemento aparece una sola vez.
    Los conjuntos se utilizan para realizar operaciones de conjunto, 
    como unión, intersección, diferencia y otras operaciones matemáticas en conjuntos.
 """
 
#formas de crear sets
# Crear un conjunto con llaves
mi_set = {1, 2, 3, 4, 5}

# Crear un conjunto con la función set()
otro_set = set([3, 4, 5, 6, 7])

#ejemplo de como trabajar con operacion de conjuntos
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

print("Tenemos los conjuntos: ")
print("A :",conjunto1)
print("B: ",conjunto2)
time.sleep(1.5)
print("Podemos realizar diferentes operaciones de conjuntos como:")
time.sleep(1.5)
print("1)Union\n2)Interseccion\n3)Diferncia")
time.sleep(1.5)
print("Hagamos un ejemplo:")
time.sleep(1.5)
print("Con los conjuntos anteriores podemos realizar una union entre A y B el resultado nos daria")
time.sleep(1.5)
# Unión de conjuntos
union = conjunto1.union(conjunto2)
print(union)
# Resultado: {1, 2, 3, 4, 5, 6}
time.sleep(1.5)
print("Ahora realizamos la operacion de interseccion entre A y B el resultado es: ")
time.sleep(1.5)
# Intersección de conjuntos
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)
# Resultado: {3, 4}
time.sleep(1.5)
print("Ahora realizamos la operacion de diferencia entre A y B el resultado es: ")
time.sleep(1.5)
# Diferencia entre conjuntos
diferencia = conjunto1.difference(conjunto2)
# Resultado: {1, 2}
print(diferencia)

# Comprobar si un elemento está en un conjunto
print(2 in conjunto1)  # Devuelve True

