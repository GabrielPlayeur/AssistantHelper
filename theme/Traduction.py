from outils import Theme, Api

class Traduction(Theme.Theme):
    def __init__(self):
        super().__init__("traduction", 2)

        super().ajouterReconnaisseur("traduit","traduction")
        super().ajouterConnecteur("de","en",":")

        self.api = TraductionApi()

    def action(self):
        resultat = self.api.envoyerRequest()        
        self.resetElement()
        return resultat

class TraductionApi(Api.Api):
    def __init__(self):
        super().__init__()

    def envoyerRequest(self):
        return "Work in progress !"