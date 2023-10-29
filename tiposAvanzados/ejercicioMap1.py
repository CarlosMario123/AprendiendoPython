#convertir nombres a mayuscula
nombres = ["carlos","pepe","plutarco","sofia","david"]
numbers = [2,4,1,4,3,4,5,21]
#aplicamose el mapeo
print("ejercicios convertir nombres a mayuscula")

nameUpper = list(map(lambda name:name.upper(),nombres))

print("nombres en mayus: ",nameUpper)

#Calcular longitudes de cadenas
print("calcular longitudes de cadena")
listSize = list(map(lambda x:len(x),nombres))
print("longitud de las cadenas",listSize)

#Calcular el cuadrado de los números pares y el cubo de los impares:
def calculateCC(number):
    if number % 2 ==0 :
        return pow(number,2)
    return pow(number,3)

print("Calcular el cuadrado de los números pares y el cubo de los impares:")

potenciado = list(map(lambda x:calculateCC(x),numbers))

print(potenciado)


#concatenar dos listas
print("concatenar dos lista")
nombres = ["Juan", "María", "Pedro", "Laura"]
apellidos = ["Gómez", "Pérez", "Sánchez", "Rodríguez"]
resultado = list(map(lambda x, y: x + " " + y, nombres, apellidos))
print("listas concatenadas: ",resultado)