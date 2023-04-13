# 1. Написати програму, яка буде робити запит на один із 5 сайтів і
# друкувати статус-код відповіді, назву сайту, а також довжину HTML-коду із відповіді.
# Вибір сайту для здійснення запиту має бути здійснений випадковим чином (random).
# Сайти:
# google.com,
# facebook.com,
# twitter.com,
# amazon.com,
# apple.com.

import json
import requests
import random

websites = [
    "https://google.com",
    "https://facebook.com",
    "https://twitter.com",
    "https://amazon.com",
    "https://apple.com"
]

website = random.choice(websites)
response = requests.get(website)
print("Website:", website)
print("Status code:", response.status_code)
print("Content length:", len(response.text))

#2. Використовуючи API для погоди https://open-meteo.com/en/docs, написати програму, яка буде приймати від користувача назву міста і
# виводити поточні показники погоди в консоль.
# Для визначення координат міста можна використати open-meteo.com

city = input("Enter city name: ")
def get_city_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&language=en&count=1&format=json"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        k = data.get('results')
        for i in k:
            lat = i.get('latitude')
            lon = i.get('longitude')
            return lat, lon

coordinates = list(get_city_coordinates(city))

def get_weather_data(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    response = requests.get(url)
    if response.ok:
        data2 = response.json()
        h = data2.get('hourly')
        return h




if coordinates:
    weather = get_weather_data(*coordinates)
    print(weather)
else:
    print("City not found.")
