import requests
import json

#Teil a)

class StadtWetter:
    def __init__(self):
        self.stadtname = input("Stadtname? ")
        self.wetter = requests.get(f'https://wttr.in/{self.stadtname}?format=j1')
        print(self.wetter.json())

#Teil b)

#Lösung:
# Aufgabe 2
# a
class StadtWetter:
    def __init__(self, stadt):
        self.stadt = stadt
        self.weather_data = self.get_weather()

    def get_weather(self):
        url = 'https://wttr.in/' + self.stadt + '?format=j1'
        return requests.get(url).json()

    # b
    def current_weather(self):
        print(self.weather_data['current_condition'][0]['weatherDesc'][0]['value'])

    # c
    def day_max(self):
        print(self.weather_data['weather'][1]['maxtempC'])


wetter = StadtWetter('Bonn')
wetter.current_weather()
wetter.day_max()