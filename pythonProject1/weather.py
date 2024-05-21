import requests
from keys import *

api_address='https://api.openweathermap.org/data/2.5/weather?q=Indore&appid='+key2
json_data=requests.get(api_address).json()

def temp():
    temperature= round(json_data["main"]["temp"]-273,1)
    return temperature
def desc():
    description=json_data["weather"][0]["description"]
    return description
#print(temp())
#print(desc())

