# 1 libreria para mysql   mysql-connector-python   en pip install y luego importamos
import mysql.connector

#aqui creamos solo la tabla

#2 conexion con mysql
conexion = mysql.connector.connect(
    #servidor donde esta, IP etc...
  host="localhost",
  user="root",
  password="123456",
  database="weather"
)


cursor = conexion.cursor()
#creando como un excel Y OBLIGATORIO AGREGAR TIPO DE DATO
cursor.execute("CREATE TABLE IF NOT EXISTS cities(id VARCHAR(3) PRIMARY KEY, name VARCHAR(20), temperature INT, rain_probability FLOAT)")