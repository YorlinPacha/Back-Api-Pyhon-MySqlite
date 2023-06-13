
#TERCERA Y ULTIMA ETAPA

# sqlite no guarda dats en un diccionario
# se define como interfaz ( solo se define los nombres de los metodos)

# 1 paso crear base de datos (https://docs.python.org/3/library/sqlite3.html)
import sqlite3
conexion = sqlite3.connect("weather.db")
cursor = conexion.cursor()
#creando como un excel
cursor.execute("CREATE TABLE IF NOT EXISTS cities(id, name, temperature, rain_probability)")


#post
# def create(new_city):
#     con = sqlite3.connect("weather.db")
#     cur = con.cursor()
#     values = (new_city['id'], new_city['name'], new_city['temperature'], new_city['rain_probability'])
#     cur.execute("INSERT INTO cities (id, name, temperature, rain_probability) VALUES (?, ?, ?, ?)", values)
#     con.commit()
#     con.close()
#     print("********he recibido una ciudad")
#     return 

#create con joseba
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
    conexion = sqlite3.connect("weather.db")
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

##update joseba
# def update(weather):
#     print("****************")
#     print("*******", weather)
#     conexion = sqlite3.connect("weather.db")
#     try:
#         cursor = conexion.cursor()
#         # estos valores se prueban cundo las otras partes esten listas
#         cursor.execute("UPDATE cities SET 'name'=?, 'temperature'=?, 'rain_probability'=? WHERE 'id'=?", 
#                        [
#                        weather['name'], 
#                        weather['temperature'], 
#                        weather['rain_probability'],
#                        weather['id']
#                        ] 
#                     )
#         #devuelve informacion
#         conexion.commit()
    
#     finally:
#         conexion.close   

##################################################################

def delete(city_id):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    cur.execute("DELETE FROM cities WHERE id=?", (city_id,))
    con.commit()
    con.close()
    return 