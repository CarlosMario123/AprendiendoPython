import sqlite3

# Datos de ejemplo para insertar en la tabla
datos_personas = [
    ("Juan", 25),
    ("María", 30),
    ("Carlos", 28)
]

# Comando SQL para crear la tabla y para insertar datos
crear_tabla = '''
    CREATE TABLE IF NOT EXISTS Personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER,
        correo TEXT UNIQUE
    )
'''

insert_query = '''
    INSERT INTO Personas (nombre, edad)
    VALUES (?, ?)
'''

# Utilizar 'with' para manejar la conexión y la ejecución de comandos SQL
with sqlite3.connect('app.db') as conexion:
    cursor = conexion.cursor()

    # Crear la tabla si no existe
    cursor.execute(crear_tabla)

    # Insertar datos en la tabla
    cursor.executemany(insert_query, datos_personas)

    # Guardar los cambios
    conexion.commit()
