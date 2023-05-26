#todo lo que tiene que ver con flask

from flask import Flask, request
#importar cors e instalar con pip...cors. porque es el dedicado hablar con el front
from flask_cors import CORS
# . para indicar ruta  y * para importar todo
from .weather import *

app = Flask(__name__)
#aqui cors porque es el dedicado hablar con el front
#se debe colocar
cors=CORS(app)

#@app.route("/cities/<id>") equivalentes como al de abajo
@app.route("/cities/<id>", methods=["GET"])
def cities(id):
    return get_weather_by(id)

# 1 obtenemos todos los datos, con get  endpoint
@app.route("/cities/", methods=["GET"])
def all_cities():
    return list_weather_all()

# 2 guardar o añadir una ciudad
@app.route("/cities", methods=["POST"])
def new_city():
    #llamamos con un valor.  add_city(informacion del formulario)
    #return add_city()
    #recuperar toda la informacion que llega del body en postman
    data = request.get_json()
    print("***********new_city", data)
    
    #llamamos la funcion y le pasamos el parametro de lo obtenido
    add_city(data)
    return ""

@app.route("/cities/<city_id>", methods=["PUT"])
def update_city(city_id):
    #llamamos con un valor.  add_city(informacion del formulario)
    #return add_city()
    #recuperar toda la informacion que llega del body en postman
    data = request.get_json()
    print("***********new_city", data)
    
    #llamamos la funcion y le pasamos el parametro de lo obtenido
    put_city(data)
    return ""

@app.route("/")
def hello_world():
    return "Hola"


# 3 borrar ciudad test
@app.route("/cities/<id>", methods=["DELETE"])
def delete_city(id):
    remove_city(id)
    return list_weather_all()
