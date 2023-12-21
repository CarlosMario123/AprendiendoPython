"""
Dada una lista de elementos, verifica si hay algún elemento 
duplicado en la lista utilizando una tabla hash
"""

#funcion que verifica que no haya elementos repetidos
def verificarRepetido(lista):
    frecuencia = {}
    #iteramos el arreglo para guardarlo en la lista
    for element in lista:
        #verificamos si existe
        if element in frecuencia:
            frecuencia[element] += 1#si ya exist seguimos contando
        else:#caso contrario creamos y sumamos 1 que quiere decir que aparecio
            frecuencia[element] = 1
    #ahora contamos que elementos son mayo a 2 que quiere decir que se repito
    repetidos = []
    for element in frecuencia: #recorremos frecuencia que nos dara la clave para acceder al valor
        if frecuencia[element] > 1:
            repetidos.append(element) 
    return repetidos          
    


#arreglo

lista = ["pato","perro","casa","perro","pato","vaca"]


print("elementos repetidos")
for element in verificarRepetido(lista):
    print(element)