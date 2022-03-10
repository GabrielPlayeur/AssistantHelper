
class MissingElement(Exception):
    def __init__(self, element: list, nombreElementDemande: int):
        """
            Entree: element (list), nombreElementDemande (int)
            Sortie:
            Fonction: Exception leve lorsqu'il manque des elements pour pouvoir utiliser un theme
        """
        self.element = element
        self.nombreElementDemande = nombreElementDemande
        self.message = f"Le nombre d'element donné est insufisant, il en faut {self.nombreElementDemande}. Element donné: {self.element}."
        super().__init__(self.message)

class ToManyElement(Exception):
    def __init__(self, element: list, nombreElementDemande: int):
        """
            Entree: element (list), nombreElementDemande (int)
            Sortie:
            Fonction: Exception leve lorsqu'il y a trop d'elements donne pour pouvoir utiliser un theme
        """
        self.element = element
        self.nombreElementDemande = nombreElementDemande
        self.message = f"Le nombre d'element donné est trop grand, il en faut {self.nombreElementDemande}. Element donné: {self.element}."
        super().__init__(self.message)

class ToManyThemeFind(Exception):
    def __init__(self, themesTrouves: list):
        """
            Entree: themesTrouves (list)
            Sortie:
            Fonction: Exception leve lorsqu'il y a plusieur theme trouver pour pouvoir executer une action de theme
        """
        self.themesTrouves = themesTrouves
        self.message = f"Le nombre de theme trouvé est trop grand. Themes trouvé: {self.themesTrouves}."
        super().__init__(self.message)