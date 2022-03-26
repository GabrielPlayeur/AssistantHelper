from outils import Theme, Api
from bs4 import BeautifulSoup
from re import sub
from unicodedata import normalize

class Larousse(Theme.Theme):
    def __init__(self):
        super().__init__("larousse", 1)

        super().ajouterReconnaisseur("cherche","definit","definition","définition")
        super().ajouterConnecteur(":","de")

        self.api = LarousseApi()

    def action(self):
        resultat = self.api.envoyerRequest(self.getElement()[0])
        self.resetElement()
        return resultat

class LarousseApi(Api.Api):
    def __init__(self):
        super().__init__()

        self.setUrl("https://www.larousse.fr/dictionnaires/francais/")

    def parametre(self, mot):
        return mot.lower()

    def envoyerRequest(self, mot):
        reponse = super().getRequest(mot)
        resultat = ""
        definition = []
        
        if super().checkRequestStatus(reponse):
            #Recuperation de la page en format HTML
            soup = BeautifulSoup(reponse.text, 'html.parser')
            for ul in soup.find_all('ul'):
                if ul.get('class') is not None and 'Definitions' in ul.get('class'):
                    #Recherche de la definition sur la page
                    definition.append([normalize("NFKD", sub("<.*?>", "", str(li))) for li in ul.find_all('li')])
                    for d in definition[0]:
                        resultat += str(d).replace("\t","")+"\n"
        if resultat == "":
            resultat = "Le mot n'a pas été trouvé !"
                
        return resultat