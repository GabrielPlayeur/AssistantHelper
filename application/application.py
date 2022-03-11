from tkinter import *
from tkinter import filedialog
import threading

from outils.pile import Pile

class Application(Tk):
    def __init__(self, gestionnaire):
        Tk.__init__(self)
        
        self.gestionnaire = gestionnaire

        self.geometry("500x600")
        self.title("Assistant")
        self.resizable(width = False,height = False)

        self._texte = StringVar()
        self.actual_file = False
        self.listeTypes =[("fichier texte",".txt"),("autre fichier",".*")]        
        
        self.pileEntree = Pile()
        self.pileSortie = Pile()

        self.creerWidgets()
        self.creerMenu()
        self.creerAction()

        self.config(menu=self.mainmenu)

    def creerWidgets(self):
        self.cadreDuBas = Frame(self, bg="#33A2FF")        
        self.cadreDuBas.pack(side = BOTTOM, fill=X)
        self.cadreDuHaut = Frame(self)
        self.cadreDuHaut.pack(side=TOP)

        self.boutonAudio = Button(self.cadreDuBas, text="parler", command=self.audioAction)
        self.boutonAudio.pack(padx=20, pady=25, side=LEFT)

        self.saisieDeTexte = Entry(self.cadreDuBas, textvariable=self._texte, width=30, justify=CENTER, bd=1, takefocus=0)
        self.saisieDeTexte.pack(side='left', padx=25, pady=25)

        self.boutonVerif = Button(self.cadreDuBas, text="verifier", command=self.gestionnaire.validationRecherche)
        self.boutonVerif.pack(padx=0, pady=25)

        self.texte = Text(self.cadreDuHaut, height=20, width=50, font="Calibri", relief=FLAT)
        self.texte.configure(state='disabled')
        self.texte.pack(pady=20, padx=5, side=LEFT)        

        self.scrol = Scrollbar(self.cadreDuHaut, orient=VERTICAL, command=self.texte.yview)
        self.scrol.pack(side=RIGHT, padx=5, pady=20, fill=Y, expand=True)

    def creerMenu(self):
        self.mainmenu = Menu(self)
        self.premierMenu = Menu(self.mainmenu,tearoff=0)
        self.deuxiemeMenu = Menu(self.mainmenu,tearoff=0)
        self.troisiemeMenu = Menu(self.mainmenu,tearoff=0)

        self.premierMenu.add_command(label="Enregistrer", command=self.sauvegarder)
        self.premierMenu.add_command(label="Enregistrer Sous", command=self.sauvegarder_sous)

        self.deuxiemeMenu.add_command(label="retour en arriere", command=self.undo)
        self.deuxiemeMenu.add_command(label="retour en avant", command=self.redo)

        self.troisiemeMenu.add_command(label="comment ça marche ?", command=self.info)
        self.troisiemeMenu.add_command(label="Crédits", command=self.credits)

        self.mainmenu.add_cascade(label="Fichier", menu=self.premierMenu)
        self.mainmenu.add_cascade(label="Edit", menu=self.deuxiemeMenu)
        self.mainmenu.add_cascade(label="Info", menu=self.troisiemeMenu)

    def creerAction(self):        
        self.bind("<Control-s>", self.sauvegarder)     
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
        threading.Thread(target=self.gestionnaire.validationAudio).start()

    def credits(self):
        nouvellefenetre = Tk()
        nouvellefenetre.title("Crédits")
        nouvellefenetre.geometry("500x600")
        nouvellefenetre.mainloop()

    def info(self):
        nouvellefenetre = Tk()
        nouvellefenetre.title("comment ça marche ?")
        nouvellefenetre.geometry("500x600")
        nouvellefenetre.mainloop()

    def sauvegarder(self,*args):
        if not self.actual_file:
            self.sauvegarder_sous()
        else:
            open(self.actual_file, "w").write(self.texte.get(0.,END))

    def sauvegarder_sous(self):
        self.actual_file = filedialog.asksaveasfilename(filetypes = self.listeTypes,defaultextension = self.listeTypes)
        open(self.actual_file, "w").write(self.texte.get(0., END))