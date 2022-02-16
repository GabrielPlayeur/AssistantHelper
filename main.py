from gestion.gestionTheme import GestionTheme

def docstring():
        """
            Entree:
            Sortie:
            Fonction:
        """

theme = GestionTheme()
print(theme.verifierTheme("Donne moi la meteo de cholet")[0].action("cholet"))
print(theme.verifierTheme("Donne moi l heure a cholet"))