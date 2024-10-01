from itertools import permutations, combinations_with_replacement

# Obtener permutaciones de ["a", "b", "c"]
perms = permutations(["a", "b", "c"])
perms_list = list(perms)  # Convertir a lista para imprimir

print("Permutaciones de ['a', 'b', 'c']: ")
print(perms_list)

# Obtener combinaciones con reemplazo de ["a", "b", "c"] con tamaños 1 y 2
array = ["a", "b", "c"]
perms2 = combinations_with_replacement(array, 2)  # Aquí se usa 2 en lugar de [1, 2]
perms2_list = list(perms2)  # Convertir a lista para imprimir

print("\nCombinaciones con reemplazo de ['a', 'b', 'c'] y tamaño 2: ")
print(perms2_list)



