from pathlib import Path
class Gestor():
    def __init__(self):
        self.ruta = Path("rutasNotes/")
    def eliminarArchivo(self,nombre):
        direcion = self.ruta / nombre
        direcion = direcion.with_suffix('.txt')
        if direcion.exists():#si existe eliminamos el archivo
            direcion.unlink()
            print("archivo eliminado correctamente")
        else:
            print("El archivo no existe")
            
    def verificarExistencia(self,nombre):
        direcion = self.ruta / nombre
        direcion = direcion.with_suffix('.txt')
        return direcion.exists()
    def actualizarNota(self,nombre,contenido):
        direcion = self.ruta / nombre
        direcion = direcion.with_suffix('.txt')
        direcion.write_text(contenido,"utf-8")
    
    def view(self,nombre):
        direcion = self.ruta / nombre
        direcion = direcion.with_suffix('.txt')
        return direcion.read_text("utf-8").split("\n")
       
        
        
        
        