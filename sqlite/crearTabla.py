#aca creaeremos una tabla 
import sqlite3

con = sqlite3.connect("app.db")

cursor = con.cursor()#con cursor creamos una consulta
#para ejecutar ejecutamos execute:

# Comando SQL para crear la tabla "Personas"
creartabla = '''
    CREATE TABLE IF NOT EXISTS Personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER
    )
'''
cursor.execute(creartabla)
# Guardar los cambios para compremeterlo a la base de datos
con.commit()
#cerramos
con.close()