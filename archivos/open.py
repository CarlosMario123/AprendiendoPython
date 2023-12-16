#importamos open
from io import open

#solo escritura
texto = "hola mundo"
#w es para write
archivo = open("prueba.txt","w",encoding="utf-8")

#ahora si lo escribimos y pasamos el texto
archivo.write(texto)
#siempre cuando usamos open que nos olvide cerrar el archivo ya que nos puede consumir memoria
archivo.close()