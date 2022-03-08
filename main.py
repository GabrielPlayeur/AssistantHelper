from gestion.gestionTheme import GestionTheme

def docstring():
        """
            Entree:
            Sortie:
            Fonction:
        """

theme = GestionTheme()
phrase = "Qu elle est la meteo a Marseille ?"
phrase = "Traduit moi en Anglais : salut les amis !"
phrase = "Qu elle est le cour de ETH ?"
phrase = "Donne moi ta meilleure blague !"
phrase = "Jouons papier"
print(theme.verifierTheme(phrase))
theme.themesTrouvesSetElement()
theme.themesTrouvesAction()

from temp import audio

phrase = audio.getAudioListen()
print(phrase)
print(theme.verifierTheme(phrase))
theme.themesTrouvesSetElement()
theme.themesTrouvesAction()