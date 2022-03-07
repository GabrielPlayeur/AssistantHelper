from outils import Theme, Api
from erreur import erreur

class Crypto(Theme.Theme):
    def __init__(self):
        super().__init__("crypto", 1)

        super().ajouterReconnaisseur("cour","valeur")
        super().ajouterConnecteur("de","du","l")

        self.api = TraductionApi()

    def action(self):
        self.api.envoyerRequest(self.getElement()[0])
        self.resetElement()

class TraductionApi(Api.Api):
    def __init__(self):
        super().__init__()
        
        self.URL = "https://api.blockchain.com/v3/exchange"

    def parametre(self, nomCrypto):
        return f"/l3/{nomCrypto}-USD"

    def envoyerRequest(self, nomCrypto):
        reponse = super().getRequest(nomCrypto)
        print(reponse.json()['bids'][0])