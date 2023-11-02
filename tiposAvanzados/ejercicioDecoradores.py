#decorador que permite medir tiempo de ejecucion de una funcion
import time
def medirTiempo(funcionParam):
    #funcion que envuelve a la funcion
    def wrapper(*args):
        #creamos una variable de inicio para empezar a medir el tiempo
        inicio = time.time()
        resultado = funcionParam(*args)
        #mide el tiempo final
        fin = time.time()
        print(f"La función {funcionParam.__name__} tomó {fin - inicio} segundos en ejecutarse")
        return resultado
    return wrapper

@medirTiempo
def contador():
    for i in range(100):
        print(i)

contador()      


#decorador que permite manejar exepciones
def manejo_de_excepciones(mensaje_error):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            try:
                resultado = funcion(*args, **kwargs)
                print("sin exepciones")
                return resultado
            except Exception as e:
                print(f"Error: {mensaje_error}")
                return None
        return wrapper
    return decorador

@manejo_de_excepciones("Hubo un error en la función")
def funcion_con_error():
    return 1 / 0

funcion_con_error()  # Imprime el mensaje de error, pero no provoca una excepción no controlada

@manejo_de_excepciones("error al parsear el numero")
def parsearNumero():
    number = int(input("ingrese un numero a parsear"))
    
    
parsearNumero()    



def validar_argumentos(funcion):
    def wrapper(*args, **kwargs):
        if all(arg > 0 for arg in args):
            return funcion(*args, **kwargs)
        else:
            return "Argumentos inválidos: deben ser números positivos"
    return wrapper

@validar_argumentos
def funcion_positiva(a, b):
    return a + b

print(funcion_positiva(3, 4))  # Resultado válido
print(funcion_positiva(-2, 5))  # Argumentos inválidos

  
    