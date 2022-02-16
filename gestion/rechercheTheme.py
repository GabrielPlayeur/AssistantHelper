
class RechercheTheme:
    def __init__(self, gestionTheme: object, texte: str):
        self.gestionTheme = gestionTheme

        self.texte = texte

        self.recupererReconnaisseur()
        self.recupererConnecteur()

        self.comparaisonTheme()

    def get(self):
        """
            Entree:
            Sortie: list
            Fonction: retourne la liste des themes possible
        """
        return self.listeThemePossible

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
