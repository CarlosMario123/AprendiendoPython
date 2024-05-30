#usando la variable de entorno
from dotenv import load_dotenv
import os
from sendgrid.helpers.mail import Mail#objeto para crear correo

from sendgrid import SendGridAPIClient #modulo que nos permite enviar el correo

load_dotenv()#cargamos la variables de entorno
key = os.getenv("SENDGRIDAPI")
email = os.getenv("EMAILGRID")

mensaje = Mail(
    from_email=email,#corro donde enviaremos
    to_emails="car06ma15@gmail.com",#correo donde enviaremos
    subject="Correo de prueba",#titulo de lo correo
    html_content= "curso de <b>ultimate</b>"#mensaje
    
)

try:
    sg = SendGridAPIClient(key)
    respuesta = sg.send(mensaje)#enviamos el ojeto Mail creado que es el mensaje
    print("Mensaje enviado: " )
    print(respuesta.status_code)
    print(respuesta.body)
    print(respuesta.headers)
except Exception as e:
    print(e)
