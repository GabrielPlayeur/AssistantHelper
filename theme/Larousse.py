from outils import Theme, Api
from erreur import erreur
from bs4 import BeautifulSoup
import re
import unicodedata

class Larousse(Theme.Theme):
    def __init__(self):
        super().__init__("larousse", 1)

        super().ajouterReconnaisseur("cherche","definit","definiton")
        super().ajouterConnecteur(":","de")

        self.api = LarousseApi()

    def action(self):
        self.api.envoyerRequest(self.getElement()[0])
        self.resetElement()

class LarousseApi(Api.Api):
    def __init__(self):
        super().__init__()
        
        self.setUrl("https://www.larousse.fr/dictionnaires/francais/")
        
    def parametre(self, mot):
        return mot.lower()

    def envoyerRequest(self, nomCrypto):
        reponse = super().getRequest(nomCrypto)
        
        if super().checkRequestStatus(reponse):
            soup = BeautifulSoup(reponse.text, 'html.parser')
            for ul in soup.find_all('ul'):
                if ul.get('class') is not None and 'Definitions' in ul.get('class'):
                    print([unicodedata.normalize("NFKD", re.sub("<.*?>", "", str(li))) for li in ul.find_all('li')])
             
        