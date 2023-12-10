class Model:
    tabla = False
    def __init__(self):
        if not self.tabla:
            print("error tienes que definir una tabla")
    
    def guardar(self):
        print(f"Guardando {self.tabla} en la base de datos")
    @classmethod    
    def buscarById(self,_id):
        print(f"buscando el id:{id} en la table {self.tabla}")   
        

#creamos una clase de usuario

class Usuario(Model):
    tabla = "usuario"#la tabla hacemos referencia al que le pertenece modelo                
    
#creamos una clase para venta
class Venta(Model):
       tabla = "Venta"
    
    
#cremos una tablar usuario

usuario = Usuario()
usuario.guardar()

venta = Venta()
venta.guardar()
    