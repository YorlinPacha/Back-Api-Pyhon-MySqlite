
#pequeño archivo para crear la conexion 

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)

print(mydb)

# en terminal para probar =>  python3 test/demo_mysql_connection.py 