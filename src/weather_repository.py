# function getWeather(){
#     return{
#     "id": "BIO",
#     "name": "Bilbao",
#     "temperature": 11,
#     "rain_probability": 0.9
# }
# }


# ahora en python , se hace asi una funcion
#Definir un mapa o un objeto, diccionario)
WEATHER_DB = {
    "BIO":{
        "id": "BIO",
        "name": "Bilbao",
        "temperature": 11,
        "rain_probability": 0.9
    },
    "RMA":{
        "id": "RMA",
        "name": "Roma",
        "temperature": 22,
        "rain_probability": 0.2
    }
}

def create(weather):
    #weather = {"id": "MAD","name": "Madrid", ...
    #id=weather["id"]  => lo que llegue, cojo el id MAD
    #WEATHER_DB[id]=weather => el resto lo agrego como valor
    
    #WEATHER_DB[weather["id"]]=weather
     WEATHER_DB[weather["id"]]=weather
     
def read(id):    #dane uno 
    return WEATHER_DB.get(id)  

def read_all():      #dane todos
    return WEATHER_DB

def delete(id):   
    del WEATHER_DB[id]

#NOTA
# weather. En otras palabras, se espera que weather sea un diccionario que contenga ciertas claves (en este caso "id", "name", etc.) y sus respectivos valores.
# La línea de código principal WEATHER_DB[weather["id"]] = weather asigna el argumento weather al diccionario global WEATHER_DB con una clave que es el valor de la clave "id" en el diccionario weather. Esto significa que cada ciudad en el diccionario global WEATHER_DB se identifica por su "id" y tiene asociada toda la información del diccionario weather.
# En la línea de código WEATHER_DB[weather["id"]] = weather, la clave sería el valor de la clave "id" en el diccionario weather. Por lo tanto, la clave sería una cadena de texto que representa el ID de la ciudad, como "MAD" para Madrid.
# El valor sería el diccionario completo weather, que contiene la información meteorológica de la ciudad, incluyendo su nombre, coordenadas geográficas, temperatura, humedad, etc.
# En resumen, la clave identifica una ciudad específica en la base de datos global WEATHER_DB, mientras que el valor contiene toda la información meteorológica de esa ciudad.

    