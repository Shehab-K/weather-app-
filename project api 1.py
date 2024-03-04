import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "8c5ba9b2bec470a01a2a5563e29cf2d0"
CITY = "cairo"

Url = f"{BASE_URL}appid={API_KEY}&q={CITY}"


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = kelvin * (9 / 5) + 32
    return fahrenheit, celsius


response = requests.get(Url).json()
print(response)


temp_kelvin = response["main"]["temp"]
temp_celsius = kelvin_to_celsius_fahrenheit(temp_kelvin)
temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

feel_like_kelvin = response["main"]["feels_like"]
feel_like_celsius = kelvin_to_celsius_fahrenheit(feel_like_kelvin)
feel_like_fahrenheit = kelvin_to_celsius_fahrenheit(feel_like_kelvin)

humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
wind_speed = response["wind"]["speed"]
sunrise_time = dt.datetime.utcfromtimestamp(
    response["sys"]["sunrise"] + response["timezone"]
)
sunset_time = dt.datetime.utcfromtimestamp(
    response["sys"]["sunset"] + response["timezone"]
)

print(f"temperature in {CITY}: {temp_celsius:}*C or {temp_fahrenheit}*f")
print(
    f"temperature in {CITY} feels like: {feel_like_celsius:}*C or {feel_like_fahrenheit}*f"
)
print(f"the humidity in {CITY}: {humidity}%")
print(f"the wind speed in {CITY}: {wind_speed}km/h")
print(f"General Weather in {CITY}:{description}")
print(f"the sunrise in {CITY}: {sunrise_time} local time")
print(f"the sunset in {CITY}: {sunset_time} local time")
