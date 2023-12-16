from Notas import Notas
from Gestor import Gestor
def manejarOpciones(opcion):
    match opcion:
        case 1: crearNota()
        case 2: eliminarNota()
        case 3:actualizaNota()
        case 4:visualizar()
            
            
def crearNota():
    nombre = input("ingrese el nombre para su nota: ")
    contenido = input("ingrese el contenido para su nota\n")
    Notas(nombre,contenido).crear() 

def eliminarNota():
    nombre = input("ingrese el nombre de la nota a eliminar")
    Gestor().eliminarArchivo(nombre)
    
def actualizaNota():
    nombre = input("Nombre de la nota a actualizar")
    if(Gestor().verificarExistencia(nombre)):
        print("archivo encontrado")
        contenido = input("ingrese el nuevo contenido a la nota \n")
        Gestor().actualizarNota(nombre,contenido)
    else:
        print("archivo no encontrado") 

def visualizar():
    nombre = input("Nombre de la nota a visualizar")
    if Gestor().verificarExistencia(nombre):
        for text in Gestor().view(nombre):
            print(text)
    else:
        print("archivo no encontrado")   
                      
         
    