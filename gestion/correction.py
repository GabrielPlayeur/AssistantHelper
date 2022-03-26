from autocorrect import Speller

class Correcteur:
    def __init__(self,texte: str):
        self.texte = texte
        self.spell = Speller(lang='fr')
        self.texteCorriger = self.spell(self.texte)

    def check(self):
        """
        Entree: 
        Sortie: bool
        Fonction: renvoie true si le texte a subit des modifications
        """
        return not self.texteCorriger == self.texte
    
    def get(self):
        """
        Entree: 
        Sortie: str
        Fonction: renvoie le texte corriger
        """
        return self.texteCorriger

    
