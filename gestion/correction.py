from autocorrect import Speller

class Correcteur:
    """
        Entree: str
        Sortie: str
        Fonction: renvoie autre valeur si il y a une faute d'orthographe
    """
    def __init__(self,texte: str):
        self.texte = texte
        self.spell = Speller(lang='fr')
        self.texteCorriger = self.spell(self.texte)

    def check(self):
        if self.texteCorriger == self.texte:
            return False

        return True
    
    def get(self):
        return self.texteCorriger

    
