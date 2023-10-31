# Creamos nuestro diccionario de productos
productos = {}

# Función para crear productos
def createProduct():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    productos[nombre] = {
        "precio": precio,
        "cantidad": cantidad
    }
    print(f"{nombre} ha sido registrado con éxito.")

# Función para mostrar un producto específico
def showOneProduct():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    if nombre in productos:
        data_product = productos.get(nombre)
        print("Nombre del producto:", nombre)
        print("Precio del producto: ", data_product["precio"])
        print("Cantidad del producto: ", data_product["cantidad"])
    else:
        print("Producto no encontrado.")

# Funcion para mostrar todos los productos en stock
def showAllProduct():
    print("Productos en stock:")
    for nombre, valor in productos.items():
        print("____________________________")
        print("Nombre del producto: ", nombre)
        print("Precio del producto: ", valor["precio"])
        print("Cantidad: ", valor["cantidad"])

# Funcion para calcular el valor total del inventario
def calculateInventoryValue():
    total = sum(producto["precio"] * producto["cantidad"] for producto in productos.values())
    print(f"El valor total del inventario es: ${total:.2f}")

# Funcion para eliminar un artículo del inventario
def deleteProduct():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in productos:
        del productos[nombre]
        print(f"{nombre} ha sido eliminado del inventario.")
    else:
        print("Producto no encontrado.")

# Funcion para actualizar la cantidad en stock de un artículo
def updateStock():
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    if nombre in productos:
        nueva_cantidad = int(input("Nueva cantidad en stock: "))
        productos[nombre]["cantidad"] = nueva_cantidad
        print(f"La cantidad en stock de {nombre} ha sido actualizada.")
    else:
        print("Producto no encontrado.")

# Función para mostrar el menú
def showMenu():
    print("Seleccione una opción")
    print("1. Añadir producto")
    print("2. Mostrar un producto")
    print("3. Mostrar todos los productos")
    print("4. Calcular valor total del inventario")
    print("5. Eliminar producto")
    print("6. Actualizar cantidad en stock")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")
    return int(opcion)

# Inicia el programa
contador = 0
while contador != 7:
    opcion = showMenu()

    match opcion:
        case 1:
            createProduct()
        case 2:
            showOneProduct()
        case 3:
            showAllProduct()
        case 4:
            calculateInventoryValue()
        case 5:
            deleteProduct()
        case 6:
            updateStock()
        case 7:
            print("¡Hasta luego!")
            contador = 7
        case _:
            print("Opción no válida. Por favor, elija una opción válida.")
  
        
        
   
         