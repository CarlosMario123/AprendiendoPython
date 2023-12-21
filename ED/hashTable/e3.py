def encontrar_pares(lista, objetivo):
    tabla_hash = {}
    pares = []

    for num in lista:
        complemento = objetivo - num

        if complemento in tabla_hash:
            print(complemento,num)
            pares.append((complemento, num))

        tabla_hash[num] = True

    return pares

# Ejemplo de uso
numeros = [3, 5, 8, 2, 4, 7]
objetivo = 10

resultado = encontrar_pares(numeros, objetivo)
print(resultado)  # Mostrará los pares que suman el valor dado
