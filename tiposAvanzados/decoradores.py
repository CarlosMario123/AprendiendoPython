""" decoradores 
¿Que es un decorador?

son funciones que a su vez añaden funcionalidades a otras funcion"""
import time

def funcionDecoradora(funcionParametro):
    #ponemos la convecion arg que quiere decir que va a recibir parametro
    def funcionInterior(*args):
    #acciones adicionales que decoran
      print("realizando el calculo...")
      time.sleep(2)
      funcionParametro(*args)
      print("hemos terminado de realizar los calculoas")
    return funcionInterior


#decoramos alguna funciom
@funcionDecoradora
def suma(num1,num2):
    print(num1 + num2)
  
@funcionDecoradora    
def potencia(base,exp):
    print(pow(base,exp))    
    

suma(1,12)
potencia(2,3)

            