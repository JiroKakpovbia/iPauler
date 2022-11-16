
from bs4 import BeautifulSoup
import requests, json


def getweather(city):

    city = city.replace(" ", "+")

    api_key = "d3f942c21618e3c4c65190a565eba1b4"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)

    thing = response.json()
 
    if thing["cod"] != "404":
    

        main = thing["main"]
    

        temperature = main["temp"]
    

        pressure = main["pressure"]

        humidity = main["humidity"]

        weath = thing["weather"]

        description = weath[0]["description"]
    
        result = [temperature, pressure, humidity, description]

        return result
    
    else:
        return 0




