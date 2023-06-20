# 1 libreria para mysql   mysql-connector-python   en pip install y luego importamos
import mysql.connector


#aqui creamos solo la base de datos

#2 conexion con mysql
conexion = mysql.connector.connect(
    #servidor donde esta, IP etc...
  host="localhost",
  user="root",
  password="123456"
)

cursor = conexion.cursor()
cursor.execute("CREATE DATABASE weather")
