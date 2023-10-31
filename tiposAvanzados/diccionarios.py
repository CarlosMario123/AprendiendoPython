""" diccionario es una estructura de datos que te permite almacenar pares de clave-valor.
Cada elemento en un diccionario consta de una clave única y su correspondiente valor. 
Los diccionarios son extremadamente útiles cuando necesitas 
asociar datos o valores con identificadores específicos en lugar de usar índices numéricos, c
omo en las listas o tuplas"""
# Crear un diccionario con llaves
mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}

# Crear un diccionario con la función dict()
otro_diccionario = dict(clave1="valor1", clave2="valor2", clave3="valor3")

#acceso a elementos de dicinario
print(mi_diccionario["clave1"])  # Acceder al valor asociado a la clave "clave1"

#otra manera de accedar es con su metodo get
print(mi_diccionario.get("clave3")) 

#modificar elementos
mi_diccionario["clave1"] = "nuevo_valor"  # Modificar un valor existente
mi_diccionario["nueva_clave"] = "nuevo_valor"  # Agregar una nueva clave y valor

#eliminar Elementos
del mi_diccionario["clave1"]  # Eliminar un elemento por clave

#reccorrer un dicionario
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

#comprobar si una clave existe
if "clave1" in mi_diccionario:
    print("La clave existe")
