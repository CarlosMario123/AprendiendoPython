import requests
from bs4 import BeautifulSoup

url = "https://unsplash.com/es/t/wallpapers"

respuesta = requests.get(url).text #esencialmente para traer las imagenes de splash

#ahora creamos el objeto beautifulsoup
soup = BeautifulSoup(respuesta,"html.parser")

#selecionaremos los wallpapers imagenes de esa pagina

imagenes = soup.select("img")
for imagen in imagenes:
    print(imagen.get("src"))
    print
