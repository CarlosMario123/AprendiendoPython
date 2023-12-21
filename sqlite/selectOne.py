import sqlite3

# id de la persona a buscar
Idbuscar = 3

# Comando SQL para buscar una persona por correo
select_query = '''
    SELECT * FROM Personas
    WHERE id = ?
'''

# Utilizar 'with' para manejar la conexión y la ejecución de comandos SQL
with sqlite3.connect('app.db') as conexion:
    cursor = conexion.cursor()

    # Ejecutar la consulta y obtener el resultado
    cursor.execute(select_query, (Idbuscar,))
    resultado = cursor.fetchone()

    if resultado:
        print("Datos de la persona encontrada:", resultado)
    else:
        print("La persona con id '{}' no fue encontrada.".format(Idbuscar))
