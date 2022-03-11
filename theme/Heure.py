from outils import Theme, Api
from erreur import erreur
import pytz
from tzwhere import tzwhere
from datetime import datetime
from geopy.geocoders import Nominatim

class Heure(Theme.Theme):
    def __init__(self):
        super().__init__("heure",1)

        super().ajouterReconnaisseur("heure")
        super().ajouterConnecteur("à","en","de")

        self.geolocator = Nominatim(user_agent="geoapiExercises")

    def action(self):
        lad = self.getElement()[0]

        location = self.geolocator.geocode(lad)

        tz = tzwhere.tzwhere()

        timezone_str = tz.tzNameAt(location.latitude, location.longitude)

        if timezone_str is None:
            print("ne peut pas déterminer la localisation de votre ville donnée")
        else:
            # Display the current time in that time zone
            timezone = pytz.timezone(timezone_str)
            dt = datetime.utcnow()
            res = dt + timezone.utcoffset(dt)
            res2 = res.strftime("%H:%M")
            print("Il est",res2,"à/en",timezone_str)
