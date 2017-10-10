import requests


url="https://opendata.paris.fr/explore/dataset/stations-velib-disponibilites-en-temps-reel/api/?lang=FR&rows=8&exclude.status=CLOSED&geofilter.distance="


#dynamic_url return a dynamic url that directs straight to the appropriate API
def dynamic_url(lat,long,distance):
    return url+lat+","+long+","+distance

class Velib():
    def __init__(self,lat,long,distance):
        self.lat=lat
        self.long=long
        self.distance=distance
    def Get_Velib_Itinerary(self):
        self.url = dynamic_url(self.lat,self.long,self.distance)

        self.response = requests.get(self.url)
        if self.response.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(self.response.status_code))
        print(self.response.json())

        #for item in self.response.json()['weather']:
           # self.meteo = item.pop('main')
        #return self.meteo

#temps = Weather()
#print(temps.GetMeteo())