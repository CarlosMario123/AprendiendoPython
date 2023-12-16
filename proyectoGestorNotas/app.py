#menu en consola
from opcionesNotas import manejarOpciones 
print("Bienvenido a tu gestor de notas")
opcion = 0
while opcion != 5:
    print("1-Crear Nota")
    print("2-Eliminar notas")
    print("3-actualizar nota")
    print("4-visualizar nota")
    print("5-Salir")
    opcion = int(input("ingrese su opcion: "))
    manejarOpciones(opcion)
    