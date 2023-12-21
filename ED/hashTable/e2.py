def son_anagramas(cadena1, cadena2):
    # Si las longitudes de las cadenas son diferentes, no pueden ser anagramas
    if len(cadena1) != len(cadena2):
        return False
    
    # Crear tablas hash para almacenar la frecuencia de caracteres de cada cadena
    frecuencia_cadena1 = {}
    frecuencia_cadena2 = {}

    # Contar la frecuencia de caracteres en la primera cadena
    for char in cadena1:
        if char in frecuencia_cadena1:
            frecuencia_cadena1[char] += 1
        else:
            frecuencia_cadena1[char] = 1

    # Contar la frecuencia de caracteres en la segunda cadena
    for char in cadena2:
        if char in frecuencia_cadena2:
            frecuencia_cadena2[char] += 1
        else:
            frecuencia_cadena2[char] = 1

    # Verificar si las tablas hash son iguales (mismas frecuencias de caracteres)
    print(frecuencia_cadena1)
    print(frecuencia_cadena2)
    return frecuencia_cadena1 == frecuencia_cadena2

# Ejemplos
cadena_1 = "listen"
cadena_2 = "silent"

if son_anagramas(cadena_1, cadena_2):
    print(f"'{cadena_1}' y '{cadena_2}' son anagramas.")
else:
    print(f"'{cadena_1}' y '{cadena_2}' no son anagramas.")
