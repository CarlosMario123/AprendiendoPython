#se tiene un arreglo con este contenido

mascotas = ["pulguitas","oso","solovino","Caguamo"]

""""para repasar lo aprendido anteriomente los arreglo se pueden acceder por medio de subindices
los subindices comienzan en 0 y van aumentando, es decir el primer elemento del arreglo esta almacenado
hasta llegar al elemento n - 1

ejemplo

print(mascotas[0]) //Resultado => pulguitas
"""

"""otra cosa interesante de manipular arreglos como imprimir a un cierto rango 
supongamos que queremos ver desde la posicon 0 hasta las 2 de arreglo podemos agregar una notacion 
en los corchete de los arreglos esta manera

Ejemplo:

arreglo[0:3]

cuando lo dejamos de esta manera

arreglo[:3] --> por defecto el valor inicial es cero

Tambien podemos definir un inicio
arreglo[1:3] --> 

veamos ejemplos en codigo
"""

print(mascotas[0:3])
print(mascotas[1:3])


#desempaquetar listas en python 
print("aprendiendo desempaquetar listas")

#tenemos de ejemplo una lista de numeros y queremos pasarla a variable
listaNum = [1,2,3]

"""
hacer de esta manera en python esta bien

num1 = listaNum[0]
num2 = listaNum[1]
num3 = listaNum[2]

pero en python existe una manera mas elegante de hacerlo veamos como se hace:
 """
 
#procedemos a desempaquetar
num1,num2,num3 =  listaNum
print(f"{num1} {num2} {num3}") #imprime 1 2 3

""" pero que tal si ahora solo quisieramos desempaquetar
el primer elemento de la lista realizamos esto
"""

num1,*otros = listaNum
"""
pero que hizo la setencia anterior como se va desempaquetando los
elementos de izquierda a derecha al poner la primera variabla num1
extraimos el valor de la posicion 0 despues al usar * en la variable siguiente
obtenemos los elementos restantes
"""

print("valor de una variable que extraimos ",num1)


#iterar listas

print("seccion de iterar listas")

mascotas = ["Max", "Bella", "Lucy", "Charlie", "Luna", "Cooper", "Daisy", "Bailey", "Rocky", "Molly","Max"]

#procedemos a iterar
for mascota in mascotas:
    print("hola me llamo",mascota)

"""este for nos permite mostrar las mascotas de manera enumerada
pero para eso usamos la funcion enumerate y asu vez utilizando un index 
que sera el indice de nuestro arreglo"""  
for index,mascota in enumerate(mascotas):
    print(index,mascota)    


    
""" cosas adiccionales utiles en python si queremos verificar
que un elemntos se encuentra en la lista podemos crear como un tipo de 
if con un for condional aqui va el ejemplo """  


name = input("ingrese el nombre de una mascota")
if name in mascotas:
    print("Esta mascota se encuentra en la lista")
else:
    print("Esta mascota no se encuentra en la lista")
    
"""
otro funcion adicional existe un metodo en los arreglos para saber el indices de elemento
pasado por parametro pero cuidado si no lo encuentra este no mandara un error en consola 
el metodo es .index()

veamos como usarlo
"""
print("la mascota Luna se encuentra en la posiscion: ",mascotas.index("Luna"))

"""
otro metodo util de los arreglos es el metodo .count() este metodo 
se usa para saber cuantas veces aparace un elementos con ese mismo valor pasado por parametro

"""

print("las veces que aparece max en la lista: ",mascotas.count("Max"))