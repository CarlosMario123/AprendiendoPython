import cv2

# Cargar una imagen desde el archivo
image = cv2.imread("openCV/ita.jpg")

if image is None:
    print("Error: No se puede cargar la imagen.")
else:
    # Mostrar la imagen original
    cv2.imshow('Original Image', image)

    while True:
        # Esperar a que se presione una tecla
        key = cv2.waitKey(0) & 0xFF

        # Verificar si se presiona una tecla válida
        if key == ord('a'):  # Presionar 'a' para 400 x 400
            new_dimensions = (400, 400)
        elif key == ord('b'):  # Presionar 'b' para 600 x 400
            new_dimensions = (600, 400)
        elif key == ord('c'):  # Presionar 'c' para 1000 x 100
            new_dimensions = (1000, 100)
        elif key == ord('q'):  # Presionar 'q' para salir
            break
        else:
            continue  # Si se presiona una tecla no válida, continuar el bucle

        # Redimensionar la imagen
        resized_image = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_LINEAR)

        # Mostrar la imagen redimensionada
        cv2.imshow('Original Image', resized_image)
        #por lo que vi el primer parametro es como un nombre a la referencia donde estaria esa imagen
        
      
            
           

    # Cerrar todas las ventanas
    cv2.destroyAllWindows()


