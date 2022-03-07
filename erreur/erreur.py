
class MissingElement(Exception):
    def __init__(self, element, nombreElementDemande):
        self.element = element
        self.nombreElementDemande = nombreElementDemande
        self.message = f"Le nombre d'element donné est insufisant, il en faut {self.nombreElementDemande}.Element donné: {self.element}."
        super().__init__(self.message)

class ToManyElement(Exception):
    def __init__(self, element, nombreElementDemande):
        self.element = element
        self.nombreElementDemande = nombreElementDemande
        self.message = f"Le nombre d'element donné est trop grand, il en faut {self.nombreElementDemande}. Element donné: {self.element}."
        super().__init__(self.message)

class ToManyThemeFind(Exception):
    def __init__(self, themesTrouves):
        self.themesTrouves = themesTrouves
        self.message = f"Le nombre de theme trouvé est trop grand. Themes trouvé: {self.themesTrouves}."
        super().__init__(self.message)