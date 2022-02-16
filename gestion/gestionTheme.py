from theme import Meteo
from gestion import rechercheTheme

class GestionTheme:
    def __init__(self):

        self.meteo = Meteo.Meteo()

        self.theme = {"meteo": self.meteo,
                      "meteo2": Meteo.Meteo()}

        #------------------temp----------------------------
        self.meteo.ajouterReconnaisseur("temperature")
        self.meteo.ajouterConnecteur("de")
        self.meteo.nom="La vraie meteo"

        self.theme["meteo2"].ajouterConnecteur(":")
        #--------------------------------------------------

    def verifierTheme(self, texte: str):
        """
            Entree: texte (str)
            Sortie: list
            Fonction: retourne la liste des themes possible present dans un texte
        """
        themesTrouves = rechercheTheme.RechercheTheme(self,texte).get()
        return themesTrouves

    def getAllReconnaisseur(self):
        """
            Entree:
            Sortie: list
            Fonction: retourne la liste de tous les mot reconnaisseur des theme de facon unique
        """
        listeReconnaisseur = []
        for theme in self.theme.values():
            for mot in theme.getReconnaisseur():
                if mot not in listeReconnaisseur:
                    listeReconnaisseur.append(mot)
        return listeReconnaisseur

    def getAllConnecteur(self):
        """
            Entree:
            Sortie: list
            Fonction: retourne la liste de tous les mot connecteur des theme de facon unique
        """
        listeConnecteur = []
        for theme in self.theme.values():
            for mot in theme.getConnecteur():
                if mot not in listeConnecteur:
                    listeConnecteur.append(mot)
        return listeConnecteur

    def getAllUrl(self):
        """
            Entree:
            Sortie: list
            Fonction: retourne la liste de tous les url des theme de facon unique
        """
        listeUrl = []
        for theme in self.theme.values():
            listeUrl.append(theme.api.URL)
        return listeUrl
