from string import punctuation as ponctuation
from unidecode import unidecode

class RechercheTheme:
    def __init__(self, gestionTheme: object, texte: str):
        self.gestionTheme = gestionTheme

        self.texte = unidecode(texte)

        self.recupererReconnaisseur()
        self.recupererConnecteur()

        self.comparaisonTheme()
        self.recupererElement()

    def get(self):
        """
            Entree:
            Sortie: list
            Fonction: retourne la liste des themes possible
        """
        return self.dictElementThemePossible

    def comparaisonTheme(self):
        """
            Entree:
            Sortie:
            Fonction: ajouter dans une liste les themes dont au moin 1 mot reconnaisseur et connecteur est present dans le texte
        """
        self.listeThemePossible = []
        for theme in self.gestionTheme.theme.values():
            compteurReconnaisseur,compteurConnecteur  = 0, 0
            index = 0
            indexMax = max(len(self.listeReconnaisseur), len(self.listeConnecteur))
            while index < indexMax:
                if index < len(self.listeReconnaisseur) and self.listeReconnaisseur[index] in theme.getReconnaisseur():
                    compteurReconnaisseur+=1
                if index < len(self.listeConnecteur) and self.listeConnecteur[index] in theme.getConnecteur():
                    compteurConnecteur+=1
                index+=1
            if compteurReconnaisseur > 0 and compteurConnecteur > 0:
                self.listeThemePossible.append(theme)

    def recupererElement(self):
        """
            Entree:
            Sortie:
            Fonction: ajouter dans une liste les mots suivant des connecteurs pour pouvoir trouver les elements utiles a l'execution de l'action du theme
        """
        self.dictElementThemePossible = []
        for theme in self.listeThemePossible:
            texteTheme = []
            #Determination des connecteurs du theme present dans le texte et ajout du mot suivant
            for connecteur in self.listeConnecteur:
                if connecteur in theme.getConnecteur():
                    valeurDecalage = 1
                    #Si il y a plusieur fois le connecteur
                    if self.texte.count(connecteur) > 1:
                        connecteur = " "+connecteur
                    texte = self.texte[self.texte.lower().index(connecteur)+len(connecteur)+valeurDecalage:]
                    if connecteur != ":":
                        for i in ponctuation:
                            if i != "'" and i in texte:
                                texte = texte.split(i)[0]
                    #Supprimer les espaces inutile
                    while len(texte)>0 and texte[-1] == " ":
                        texte = texte[:-1]
                    texteTheme.append(texte)
            self.dictElementThemePossible.append({"theme":theme,"element":texteTheme})

    def recupererReconnaisseur(self): 
        """
            Entree:
            Sortie:
            Fonction: ajouter dans une liste les mots reconnaisseur qui sont present dans le texte (en un seul exemplaire)
        """
        self.listeReconnaisseur = []
        for Reconnaisseur in self.gestionTheme.getAllReconnaisseur():
            if Reconnaisseur.lower() in self.texte.lower().split(" "):
                self.listeReconnaisseur.append(Reconnaisseur)

    def recupererConnecteur(self):
        """
            Entree:
            Sortie:
            Fonction: ajouter dans une liste les mots connecteur qui sont present dans le texte (en un seul exemplaire)
        """
        self.listeConnecteur = []
        for connecteur in self.gestionTheme.getAllConnecteur():
            if connecteur.lower() in self.texte.lower().split(" "):
                self.listeConnecteur.append(connecteur)
