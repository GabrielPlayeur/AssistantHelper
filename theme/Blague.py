from outils import Theme, Api
from erreur import erreur

class Blague(Theme.Theme):
    def __init__(self):
        super().__init__("blague", 1)

        super().ajouterReconnaisseur("blague")
        super().ajouterConnecteur("blague")

        self.api = BlagueApi()

    def action(self):
        self.api.envoyerRequest()
        self.resetElement()

class BlagueApi(Api.Api):
    def __init__(self):
        super().__init__()
        
        self.setApiKey("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjA3MTkwNzgyNjczODEzNTA0IiwibGltaXQiOjEwMCwia2V5IjoiYVdpSkNaTXMzaEY2bjI2S2pKYlUzZkU0VnNnN2Z0V0RBQlNaZGhJWHFwdXRJMlM3b1giLCJjcmVhdGVkX2F0IjoiMjAyMC0wNC0xNVQxMDo0NzowNiswMjowMCIsImlhdCI6MTU4Njk0MDQyNn0.vv1PE6m74sO2E1N97T679NZCQetF82n_54p9MXL1Wdc")
        self.setUrl("https://www.blagues-api.fr/api/random")

    def payload(self):
        return {"Authorization": f"Bearer {self._API_KEY}"}

    def envoyerRequest(self):
        reponse = super().getRequestHeader()
        if super().checkRequestStatus(reponse):
            blague = reponse.json().get("joke")
            blagueReponse = reponse.json().get("answer")
            self.afficherBlague(blague, blagueReponse)
            
    def afficherBlague(self, blague, blagueReponse):
        print(f"{blague}\n{blagueReponse}")