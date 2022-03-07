from gestion.gestionTheme import GestionTheme

def docstring():
        """
            Entree:
            Sortie:
            Fonction:
        """

theme = GestionTheme()
phrase = "Qu elle est la meteo de Marseille ?"
phrase = "Traduit moi en Anglais : salut les amis !"
phrase = "Qu elle est le cour de ETH ?"
phrase = "Fais moi une blague !"
print(theme.verifierTheme(phrase))
theme.themesTrouvesSetElement()
theme.themesTrouvesAction()