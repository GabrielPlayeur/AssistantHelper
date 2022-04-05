from application.application import Application
from gestion.gestionTheme import GestionTheme
from audio.gestionCommandeVocal import GestionAudio
from outils.pile import Pile
from erreur import erreur
from log.gestionLog import *

from time import localtime, strftime
from tkinter import END, INSERT

class GestionApplication:
    def __init__(self):
        self.theme = GestionTheme()
        self.audio = GestionAudio()

        self.logger = Logger("log/info.log")
        self.app = Application(self)

    def validationRecherche(self, texteAudio="", *args):
        """
            Entree: texteAudio (str)
            Sortie:
            Fonction: Effectue les actions necessaire pour donner une reponse a la phrase donne :
                - trouver les themes et les elements
                - gerer les eventuelles incomprehensions
                - effectuer l'action
                - afficher le resultat de l'action dans la zone de reponse
        """
        phrase = self.app.saisieDeTexte.get()
        if isinstance(texteAudio, str) and texteAudio != "":
            phrase = texteAudio
        if phrase == "":
            return

        self.app.texte.configure(state='normal')
        self.app.texte.delete("1.0",END)

        date = strftime('%d/%m/%Y, %Hh %Mm %Ss', localtime())

        if len(self.theme.verifierTheme(phrase)) > 0:
            resultat = self.recuperationResultat()
        else:
            reponse, phrase = self.theme.verifierOrthographe(phrase)
            if reponse == True and len(self.theme.verifierTheme(phrase)) > 0:                
                logging.info("Correction de la phrase en "+phrase)
                resultat = self.recuperationResultat()
            else:
                resultat = "Pas de theme trouver en rapport avec la demande"

        logging.info(self.theme.themesTrouves)

        texte = f"{phrase}\nfut demandé le : {date}\n\n{resultat}"

        self.insertTexte(texte)
        self.app.pileEntree.empiler(texte) #Ajout du texte a la pile d'evenement
        self.app.pileSortie=Pile()

        self.app.saisieDeTexte.delete(0,END)
        self.app.texte.configure(state='disabled')

    def recuperationResultat(self):
        """
            Entree:
            Sortie: str
            Fonction: Selectionne la reponse revoie par l'assistant en fonction des situations
        """
        try:
            self.theme.themesTrouvesSetElement()

            resultat = self.theme.themesTrouvesAction()
        except erreur.ToManyElement as exception:
            resultat = exception

        except erreur.MissingElement as exception:
            resultat = exception

        except erreur.ToManyThemeFind as exception:
            resultat = exception
        return resultat

    def validationAudio(self, *args):
        """
            Entree:
            Sortie:
            Fonction: active l'ecoute du micro et recherche les themes present dans le texte entendu
        """
        self.app.audioActif = True
        self.app.saisieDeTexte.configure(state='disabled')        
        logging.info("Debut de l'ecoute du micro")
        texteAudio = self.audio.ecouter()        
        logging.info("Fin de l'ecoute du micro")
        self.validationRecherche(texteAudio)
        self.app.saisieDeTexte.configure(state='normal')
        self.app.audioActif = False

    def insertTexte(self, texte: str):
        """
            Entree: texte (str)
            Sortie:
            Fonction: ajoute a la zone de reponse le texte donne en parametre
        """
        self.app.texte.configure(state='normal')
        self.app.texte.insert(INSERT,texte)
        self.app.texte.configure(state='disabled')

    def run(self):
        """
            Entree:
            Sortie:
            Fonction: lance l'application
        """        
        logging.info("Lancement de l'application")
        self.app.mainloop()        
        logging.info("Fermeture de l'application")