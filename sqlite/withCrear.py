#aca creaeremos una tabla 
import sqlite3

#hacerlos con with
with sqlite3.connect("app.db") as con:
    cursor = con.cursor()#con cursor creamos una consulta
    # Comando SQL para crear la tabla "Personas" 
    creartabla = ''' CREATE TABLE IF NOT EXISTS Personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER
    )
'''#para ejecutar ejecutamos execute: 
    cursor.execute(creartabla)