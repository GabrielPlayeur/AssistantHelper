from outils import Theme, Api
from erreur import erreur
from random import choice

class PierrePapierCiseau(Theme.Theme):
    def __init__(self):
        super().__init__("pierrePapierCiseau", 1)

        super().ajouterReconnaisseur("jeu","jouons")
        super().ajouterConnecteur("jeu","jouons",":")

        self.choixPierrePapierCiseau = ["pierre","papier","ciseau"]


    def action(self):
        choixJoueur = self.getElement()[0].lower()
        choixAssistant = choice(self.choixPierrePapierCiseau)
        if choixJoueur not in self.choixPierrePapierCiseau:                
            self.affichage(f"Votre choix n'est pas bon {choixJoueur} n'existe pas. Victoire de l'Assistant avec {choixAssistant} par forfait.")
        else:
            numeroVainqueur = self.trouverVainqueur(self.choixPierrePapierCiseau.index(choixJoueur),self.choixPierrePapierCiseau.index(choixAssistant))
            if numeroVainqueur == 2:
                self.affichage(f"Le vainqueur est l'Assistant avec {choixAssistant}.")
            elif numeroVainqueur == 1:
                self.affichage(f"Le vainqueur est le joueur avec {choixJoueur}.")
            else:
                self.affichage(f"Pas de vainqueur match nul avec {choixJoueur}.")

        self.resetElement()

    def trouverVainqueur(self, number1, number2):
        if number1 == number2:
            return 0
        if (number1 == 0 and number2 == 1) or (number1 == 1 and number2 == 2) or (number1 == 2 and number2 == 0):
            return 2
        return 1

    def affichage(self, texte):
        print(texte)