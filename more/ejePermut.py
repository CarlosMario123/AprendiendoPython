from itertools import permutations

# Definir las letras y vocales a considerar
letras = ["a", "e", "b", "c", "d", "f", "g"]
vocales = ["a", "e"]

# Generar todas las permutaciones
perms = permutations(letras)
# Lista para almacenar las permutaciones válidas
permutaciones_validas = []

# Filtrar las permutaciones donde la vocal esté al inicio y al final
contar = 0
for perm in perms:
    contar = contar + 1
    if perm[0] in vocales and perm[-1] in vocales:
       
        permutaciones_validas.append(perm)

print(contar)
print("Total de permutaciones donde una vocal está al inicio y al final:", len(permutaciones_validas))
