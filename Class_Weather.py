#201999caea9038bf5f77ce8a08f8d1af APIID
import requests
from pprint import pprint
import json

class Weather_API():

    def GetMeteo(self):
        self.url = 'https://api.openweathermap.org/data/2.5/weather?q=Paris&APPID=201999caea9038bf5f77ce8a08f8d1af'

        self.response = requests.get(self.url)
        if self.response.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(self.response.status_code))
        self.response.json()

        for item in self.response.json()['weather']:
            self.meteo = item.pop('main')
        return self.meteo

temps = Weather()
print(temps.GetMeteo())
