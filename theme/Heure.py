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
        lad = self.getElement()[0]        
        location = self.geolocator.geocode(lad)
        timezoneStr = tzwhere.tzwhere().tzNameAt(location.latitude, location.longitude)

        if timezoneStr is None:
            resultat = "Ne peut pas déterminer la localisation de votre ville donnée"
        else:
            timezonePy = timezone(timezoneStr)
            dt = datetime.utcnow()
            res = dt + timezonePy.utcoffset(dt)
            res2 = res.strftime("%H:%M")
            resultat =  f"Il est {res2} à/en {timezoneStr}"
        
        self.resetElement()
        return resultat
