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
            Sortie: str
            Fonction: permet d'envoyer et de traiter une requete envoyer a une api
        """
        return ""
    
    def setApiKey(self, apiKey: str):
        """
            Entree: apiKey (str)
            Sortie:
            Fonction: setter de l'attribut apiKey
        """
        self._API_KEY = apiKey
        
    def setUrl(self, url: str):
        """
            Entree: url (str)
            Sortie:
            Fonction: setter de l'attribut url
        """
        self.URL = url

    def getRequest(self, *agrs, **kwars):
        """
            Entree:
            Sortie:
            Fonction: envoie une requete get a une url et retourne la reponse
        """
        url = self.URL + self.parametre(*agrs, **kwars)
        return requests.get(url)
    
    def getRequestHeader(self,  *agrs, **kwars):
        """
            Entree:
            Sortie:
            Fonction: envoie une requeste get a une url et retourne la reponse
        """
        return requests.get(self.URL, headers=self.payload(*agrs, **kwars))
    
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
        
    def pasResultat(self, texte="Le theme n'a pas fonctionne"):
        """
            Entree: texte (str)
            Sortie: str
            Fonction: Retourne un texte predefini lorsque rien n'ai trouve par l'action du theme
        """
        return texte