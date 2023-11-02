#a(b) --> c

""" tenenmos una funcion a que recibira como parametro a 
y retornara c"""

#no podiamos guiar de esta estructura para crear un decorador en python
def funcion_a(funcion_b):
    def funcion_c():
        print("antes de la ejeccion")
        funcion_b()
        print("Despues de la ejecucion")
         
    return funcion_c


@funcion_a
def hola():
    print("esta es la funcion hola")
    
hola()   