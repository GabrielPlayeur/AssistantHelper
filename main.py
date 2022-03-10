from gestion.gestionTheme import GestionTheme
from audio.gestionCommandeVocal import GestionAudio

def docstring():
        """
            Entree:
            Sortie:
            Fonction:
        """

theme = GestionTheme()
audio = GestionAudio()
phrase = "Qu elle est la météo à Beaupreau ?"
phrase = "Traduit moi en Anglais : salut les amis !"
phrase = "Qu elle est le cour de BTC ?"
phrase = "Donne moi ta meilleure blague !"
phrase = "Jouons papier"
phrase = "donne-moi la météo à Paris s'il te plaît"

print(theme.verifierTheme(phrase))
theme.themesTrouvesSetElement()
theme.themesTrouvesAction()

phrase = audio.ecouter()
print(phrase)
print(theme.verifierTheme(phrase))
theme.themesTrouvesSetElement()
theme.themesTrouvesAction()