import sqlite3

# Comando SQL para seleccionar todos los registros en la tabla
select_query = '''
    SELECT * FROM Personas
'''

# Utilizar 'with' para manejar la conexión y la ejecución de comandos SQL
with sqlite3.connect('app.db') as conexion:
    cursor = conexion.cursor()

    # Ejecutar la consulta y obtener todos los resultados
    cursor.execute(select_query)
    resultados = cursor.fetchall()

    # Mostrar los datos de todas las personas encontradas
    if resultados:
        print("Datos de todas las personas:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No se encontraron personas en la tabla.")
