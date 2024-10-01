from pydantic import BaseModel,Field
from typing import List

class Producto(BaseModel):
    id:int
    name:str
    price: float = Field(gt=0, description="El precio debe ser mayor que cero")#validamos que sea mayor que cero
    stock: int = Field(ge=0, le=100, description="El stock debe estar entre 0 y 100")
    
    
    

class Inventario(BaseModel):
    products: List[Producto] = []
    def getProducts(self)->List[Producto]:
        return self.products
    
    def addProduct(self, product:Producto):
        self.products.append(product)

def createProduct(inventario:Inventario):
    id = len(inventario.getProducts()) + 1
    name = input("Ingrese el nombre del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad del producto: "))
    
    try:
        product = Producto(id=id, name=name, price=price, stock=stock)
        inventario.addProduct(product)
        print("El producto fue creado exitosamente")
    except Exception as e:
        print(e)
        print("Error al crear el producto")
      

if __name__ == "__main__":
    value = ""
    inventario = Inventario()
    while value != "x":
        print("**********************************************************")
        print("               Inventarios de productos")
        print("**********************************************************")
        print("1- Crear un nuevo producto")
        print("2- Listar todos los productos")
        print("3-Ver productos en formato json")
        print("x-salir")
        value = input("Elija una opcion: ")
        
        match value:
            case "1":
                createProduct(inventario)
            case "2":
                print(inventario.getProducts())
            case "3":
                print(inventario.json())
            case "x":
                print("Hasta pronto")
            case _:
                print("Opcion no valida")
    

