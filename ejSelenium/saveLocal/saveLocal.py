import time
import requests
from util.afterPointStr import obtener_subcadena_despues_de_punto_al_reves
from util.generateNamefile import generar_nombre_archivo
from util.stopDoublePoint import StopDoublePoint
def saveLocalFile(url):
    typeFile = obtener_subcadena_despues_de_punto_al_reves(url)
    name = f"{generar_nombre_archivo('imagen')}.{typeFile}"
    #empieza con htpps or data
    startData = StopDoublePoint(url)
    
    if(startData == "http:" or startData == "https:"):
        respuesta = requests.get(url)
        saveFileHttp(name,respuesta)
    else:
        return
    
    
    
    
    
def saveFileHttp(name,respuesta):
     
    with open(f"imagenes/{name}", "wb") as archivo:
        archivo.write(respuesta.content)
        print("guardando archivo espere....")
        time.sleep(1)
        print(f"La imagen se ha guardado como '{name}'.")
        
        
        