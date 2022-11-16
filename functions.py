import requests, json
from bs4 import BeautifulSoup
import re
from urllib2 import urlopen
from geopy.geocoders import Nominatim

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def getlocation():

    
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    return data['city']

def getweather(city):

    city = city.replace(" ", "+")
 
    try:
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
 
        thingy = BeautifulSoup(res.text, 'html.parser')

        location = thingy.select('#wob_loc')[0].getText().strip()

        time = thingy.select('#wob_dts')[0].getText().strip()

        info = thingy.select('#wob_dc')[0].getText().strip()

        temperature = thingy.select('#wob_tm')[0].getText().strip()

        weather = {}
        weather[time] = time
        weather[temperature] = temperature
        weather[info] = info

        return weather

    except:
        return "can't find your location"
