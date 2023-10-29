"""
    Crea un programa en Python que permita a los usuarios realizar las siguientes operaciones en una lista de elementos:

Agregar un elemento a la lista.
Eliminar un elemento de la lista.
Mostrar todos los elementos de la lista.
Salir del programa.
"""
def showElements(arreglo):
    print("Elementos que hay en la lista")
    for elemento in arreglo:
        print(elemento)
        
def addElement(arreglo):
    elemento = input("Ingrese el nombre del elemento\n")
    arreglo.append(elemento)

def deleteElement(arreglo):
    elemento = input("ingrese el nombre del elemento a eliminar")
    #verificamos si existe
    if elemento in arreglo:
        arreglo.remove(elemento)
        print("elemento eliminado con exito")
    else:
        print("el elemento no se encuentra en la lista")
        
def mostrarMenu():
    print("1. Agregar un elemento")
    print("2.eliminar elemento")
    print("3.mostrar elementos")
    print("4.salir")
    opcion = int(input("ingrese la opcion a realizar\n"))
    return opcion

#aca iniciara el programa
arreglo = []
opcion = 0
while opcion != 4:
    opcion = mostrarMenu()
    print(opcion)
    
    match opcion:
        case 1: addElement(arreglo)
        case 2: deleteElement(arreglo)
        case 3: showElements(arreglo)




