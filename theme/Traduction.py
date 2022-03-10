from outils import Theme, Api
from erreur import erreur

class Traduction(Theme.Theme):
    def __init__(self):
        super().__init__("traduction", 2)

        super().ajouterReconnaisseur("traduit","traduction")
        super().ajouterConnecteur("de","en",":")

        self.api = TraductionApi()

    def action(self):
        self.api.envoyerRequest()
        self.resetElement()

class TraductionApi(Api.Api):
    def __init__(self):
        super().__init__()

    def envoyerRequest(self):
        print("Work in progress !")