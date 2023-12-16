from pathlib import Path
class Notas():
    def __init__(self,nombre,contenido):
        self.nombre = nombre
        self.contenido = contenido
        self.ruta = Path("rutasNotes/") / nombre 
    def crear(self):
        rutaExtension = self.ruta.with_suffix('.txt')
        with open(rutaExtension,"w",encoding='utf-8') as archivo:
            archivo.write(self.contenido)
        #w de write o esciruta
        
        
  
        