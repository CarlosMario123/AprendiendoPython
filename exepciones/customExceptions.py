#veremos como crear exepciones personalizadas
#algo que debemos sabes es que mandar demasiadas exepciones puede afectar el rendimiento de nuestra app


#primer paso crear una clase y heredar Exeption

class CustomExeption(Exception):
    "Esta es una clase personalizada para mi error"
    
#hacemos la misma prueba

def division(n=0):
    if n == 0:
        raise CustomExeption("Error de division pero personalizada carnal")
    return 5/n

#capturamos el error con un try

try:
    division()
except CustomExeption as e:
    print(e)            