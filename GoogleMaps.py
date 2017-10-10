#cle AIzaSyDsTWEt2e8ppNYDwYVvJ5c9x-OdHFKvaM4
import requests
from pprint import pprint
import json

class GMapsDriving :

    def Get_Voiture(self):
        self.url = 'https://maps.googleapis.com/maps/api/directions/json?origin=2+Rue+Joliot+Curie,+91190+Gif-sur-Yvette&destination=Antony&mode=driving&key=AIzaSyDsTWEt2e8ppNYDwYVvJ5c9x-OdHFKvaM4'

        self.response = requests.get(self.url)
        if self.response.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(self.response.status_code))
        self.distance = self.response.json()['routes'][0]['legs'][0]['distance']['text']
        self.temps = self.response.json()['routes'][0]['legs'][0]['duration']['text']
        return self.distance, self.temps

voiture = GMapsDriving()
print(voiture.Get_Voiture())


#Il reste à rendre l'url dynamique en prenant en compte des longitudes et latitudes pour etre coherent