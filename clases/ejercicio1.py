class Libro:
    #constructor para nuestro libro
    def __init__(self,autor,genero,titulo):
          self.autor = autor
          self.genero = genero
          self.titulo = titulo
          self.__disponible = True
          
    def prestar(self):
        self.__disponible = False
        print("El libro ha sido prestado")
        
    def devolver(self):
        self.__disponible = True
        print("El libro ha sido devuelto")
    
    #metodo que verica si el libro esta disponible 
    def isAvailable(self):
        print("El libro está disponible" if self.__disponible else "El libro no está disponible")
        return self.__disponible
  
    def viewInfo(self):
        print(f"Nombre del libro: {self.titulo}")
        print(f"Autor del libro: {self.autor}")
        print(f"Genero del libro: {self.genero}")



class Biblioteca:
    libros = []
    @classmethod
    def addBook(cls,book):
        cls.libros.append(book)
    #metodo que permite mostrar todos los libros
    @classmethod    
    def showAllBook(cls):
        if(len(cls.libros) == 0):
            print("No hay libros en la biblioteca")
        else:
            for libro in cls.libros:
                libro.viewInfo()

    #metodo que busca un libro por su titulo y lo muestra
    @classmethod
    def showOneBook(cls, titulo):
        encontrado = False
        for libro in cls.libros:
            if libro.titulo == titulo:
                print(f"Información del libro '{titulo}':")
                libro.viewInfo()
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró el libro con el título '{titulo}' en la biblioteca")
            
    @classmethod
    def removeBook(cls, titulo):
        for libro in cls.libros:
            if libro.titulo == titulo:
                cls.libros.remove(libro)
                print(f"El libro '{titulo}' ha sido eliminado de la biblioteca.")
                return
        print(f"No se encontró el libro con el título '{titulo}' en la biblioteca, por lo que no se pudo eliminar.")
        


def showMenu():
    print("1)agregar libro")
    print("2)Ver todos los libros")
    print("3)ver libro")
    print("4)Eliminar libro")
    print("5)salir")
    return int(input("Selecione una opcion\n"))

def optionAdd():
    autor= input("ingrese autor:\n")
    genero = input("ingrese el genero de libro\n")
    titulo = input("ingrese el titulo del libro:\n")
    print("libro creado exitosamente")
    return Libro(autor,genero,titulo)

def controlarMenu(opcion):
    match opcion:
        case 1: Biblioteca.addBook(optionAdd())
        case 2:Biblioteca.showAllBook()
        case 3:Biblioteca.showOneBook(input("ingrese el titulo del libro\n"))
        case 4:Biblioteca.removeBook(input("ingrese el titulo del libro\n"))
        case 5:print("hasta luego")
        case _:print("opcion no encontrada")
 
                    
#menu de ejecucion
opcion = 0
while(opcion != 5):
    opcion = showMenu()
    controlarMenu(opcion)
                
        