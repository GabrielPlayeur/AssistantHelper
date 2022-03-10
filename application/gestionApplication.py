from application.application import Application
from gestion.gestionTheme import GestionTheme
from audio.gestionCommandeVocal import GestionAudio
from outils.pile import Pile

from time import localtime, strftime
from tkinter import END, INSERT

class GestionApplication:
    def __init__(self):
        self.app = Application(self)

        self.theme = GestionTheme()
        self.audio = GestionAudio()

    def validationRecherche(self, *args):
        if self.app.saisieDeTexte.get() != "":            
            self.app.texte.configure(state='normal')
            self.app.texte.delete("1.0",END)

            phrase = self.app.saisieDeTexte.get()
            date = strftime('%d/%m/%Y, %Hh %Mm %Ss', localtime())

            print(self.theme.verifierTheme(phrase))
            self.theme.themesTrouvesSetElement()
            resultat = self.theme.themesTrouvesAction()

            texte = f"{phrase}\nfut demandé le : {date}\n{resultat}"
            self.insertTexte(texte)
            self.app.pileEntree.empiler(texte)
            self.app.pileSortie=Pile()

            self.app.saisieDeTexte.delete(0,END)            
            self.app.texte.configure(state='disabled')

    def insertTexte(self, texte):
        self.app.texte.configure(state='normal')
        self.app.texte.insert(INSERT,texte)
        self.app.texte.configure(state='disabled')

    def run(self):
        self.app.mainloop()