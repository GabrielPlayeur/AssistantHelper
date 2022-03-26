from outils import Theme, Api

class Crypto(Theme.Theme):
    def __init__(self):
        super().__init__("crypto", 1)

        super().ajouterReconnaisseur("cours","valeur","prix","echanges","echange","cour")
        super().ajouterConnecteur("de","du")

        self.api = CryptoApi()

    def action(self):
        resultat = self.api.envoyerRequest(self.getElement()[0])        
        self.resetElement()
        return resultat

class CryptoApi(Api.Api):
    def __init__(self):
        super().__init__()
        
        self.setUrl("https://api.blockchain.com/v3/exchange")
        
        self.derniereInfoCrypto = {}

    def parametre(self, nomCrypto: str):
        return f"/l3/{nomCrypto}-USD"

    def envoyerRequest(self, nomCrypto: str):
        reponse = super().getRequest(nomCrypto)
        if super().checkRequestStatus(reponse):
            self.addDerniereInfoCrypto(reponse.json())
            cryptoTrouve = self.derniereInfoCrypto.get(reponse.json()['symbol'])
            return f"{reponse.json()['symbol']} est actuelement à {cryptoTrouve['px']}$."
        elif reponse.status_code == 400:
            return "Pas de crypto existante"
        else:
            return super().pasResultat()
            
    def addDerniereInfoCrypto(self, reponse: dict):
        """
            Entree: reponse (dict)
            Sortie:
            Fonction: mettre a jour les information sur la crypto demande
        """
        self.derniereInfoCrypto[reponse['symbol']] = reponse['bids'][0]
        