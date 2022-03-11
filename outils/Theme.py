from abc import ABC, abstractmethod
from erreur import erreur

class Theme(ABC):
    def __init__(self, nom, nombreElementDemande):
        self.nom = nom
        self._motsReconnaisseur = []
        self._motsConnecteur = []

        self.nombreElementDemande = nombreElementDemande
        self._element = []

    def ajouterReconnaisseur(self, *args):
        """
            Entree: args (list[str])
            Sortie:
            Fonction: ajouter un/des mot(s) au mots reconnaisseur du theme
        """
        for mot in args:
            self._motsReconnaisseur.append(mot)

    def ajouterConnecteur(self, *args):
        """
            Entree: args (list[str])
            Sortie:
            Fonction: ajouter un/des mot(s) au mots connecteur du theme
        """
        for mot in args:
            self._motsConnecteur.append(mot)

    def getReconnaisseur(self):
        """
            Entree:
            Sortie: list
            Fonction: retourne les mots reconnaisseur du theme
        """
        return self._motsReconnaisseur

    def getConnecteur(self):
        """
            Entree:
            Sortie: list
            Fonction: retourne les mots connecteur du theme
        """
        return self._motsConnecteur

    def getElement(self):
        """
            Entree:
            Sortie: list
            Fonction: retourne les elements du theme
        """
        return self._element

    def resetElement(self):
        self._element = []

    def setElement(self, listeElement):
        """
            Entree:
            Sortie:
            Fonction:
        """
        if len(listeElement) == self.nombreElementDemande:
            self._element = listeElement
            return
        if len(listeElement) < self.nombreElementDemande:
            raise erreur.MissingElement(listeElement, self.nombreElementDemande)
        raise erreur.ToManyElement(listeElement, self.nombreElementDemande)

    @abstractmethod
    def action(self, *args, **kwars):
        """
            Entree:
            Sortie:
            Fonction: permet de definir les actions d'un theme
        """
        return

    def __str__(self):
        return f"le theme sur: {self.nom}"