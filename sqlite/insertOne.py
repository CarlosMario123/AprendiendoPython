import sqlite3

# Datos de ejemplo para insertar en la tabla
nueva_persona = ("Laura", 35)

# Comando SQL para insertar un solo registro en la tabla
insert_query = '''
    INSERT INTO Personas (nombre, edad)
    VALUES (?, ?)
'''

# Utilizar 'with' para manejar la conexión y la ejecución de comandos SQL
with sqlite3.connect('app.db') as conexion:
    cursor = conexion.cursor()

    # Insertar un solo registro en la tabla
    cursor.execute(insert_query, nueva_persona)

    # Guardar los cambios
    conexion.commit()
