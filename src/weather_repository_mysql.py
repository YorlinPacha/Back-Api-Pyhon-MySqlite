
# 1 libreria para mysql   mysql-connector-python   en pip install y luego importamos
import mysql.connector


# cambiar el tipo de conexion de sqlite a mysql
def create(weather):
    print("****************")
    print("*******", weather)
    conexion = sqlite3.connect("weather.db")
    try:
        cursor = conexion.cursor()
        # estos valores los mando desde postman y se agregan - ? variables y se agregan con []
        cursor.execute("INSERT INTO 'main'.'cities' ('id', 'name', 'temperature', 'rain_probability') VALUES (?, ?, ?, ?);", 
                       [weather['id'], 
                       weather['name'], 
                       weather['temperature'], 
                       weather['rain_probability']
                       ] 
                    )
        #devuelve informacion
        conexion.commit()
    
    finally:
        conexion.close    

###############################################################

     
def read(id):    #dame uno 
    conexion = sqlite3.connect("weather.db")
    try:
        cursor = conexion.cursor()
        # no se puede ingrear codigo sql a python, hay que hacer algo. ? =VARIABLES
        res = cursor.execute("SELECT id,name,temperature,rain_probability FROM cities WHERE id=?", [id])
        #devuelve informacion
        row = res.fetchone()
        
        
        # {"id": "BIO","name": "Bilbao","temperature": 11,"rain_probability": 0.9}
        # row {BIO, Bilbao, 15 ,1} , no devuelve diccionario, es tupla
        # aqui lo convierto en diccionario asignando valores
        
        city = {"id": row[0],
                "name": row[1],
                "temperature": row[2],
                "rain_probability": row[3]}
        
        return city
    except:
        None
    finally:
        conexion.close    
    
def read_all():      #dame todos
    conexion = mysql.connector.connect(
    #servidor donde esta, IP etc...
    host="localhost",
    user="root",
    password="123456",
    database="weather"
    )
    cursor = conexion.cursor()
    res = cursor.execute("SELECT * FROM cities")
    resultado = res.fetchall()
    print(resultado)
    conexion.close
    return resultado


def update(update_city):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    values = (update_city['id'], update_city['name'], update_city['temperature'], update_city['rain_probability'])
    cur.execute("UPDATE cities SET id = ?, name = ?, temperature = ?, rain_probability = ? WHERE id = ?", values + (update_city['id'],))
    con.commit()
    con.close()
    return "Se ha actualizado una ciudad"

       

def delete(city_id):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    cur.execute("DELETE FROM cities WHERE id=?", (city_id,))
    con.commit()
    con.close()
    return 