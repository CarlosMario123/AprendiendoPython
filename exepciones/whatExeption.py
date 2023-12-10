try:
    numero = int(input("ingresa un numero \n"))
     
except Exception as e:
    print(type(e)) #imprimiremos que tipo de exepccion es   
#si cae un errror marca ValueError
#type nos marca el tipo de error


"""
Errores de sintaxis (SyntaxError)

Estos errores ocurren cuando el código no sigue la sintaxis 
correcta de Python y, por lo tanto, no puede ser interpretado correctamente por el intérprete

Estos son errores que ocurren durante la ejecución del programa y 
pueden ser manejados mediante bloques try-except. Algunos ejemplos comunes:
TypeError: Ocurre cuando se realiza una operación en un tipo incorrecto.

ZeroDivisionError: Ocurre cuando intentas dividir por cero.


IndexError: Ocurre cuando intentas acceder a un índice que está fuera del rango de una secuencia.

NameError: Ocurre cuando intentas usar una variable o nombre que no está definido.
"""    
    