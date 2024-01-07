'''
This mini project uses two free API's to get the weather in give city
'''

import requests
import json
from math import ceil

def get_geocoordinates(city):
    url = f'https://geocode.maps.co/search?q={city}&api_key=65992da09ff3f807664153cbt634e5c'
    response = requests.get(url)
    json_data = response.json()
    # fetch_data = json.dumps(json_data, indent=4) For easier reading of the json response print this variable
    lat = json_data[0]["lat"]
    lon = json_data[0]["lon"]
    return lat, lon


def get_current_weather(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=a97ebf83c04d19f47b073f2c082eb9a2'
    response =requests.get(url)
    json_data = response.json()
    # fetch_data = json.dumps(json_data, indent=4)
    current_temp = json_data["main"]["temp"]
    feels_like = json_data["main"]["feels_like"]
    min_temp = json_data["main"]["temp_min"]
    max_temp = json_data["main"]["temp_max"]
    return current_temp, feels_like, min_temp, max_temp


def kelvin_to_celsius(temp):
    temp = int(temp)
    celsius_temp = temp - 273.15
    return celsius_temp


input_city = input('What is the temperature in: ')
city = input_city.capitalize()

coordinates = get_geocoordinates(city)
coord_dict = {'lat': coordinates[0], 'lon': coordinates[1]}

temperature = get_current_weather(coord_dict['lat'],coord_dict['lon'])
keys = ['current_temp', 'feels_like', 'min_temp', 'max_temp']
temperature_dict = {key: value for key, value in zip(keys, temperature)}

current_temp = ceil(kelvin_to_celsius(temperature_dict["current_temp"]))
feels_like = ceil(kelvin_to_celsius(temperature_dict["feels_like"]))
min_temp = ceil(kelvin_to_celsius(temperature_dict["min_temp"]))
max_temp = ceil(kelvin_to_celsius(temperature_dict["max_temp"]))


print(f'The temperature in {city} currently is {current_temp} Celsius')
print(f'Feels like {feels_like} Celsius')

if min_temp == max_temp:
    print(f'The minimum and maximum temperature today will be {min_temp}')

else:
    print(f'The minimum temperature today will be {min_temp} Celsius '
      f'and the maximum - {max_temp} Celsius')