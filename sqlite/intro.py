#para trabajar con sqlite3 utilizamos el modulo sqlit3
import sqlite3

#realizamos la conexion
con = sqlite3.connect("app.db")
#siempre que abrimos una base de datos hay que cerrarlo
con.close()