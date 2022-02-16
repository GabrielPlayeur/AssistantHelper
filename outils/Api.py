import requests
from abc import ABC, abstractmethod

class Api(ABC):
    def __init__(self):
        self._API_KEY = "votre_cle_api"
        self.URL = "votre_url_api"

    @abstractmethod
    def envoyerRequest(self, *agrs, **kwars):
        """
            Entree:
            Sortie:
            Fonction: permet d'envoyer et de traiter une requete envoyer a une url
        """
        return

    def getRequest(self, *agrs, **kwars):
        """
            Entree:
            Sortie:
            Fonction: envoie une requete get a une url et retourne la reponse
        """
        url = self.URL + self.parametre(*agrs, **kwars)
        return requests.get(url)
    
    def postRequest(self, *agrs, **kwars):
        """
            Entree:
            Sortie:
            Fonction: envoie une requeste post a une url et retourne la reponse
        """
        return requests.post(self.URL, data=self.payload(*agrs, **kwars))

    def parametre(self, *agrs, **kwars):
        """
            Entree:
            Sortie: str
            Fonction: permet de definir les parametres de l'url a envoyer avec la requete get
        """
        return ""
    
    def payload(self, *args, **kwars):
        """
            Entree:
            Sortie: str
            Fonction: permet de definir les data de la requete post
        """
        return ""

    def checkRequestStatus(self, reponse):
        """
            Entree: reponse 
            Sortie: bool
            Fonction: permet de retourner True si la requete a bien ete traite sinon False
        """
        if reponse.status_code == 200:
            return True
        else:
            return False  