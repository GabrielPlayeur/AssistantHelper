from gestion.gestionTheme import GestionTheme

def docstring():
        """
            Entree:
            Sortie:
            Fonction:
        """

theme = GestionTheme()
phrase = "Qu elle est la meteo de Marseille ?"
print(theme.verifierTheme(phrase))
theme.themesTrouvesSetElement()
theme.themesTrouvesAction()