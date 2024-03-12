#Crea un script que liste todos los archivos de un directorio especificado.
import os
#primero crearemos una funcion que se encargara de listar atravez de una ulr

def listFiles(ruta):
    print("---------------------------------------------------------------------")
    print("                   informacion del directorio")
    print("---------------------------------------------------------------------")
    carpetas = []
    archivitos = []
    try:
        archivos = os.listdir(ruta)
        for  indice, archivo in enumerate(archivos, start=1):
             #ruta completa
            ruta_completa = os.path.join(ruta,archivo)
            print(indice,":",archivo,"ruta: :",ruta_completa)
            #clasifcamos solo carpeta
            if(os.path.isdir(ruta_completa)):
                name = f"{archivo} ruta: : {ruta_completa}" 
                carpetas.append(name)
            else:
                archivitos.append(f"{archivo} ruta: : {ruta_completa}")    
                
        print("-----------------------------------------------------------------")
        print("carpetas:")
        for carpeta in carpetas:
            print(carpeta)  
        print("-----------------------------------------------------------------")
        
        print("-----------------------------------------------------------------")
        print("archivos:")
        for file in archivitos:
            print(file)  
        print("-----------------------------------------------------------------")        
    except Exception as e:
        print("ha ocurrido un error")
        print(e)    
        
    
listFiles("C:/Users/car06/OneDrive/Escritorio/PY/learnPy")        