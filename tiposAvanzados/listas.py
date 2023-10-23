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