from outils import Theme, Api
from datetime import datetime

class Actualite(Theme.Theme):
    def __init__(self):
        super().__init__("actualite", 1)

        super().ajouterReconnaisseur("news","journal","information","actualite")
        super().ajouterConnecteur("de",":","sur")

        self.api = ActualiteApi()

    def action(self):
        resultat = self.api.envoyerRequest(self.getElement()[0])
        self.resetElement()
        return resultat

class ActualiteApi(Api.Api):
    def __init__(self):
        super().__init__()

        self.setUrl("https://newsapi.org/v2/everything")
        self.setApiKey("8e851902b10e46ea9ccb49dff7e54e06")

        self.info = {}

    def parametre(self, mot: str):
        date = datetime.now()
        dateDebut = date.strftime("%Y/%m/%d")
        dateFin = date.strftime("%Y/%m/%d")
        return f"?q={mot}&from={dateDebut}&to={dateFin}&sortBy=popularity&apiKey={self._API_KEY}"

    def envoyerRequest(self, mot: str):
        reponse = super().getRequest(mot)
        if super().checkRequestStatus(reponse) and len(reponse.json()["articles"]):
            article = reponse.json()["articles"][0]
            self.addDerniereActu(article)
            return self.afficherArticle(self.info[article["url"]])
        return "Pas d'article sur le sujet aujourd'hui"

    def addDerniereActu(self, article: dict):
        """
            Entree: article (dict)
            Sortie:
            Fonction: Mettre dans en format le json recu sur un article pour pouvoir le reutiliser plus facilement apres
        """
        self.info[article["url"]] = {"author": article["author"], "title": article["title"], "date":article["publishedAt"], "description": article["description"], "site": article["source"]["name"],"url": article["url"]}

    def afficherArticle(self, article: dict):
        """
            Entree: article (dict)
            Sortie: str
            Fonction: retourne une chaine de caractere d'artcile mit en forme pour l'afficher
        """
        return f"{article['title']}\n{article['site']}\n{article['author']} - {article['date']}\n\n{article['description']}\n\n{article['url']}"