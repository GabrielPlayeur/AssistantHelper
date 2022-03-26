from outils import Theme

class Calculatrice(Theme.Theme):
    def __init__(self):
        super().__init__("calculatrice", 1)

        super().ajouterReconnaisseur("calcule", "calcul","calculer","somme","produit","facteur","soustrait")
        super().ajouterConnecteur(":", "calcule","calcul","calculer","de","soustrait")

    def action(self):
        element = self.getElement()[0]
        try:
            resultat = eval(element)
        except SyntaxError:
            resultat = "Veuillez entrer des nombres et pas des lettres !"        
        self.resetElement()
        return resultat

