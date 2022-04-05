from string import punctuation as ponctuation
from unidecode import unidecode

class RechercheTheme:
    def __init__(self, gestionTheme: object, texte: str):
        self.gestionTheme = gestionTheme

        self.texte = unidecode(texte)
        self.texte = self.texte.replace("'", " ")

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
            listeReconnaisseur = []
            compteurReconnaisseur,compteurConnecteur  = 0, 0
            index = 0
            indexMax = max(len(self.listeReconnaisseur), len(self.listeConnecteur))
            while index < indexMax:
                if index < len(self.listeReconnaisseur) and self.listeReconnaisseur[index] in theme.getReconnaisseur():
                    compteurReconnaisseur+=1
                    listeReconnaisseur.append(self.listeReconnaisseur[index])
                if index < len(self.listeConnecteur) and self.listeConnecteur[index] in theme.getConnecteur():
                    compteurConnecteur+=1
                index+=1
            if compteurReconnaisseur > 0 and compteurConnecteur > 0:
                self.listeThemePossible.append({'theme': theme, "reconnaiseur":listeReconnaisseur})

    def recupererElement(self):
        """
            Entree:
            Sortie:
            Fonction: ajouter dans une liste les mots suivant des connecteurs pour pouvoir trouver les elements utiles a l'execution de l'action du theme
        """
        self.dictElementThemePossible = []
        for theme in self.listeThemePossible:
            dictThemeActuel = {"texte": [], "connecteur": []}
            texteApresReconnaisseur = self.texte[self.texte.lower().index(theme["reconnaiseur"][0]):]
            #Determination des connecteurs du theme present dans le texte et ajout du mot suivant
            for connecteur in self.listeConnecteur:
                if connecteur in theme["theme"].getConnecteur() and connecteur in texteApresReconnaisseur.lower():
                    valeurDecalage = 1
                    #Si il y a plusieur fois le connecteur
                    if texteApresReconnaisseur.count(connecteur) > 1:
                        connecteur = " "+connecteur+" "
                        valeurDecalage = 0
                    texte = texteApresReconnaisseur[texteApresReconnaisseur.lower().index(connecteur)+len(connecteur)+valeurDecalage:]
                    if connecteur != ":":
                        for i in ponctuation:
                            if i == "." and i == "." and texte.count("@") == 0:
                                texte = texte.split(i)[0]
                            elif i not in ["'", "@", ".", "/", "*", "-", "+", "(", ")"] and i in texte:
                                    texte = texte.split(i)[0]
                    #Supprimer les espaces inutile
                    while len(texte)>0 and texte[-1] == " ":
                        texte = texte[:-1]
                    dictThemeActuel["texte"].append(texte)
                    dictThemeActuel["connecteur"].append(connecteur)
            self.dictElementThemePossible.append({"theme":theme["theme"],"reconnaiseur":theme["reconnaiseur"],"element":dictThemeActuel["texte"], "connecteur":dictThemeActuel["connecteur"]})

    def recupererReconnaisseur(self):
        """
            Entree:
            Sortie:
            Fonction: ajouter dans une liste les mots reconnaisseur qui sont present dans le texte (en un seul exemplaire)
        """
        self.listeReconnaisseur = []
        for Reconnaisseur in self.gestionTheme.getAllReconnaisseur():
            if Reconnaisseur.lower() in self.texte.lower().split(" "):
                if not ":" in self.texte.lower():
                    self.listeReconnaisseur.append(Reconnaisseur)
                elif self.texte.lower().index(Reconnaisseur) <= self.texte.index(":"):
                    self.listeReconnaisseur.append(Reconnaisseur)

    def recupererConnecteur(self):
        """
            Entree:
            Sortie:
            Fonction: ajouter dans une liste les mots connecteur qui sont present dans le texte (en un seul exemplaire)
        """
        self.listeConnecteur = []
        for connecteur in self.gestionTheme.getAllConnecteur():
            if (connecteur.lower() in self.texte.lower().split(" ")):
                if not ":" in self.texte.lower():
                    self.listeConnecteur.append(connecteur)
                elif self.texte.lower().index(connecteur) <= self.texte.index(":"):
                    self.listeConnecteur.append(connecteur)
