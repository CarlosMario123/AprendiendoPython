#para reaizarr esta practica lanzaremos la exepcion DivisionZero
#raise nos permite lanzar un mensaje de exepcion

#----------------------------------------------------------------
#creamos una funcion de division para capturar el error

def division(n=0):
    if n ==0:
        #raise nos permitira mandar la expecion
        raise ZeroDivisionError("Ey brother recuerda no se puede dividir entre cero")
    return 4/n

#llamamos nuestra funcion vamos utilizar el try catch para que funcione

try:
    division()
except ZeroDivisionError as e:
    print(e) #enviare el mensaje que pusimo en la funcion division
    