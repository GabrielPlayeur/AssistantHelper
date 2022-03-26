from tkinter import *
from tkinter import filedialog
import threading

from outils.pile import Pile
from application.credit import Credit
from application.info import Info

class Application(Tk):
    def __init__(self, gestionnaire):
        Tk.__init__(self)

        self.gestionnaire = gestionnaire

        self.geometry("500x600")
        self.title("Assistant Didier")
        self.iconbitmap('application/asset/logo.ico')

        self.resizable(width=False, height=False)

        self._texte = StringVar()
        self.actual_file = False
        self.listeTypes = [("fichier texte", ".txt"), ("autre fichier", ".*")]

        self.pileEntree = Pile()
        self.pileSortie = Pile()

        self.audioActif = False
        self.creditsActif = False
        self.infoActif = False

        self.creerWidgets()
        self.creerMenu()
        self.creerAction()

        self.config(menu=self.mainmenu)

    def creerWidgets(self):
        self.cadreDuHaut = Frame(self)
        self.cadreDuHaut.pack(side=TOP)
        self.cadreDuBas = Frame(self, bg="#33A2FF")
        self.cadreDuBas.pack(side = BOTTOM,fill = X)

        self.texte = Text(self.cadreDuHaut, height=25, width=50, font="Calibri", relief=FLAT)
        self.texte.configure(state='disabled')
        self.texte.pack(pady=5, padx=5, side=LEFT)

        self.scrol = Scrollbar(self.cadreDuHaut, orient=VERTICAL, command=self.texte.yview)
        self.scrol.pack(side=RIGHT, padx=5, pady=5, fill=Y, expand=True)

        self.boutonAudio = Button(self.cadreDuBas, text="PARLER", command=self.audioAction)
        self.boutonAudio.pack(padx=5, pady=25, side=LEFT)

        self.saisieDeTexte = Entry(self.cadreDuBas, textvariable=self._texte, width=60, justify=CENTER, bd=1, takefocus=0)
        self.saisieDeTexte.pack(side='left', padx=5, pady=25,fill = Y)

        self.boutonVerif = Button(self.cadreDuBas, text="ENTRER", command=self.gestionnaire.validationRecherche)
        self.boutonVerif.pack(side= "left",padx=5, pady=25)



    def creerMenu(self):
        self.mainmenu = Menu(self)
        self.premierMenu = Menu(self.mainmenu,tearoff=0)
        self.deuxiemeMenu = Menu(self.mainmenu,tearoff=0)
        self.troisiemeMenu = Menu(self.mainmenu,tearoff=0)

        self.premierMenu.add_command(label="Enregistrer", accelerator="Ctrl + s", command=self.sauvegarder)
        self.premierMenu.add_command(label="Enregistrer Sous", command=self.sauvegarder_sous)
        self.premierMenu.add_command(label="Ecoute du micro", accelerator="Ctrl + r", command=self.audioAction)

        self.deuxiemeMenu.add_command(label="retour en arriere", accelerator="Ctrl + z", command=self.undo)
        self.deuxiemeMenu.add_command(label="retour en avant", accelerator="Ctrl + y", command=self.redo)

        self.troisiemeMenu.add_command(label="comment ça marche ?", command=self.info)
        self.troisiemeMenu.add_command(label="Crédits", command=self.credits)

        self.mainmenu.add_cascade(label="Fichier", menu=self.premierMenu)
        self.mainmenu.add_cascade(label="Edit", menu=self.deuxiemeMenu)
        self.mainmenu.add_cascade(label="Aide", menu=self.troisiemeMenu)

    def creerAction(self):
        self.bind("<Control-s>", self.sauvegarder)
        self.bind("<Control-r>",self.audioAction)
        self.bind("<Control-z>",self.undo)
        self.bind("<Control-y>",self.redo)

        self.saisieDeTexte.bind("<Return>", self.gestionnaire.validationRecherche)

    def undo(self,*args):
        self.texte.configure(state="normal")
        self.texte.delete("1.0",END)
        if self.pileEntree.est_pile_vide():
            return
        self.pileSortie.empiler(self.pileEntree.depiler())
        nouveautexte = self.pileEntree.depiler()
        if nouveautexte != None:
            self.texte.insert(INSERT,nouveautexte)
            self.pileEntree.empiler(nouveautexte)
        self.texte.configure(state="disabled")

    def redo(self,*args):
        if self.pileSortie.est_pile_vide():
            return
        self.texte.configure(state="normal")
        nouveautexte = self.pileSortie.depiler()
        self.pileEntree.empiler(nouveautexte)
        self.texte.delete("1.0",END)
        self.texte.insert(INSERT,nouveautexte)
        self.texte.configure(state="disabled")

    def audioAction(self):
        if not self.audioActif:
            threading.Thread(target=self.gestionnaire.validationAudio).start()

    def credits(self):
        if not self.creditsActif:
            self.creditsActif = True
            Credit(self)

    def info(self):
        if not self.infoActif:
            self.infoActif = True
            Info(self)

    def sauvegarder(self,*args):
        if not self.actual_file:
            self.sauvegarder_sous()
        else:
            open(self.actual_file, "w").write(self.texte.get(0.,END))

    def sauvegarder_sous(self):
        self.actual_file = filedialog.asksaveasfilename(filetypes = self.listeTypes,defaultextension = self.listeTypes)
        open(self.actual_file, "w").write(self.texte.get(0., END))