from outils import Theme, Api
from erreur import erreur

class Calculatrice(Theme.Theme):
    def __init__(self):
        super().__init__("calculatrice", 1)

        super().ajouterReconnaisseur("calcule","calculer")
        super().ajouterConnecteur(":")


    def action(self):

        element = self.getElement()[0]
        try:
            print(eval(element))
        except SyntaxError:
            print("Veuillez entrer des nombres et pas des lettres !")
        
        self.resetElement()

