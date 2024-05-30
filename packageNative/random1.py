#from random import random,randint,choice funciona tambien asi
#imprimiendo solo random para ver el resultado
import random
print(random.randint(1,6)) #randint nos permite generar numeros aleatorios entre rango de numeros a,b


lista = [1,2,3,4,5,6]

print(random.choice(lista))

# Selecciona 50 elementos de lista
print(random.choices(lista, k=50))

# Desordena la lista
random.shuffle(lista)

# Imprime la lista desordenada
print(lista)