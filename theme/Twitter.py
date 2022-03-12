from outils import Theme, Api

class Twitter(Theme.Theme):
    def __init__(self):
        super().__init__("twitter", 1)

        super().ajouterReconnaisseur("tweet")
        super().ajouterConnecteur("tweet",":")

        self.api = TwitterApi()

    def action(self):
        resultat = self.getElement()
        self.resetElement()
        return resultat

class TwitterApi(Api.Api):
    def __init__(self):
        super().__init__()

    def envoyerRequest(self):
        return "Work in progress !"