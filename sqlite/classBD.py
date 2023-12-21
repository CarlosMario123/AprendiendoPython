import sqlite3

class BaseDeDatos:
    def __init__(self, nombre_base_de_datos):
        self.nombre_base_de_datos = nombre_base_de_datos
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = sqlite3.connect(self.nombre_base_de_datos)
            print("Conexión establecida a la base de datos:", self.nombre_base_de_datos)
        except sqlite3.Error as e:
            print("Error al conectar a la base de datos:", e)

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada a la base de datos:", self.nombre_base_de_datos)

    def ejecutar_consulta(self, consulta, parametros=()):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta, parametros)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("Error al ejecutar la consulta:", e)
            return None

    def ejecutar_actualizacion(self, consulta, parametros=()):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta, parametros)
            self.conexion.commit()
            print("Operación de actualización ejecutada correctamente.")
        except sqlite3.Error as e:
            print("Error al ejecutar la actualización:", e)

# Ejemplo de uso
bd = BaseDeDatos('app.db')
bd.conectar()

# Ejemplo de consulta SELECT
resultados = bd.ejecutar_consulta('SELECT * FROM Personas')
if resultados:
    for resultado in resultados:
        print(resultado)

# Ejemplo de actualización INSERT
nueva_persona = ("josefa", 35)
bd.ejecutar_actualizacion('INSERT INTO Personas (nombre, edad) VALUES (?, ?)', nueva_persona)

bd.desconectar()
