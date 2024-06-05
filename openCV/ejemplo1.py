# LEER, VISUALIZAR y GUARDAR UNA IMAGEN
import cv2

#crearemos una variable para la imagen que vamos a leer 
imagen = cv2.imread("openCV/ita.jpg")

#para visualizarla utilizaremos el siguiente metodo cv2

cv2.imshow("Visualizar imagen",imagen)

cv2.waitKey(0) #cuando se waitkey con 0 esto nos dice que se tiene que esperar que se toque una tecla

cv2.destroyAllWindows()#Para asegurarse de que todas las ventanas se cierren al terminar el script, evitando que queden abiertas.