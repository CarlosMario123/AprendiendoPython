from selenium import webdriver

# Inicializar el navegador
driver = webdriver.Firefox()

# Abrir una página web
driver.get("https://platinum.upchiapas.edu.mx/alumnos/login")

# Definir el script JavaScript para obtener todos los enlaces de la página
script = """
var links = document.querySelectorAll('a');
var endpoints = [];
for (var i = 0; i < links.length; i++) {
    var href = links[i].getAttribute('href');
    endpoints.push(href);
}
return endpoints;
"""

# Ejecutar el script JavaScript para obtener los enlaces de la página
endpoints = driver.execute_script(script)

# Imprimir los enlaces obtenidos
for endpoint in endpoints:
    print(endpoint)

# Cerrar el navegador
driver.quit()
