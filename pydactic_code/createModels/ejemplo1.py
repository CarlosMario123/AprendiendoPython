from pydantic import BaseModel,Field
from datetime import datetime
from typing import List
#crearemos nuestro primer modelo

class User(BaseModel):
    name:str
    age:int = Field(strict=True)#este campo es obligatoriamente estricto y numerico
    dateCreated:datetime
    hobbies:List[str]

#empezaremos a crear un usuario
user = User(name="John", age=30, dateCreated=datetime.now(), hobbies=["music", "art"])
print(user.json()) #podemos imprimir en su estructura json

#intentaremos crear uno pero con error
try:
    userError = User(name="John", age="30", dateCreated=datetime.now(), hobbies=["music", "art"])

except Exception as e:
    print("Error al crear el usuario")
    print(e)