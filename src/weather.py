

from .weather_repository_sqlite import *


def add_city(weather):
    #weather = {"id": "MAD","name": "Madrid", ...
    #calcular probabilidad de lluvia (rain_probability = 0.7) ya que no llega desde el post
    # 1 obtener temperatura previa
    # ciudad_previa = read(weather["id"])
    # tmp_previa = ciudad_previa["temperature"]
    # # 2 calcular la diferencia de la antigua con la nueva
    # diff_tempertura = weather["temperature"] - tmp_previa
    # if diff_tempertura < 0:
    #     rain_probability = 0.7
    # else:
        #rain_probability = 0.2     
    rain_probability = 0.7
    weather["rain_probability"] = rain_probability
    create(weather)
    

def get_weather_by(id):
    return read(id)

def list_weather_all():
    return read_all()

def remove_city(id):
    delete(id)
    
    
def put_city(weather):
    update(weather)




