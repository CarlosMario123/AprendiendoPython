import requests
#requests en como el fetch o axios de javascript sirve para realizar peticiones rest 
url = "https://jsonplaceholder.typicode.com/users"

r = requests.get(url,timeout=10)

try:
    json_data = r.json()  # Convertir la respuesta a JSON
    for dato in json_data:
        print(dato)
        print()
except ValueError as e:
    print("Error al convertir a JSON:", e)