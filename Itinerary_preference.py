class Itinerary:
    def __init__(self, departure, arrival, departure_time):
        self.departure= departure
        self.arrival = arrival
        self.departure_time = departure_time

class Itinerary_preference(Itinerary):

    preference=input("Pour le chemin le plus court, tapez 1. Pour le chemin le plus rapide, tapez 2. Pour marcher le moins possible, tapez 3.")
    accessibility=input("Pour un chemin accessible, tapez 1 sinon tapez 0.")
    def __init__(self,departure, arrival, departure_time):
        Itinerary.__init__(self,departure, arrival, departure_time)
        self.preference=Itinerary_preference.preference
        self.accesibility=Itinerary_preference.accessibility

