#usando la variable de entorno
from dotenv import load_dotenv
import os

load_dotenv()#cargamos la variables de entorno

#imprimiremos el valor de la variable de entorno
print(os.getenv("BD_FAKE"))