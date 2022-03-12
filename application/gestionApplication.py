from application.application import Application
from gestion.gestionTheme import GestionTheme
from audio.gestionCommandeVocal import GestionAudio
from outils.pile import Pile
from erreur import erreur

from time import localtime, strftime
from tkinter import END, INSERT

class GestionApplication:
    def __init__(self):        
        self.theme = GestionTheme()
        self.audio = GestionAudio()
        
        self.app = Application(self)

    def validationRecherche(self, texteAudio="", *args):
        phrase = self.app.saisieDeTexte.get()
        if isinstance(texteAudio, str) and texteAudio != "":
            phrase = texteAudio            
        if phrase != "":
            self.app.texte.configure(state='normal')
            self.app.texte.delete("1.0",END)

            date = strftime('%d/%m/%Y, %Hh %Mm %Ss', localtime())

            if len(self.theme.verifierTheme(phrase)) > 0:

                try:
                    self.theme.themesTrouvesSetElement()                    

                    resultat = self.theme.themesTrouvesAction()
                except erreur.ToManyElement as exception:
                    resultat = exception

                except erreur.MissingElement as exception:
                    resultat = exception

                except erreur.ToManyThemeFind as exception: #Changer pour demander un choix
                    resultat = exception

            else:
                resultat = "Pas de theme trouver en rapport avec la demande"                
                
            texte = f"{phrase}\nfut demandé le : {date}\n{resultat}"

            self.insertTexte(texte)
            self.app.pileEntree.empiler(texte)
            self.app.pileSortie=Pile()

            self.app.saisieDeTexte.delete(0,END)
            self.app.texte.configure(state='disabled')

    def validationAudio(self, *args):
        self.app.audioActif = True
        self.app.saisieDeTexte.configure(state='disabled')
        texteAudio = self.audio.ecouter()
        self.validationRecherche(texteAudio)
        self.app.saisieDeTexte.configure(state='normal')   
        self.app.audioActif = False     

    def insertTexte(self, texte):
        self.app.texte.configure(state='normal')
        self.app.texte.insert(INSERT,texte)
        self.app.texte.configure(state='disabled')

    def run(self):
        self.app.mainloop()