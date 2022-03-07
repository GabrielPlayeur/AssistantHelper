from outils import Theme, Api
from erreur import erreur

class Crypto(Theme.Theme):
    def __init__(self):
        super().__init__("crypto", 1)

        super().ajouterReconnaisseur("cour","valeur")
        super().ajouterConnecteur("de","du")

        self.api = CryptoApi()

    def action(self):
        self.api.envoyerRequest(self.getElement()[0])
        self.resetElement()

class CryptoApi(Api.Api):
    def __init__(self):
        super().__init__()
        
        self.setUrl("https://api.blockchain.com/v3/exchange")
        
        self.derniereInfoCrypto = {}

    def parametre(self, nomCrypto):
        return f"/l3/{nomCrypto}-USD"

    def envoyerRequest(self, nomCrypto):
        reponse = super().getRequest(nomCrypto)
        if super().checkRequestStatus(reponse):
            self.addDerniereInfoCrypto(reponse.json())
            self.afficherDerniereInfoCrypto(reponse.json()['symbol'])
        elif reponse.status_code == 400:
            self.afficherDerniereInfoCrypto("")
            
    def addDerniereInfoCrypto(self, reponse):
            self.derniereInfoCrypto[reponse['symbol']] = reponse['bids'][0]
        
    def afficherDerniereInfoCrypto(self, symbole):
        print(self.derniereInfoCrypto.get(symbole))
        