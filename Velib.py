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

#new
import requests

exemple_coordonnees=(48.8619,2.347)

def station_depart(depart_velib):
    hits=0
    i=1
    while hits < 3:
        rayon=50*i
        depart="%2C".join([str(depart_velib[0]),str(depart_velib[1]),str(rayon)])

        url="https://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel"
        param="&q=status%3D%3D%22open%22+AND+available_bikes%3E0&geofilter.distance="+depart
        #selection des stations ouvertes, avec des velos dispos, et a une distance d du point de depart

        r = requests.get(url,param)
        results = r.json()

        hits=results['nhits']
        i+=1

    station1=results['records'][0]['fields']['address']
    velo1 = results['records'][0]['fields']['available_bikes']
    distance1=results['records'][0]['fields']['dist']
    #station la plus proche

    station2=results['records'][1]['fields']['address']
    velo2 = results['records'][1]['fields']['available_bikes']
    distance2=results['records'][1]['fields']['dist']
    #deuxieme station la plus proche

    station3=results['records'][2]['fields']['address']
    velo3 = results['records'][2]['fields']['available_bikes']
    distance3=results['records'][2]['fields']['dist']
    #troisieme station la plus proche

    return "La station de Velib la plus proche de vous est la station {}, à {} mètres.\nIl y a {} vélos disponibles.\n\n La deuxième station de Velib la plus proche est la station {}, à {} mètres.\nIl y a {} vélos disponibles.\n\nLa troisième station de Velib la plus proche est la station {}, à {} mètres.\nIl y a {} vélos disponibles.".format(station1,distance1,velo1,station2,distance2,velo2,station3,distance3,velo3)


print(station_depart(exemple_coordonnees))
