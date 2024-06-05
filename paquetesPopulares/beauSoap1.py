import requests
from deep_translator import GoogleTranslator #libreria para traduccion
from bs4 import BeautifulSoup
import time

"""
A diferencia de usar selenium comparado con beautifulsoup es que selenium tiene manipulacion en el navegador
y beautifulsoup no este recibe un html permite procesarlo 
"""

url = "https://stackoverflow.com/questions"
urlBase ="https://stackoverflow.com"
respuesta = requests.get(url)

texto = respuesta.text

#ahora creamos el objeto beautifulsoup
soup = BeautifulSoup(texto,"html.parser")
preguntaHtml = [] #arreglo que nos servira para almacenar pagina

#selecionaremos un tipo de pregunta a travez de un selector
preguntas = soup.select(".s-post-summary--content")

#obtener url de las paginas solo etiqueta a
enlaces =  soup.find_all('a',class_="s-pagination--item js-pagination-item")

enlacesVisitar = []

for link in enlaces:
    text = urlBase + link.get("href")#.get nos permitra traer el href nota sin no tiene un href provocar un error :()
    enlacesVisitar.append(text)


#ahora realizaremos mas peticiones 
for enlace in enlacesVisitar:
    response = requests.get(enlace)
    time.sleep(1)
    soup = BeautifulSoup(response.text,"html.parser")
    #selecionaremos masivamente las preguntas
    preguntaHtml.append(soup.select(".s-post-summary--content"))
    


counter = 1
#guardar todas las preguntas en un archivo.txt
with open('preguntas.txt', 'w', encoding='utf-8') as file:
    for pregunta in preguntaHtml:
        for p in pregunta:
            translated = GoogleTranslator(source='auto', target='es').translate(p.select_one('.s-link').get_text())
            textQuestion = (
            f"Pregunta {counter}\n"
            f"{translated}\n"
            f"usuario: {p.select_one('.s-user-card--link').get_text()}\n"
            )
            file.write(textQuestion)
            counter += 1


    



#ejemplo para un html
""" 

for idx, p in enumerate(preguntas, start=1):
 
    print(f"Pregunta {idx}")
    print(p.select_one(".s-link").get_text())
    print("usuario: ",p.select_one(".s-user-card--link").get_text())
    print()
    
    
"""


    

