from outils import Theme
import tweepy

class Twitter(Theme.Theme):
    def __init__(self):
        super().__init__("twitter", 1)

        super().ajouterReconnaisseur("tweet")
        super().ajouterConnecteur("tweet",":")

        self.api = TwitterApi()

    def action(self):
        resultat = self.api.envoyerRequest(self.getElement()[0])
        self.resetElement()
        return resultat

class TwitterApi:
    def __init__(self):
        #Cle de connection au compte @DidierAssistant
        self.apiKey = "pfkRvbT78KEDpbVbMCkdJuTa3"
        self.apiKeySecret = "dJ6H8RMTQSyFrRaJn8tHYrHLx94Jdm3x9LVq1hxFNUHMFT7T7H"
        self.accessToken = "1504820747071631364-bYwHfsDHEALUIdu1YdjcPKZiyV6jQ0"
        self.accessTokenSecret = "tEiaevdKNjfRwj3I8t6bgCKyX7F06tkgg1JjiP3zeUONA"

        self.auth = tweepy.OAuthHandler(self.apiKey, self.apiKeySecret)
        self.auth.set_access_token(self.accessToken, self.accessTokenSecret)

        self.api = tweepy.API(self.auth)

    def envoyerRequest(self, message: str):
        try:
            self.api.update_status(message)
            return "Le message a bien été posté."
        except tweepy.errors.Unauthorized:
            return "Le message n'a pas pu être posté l'assitant n'a plus les permissions"
        except Exception as e:
            print(e)
            return "Un erreur est survenu lors de la publication du tweet."