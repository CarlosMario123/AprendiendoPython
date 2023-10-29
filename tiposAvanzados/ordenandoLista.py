""" 
con lo aprendido en la clase se vio dos manera de ordenar elementos en python

la primera manera es usar el metodo un arreglo que es .sort()

y el el otro es solo una funcion llamada sorted() que recibe como parametro
un arreglo y devuelve un nuevo arreglo con los valores del arreglo original pero sin afectar el arreglo original vemos

"""
#arreglo que se utilizar el metodo sort()
arreglo1 = [64,32,5,4,8,1,3,4,2]
#arreglo que utilizara el metodo sorted()
arreglo2 = [64,32,5,4,8,1,3,4,2]

arreglo1.sort()
print("arreglo1: ",arreglo1)

aux = sorted(arreglo2)
print("arreglo2: ",arreglo2)
print("arreglo aux: ",aux)