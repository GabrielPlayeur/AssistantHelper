from numpy import dtype
from outils import Theme
from pytz import timezone
from tzwhere import tzwhere
from datetime import datetime
from geopy.geocoders import Nominatim

class Heure(Theme.Theme):
    def __init__(self):
        super().__init__("heure",1)

        super().ajouterReconnaisseur("heure","fuseau","horaire")
        super().ajouterConnecteur("a","en","de")

        self.geolocator = Nominatim(user_agent="geoapiExercises")

    def action(self):
        lad = self.getElement()[0] #Recuperation de l'endroit demande
        location = self.geolocator.geocode(lad)
        timezoneStr = tzwhere.tzwhere().tzNameAt(location.latitude, location.longitude) #recuperation de la position de la ville

        if timezoneStr is None:
            resultat = "Impossible de déterminer la localisation de la ville donnée"
        else:
            timezonePy = timezone(timezoneStr) #recuperation de la timezone de la ville
            dt = datetime.utcnow() #Recuperation de notre heure
            res = dt + timezonePy.utcoffset(dt) #ajout du decalage
            res2 = res.strftime("%H:%M") #formatage de l'heure
            resultat =  f"Il est {res2} à/en {timezoneStr}"        
        self.resetElement()
        return resultat
