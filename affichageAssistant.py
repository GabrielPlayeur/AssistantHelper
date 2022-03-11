from tkinter import *
from time import *
from tkinter import filedialog
from outils.pile import *

class Affichage:
    def __init__(self,fenetre):
        self.fenetre = fenetre
        self._texte = StringVar()
        self.actual_file = False
        self.listeTypes =[("fichier texte",".txt"),("autre fichier",".*")]
        self.pileEntree = Pile()
        self.pileSortie = Pile()

    def application(self):
        self.fenetre.geometry("500x600")
        self.fenetre.title("Assistant")
        self.fenetre.resizable(width = False,height = False)

        cadreDuBas = Frame(self.fenetre,bg = "#33A2FF")
        cadreDuBas.pack(side = BOTTOM,fill = X)
        self.cadreDuHaut = Frame(self.fenetre)
        self.cadreDuHaut.pack(side=TOP)

        self.saisieDeTexte = Entry(cadreDuBas,textvariable = self._texte,width = 50,justify=CENTER,bd=1,takefocus=0)
        self.saisieDeTexte.pack(side='left',padx = 50,pady = 25)

        boutonVerif = Button(cadreDuBas,text="verifier",command = self.verifTexte)
        boutonVerif.pack(padx = 0,pady = 25)

        self.texte = Text(self.cadreDuHaut,height=20,width=50,font="Calibri",relief=FLAT)
        self.texte.configure(state='disabled')
        self.texte.pack(pady = 20,padx = 5,side = LEFT)

        mainmenu = Menu(self.fenetre)
        premierMenu = Menu(mainmenu,tearoff= 0)
        deuxiemeMenu = Menu(mainmenu,tearoff= 0)
        troisiemeMenu = Menu(mainmenu,tearoff= 0)

        premierMenu.add_command(label="Enregistrer",accelerator = "Ctrl +s",command = self.sauvegarder)
        premierMenu.add_command(label="Enregistrer Sous",command = self.sauvegarder_sous)

        deuxiemeMenu.add_command(label="retour en arriere",accelerator = "Ctrl + z",command = self.undo)
        deuxiemeMenu.add_command(label="retour en avant",accelerator = "Ctrl + y",command = self.redo)

        troisiemeMenu.add_command(label="comment ça marche ?",command = self.info)
        troisiemeMenu.add_command(label="Crédits",command = self.credits)

        mainmenu.add_cascade(label="Fichier",menu = premierMenu)
        mainmenu.add_cascade(label="Edit",menu = deuxiemeMenu)
        mainmenu.add_cascade(label="Info",menu = troisiemeMenu)

        scrol = Scrollbar(self.cadreDuHaut,orient=VERTICAL,command = self.texte.yview)
        scrol.pack(side = RIGHT,padx = 5,pady = 20,fill=Y,expand = True)

        self.saisieDeTexte.bind("<Control-s>", self.sauvegarder)
        self.saisieDeTexte.bind("<Control-Shift-S>",self.sauvegarder_sous)
        self.saisieDeTexte.bind("<Return>", self.verifTexte)

        self.saisieDeTexte.bind("<Control-z>",self.undo)
        self.saisieDeTexte.bind("<Control-y>",self.redo)

        self.fenetre.config(menu=mainmenu)
        self.fenetre.mainloop()

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


    def verifTexte(self,*args):
        if self.saisieDeTexte.get() != "":
            self.texte.configure(state='normal')
            self.texte.delete("1.0",END)
            self.texte.insert(INSERT,self.saisieDeTexte.get())
            tempsLocal = localtime()
            tempsStr = strftime("%d/%m/%Y, %Hh %Mm %Ss", tempsLocal)
            self.texte.insert(INSERT,"\n"+"fut demandé le : {}".format(tempsStr))
            self.pileEntree.empiler(self.texte.get("1.0",END))
            self.pileSortie = Pile()
            self.saisieDeTexte.delete(0,END)
            self.texte.configure(state='disabled')

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

    def sauvegarder_sous(self,*args):
        self.actual_file = filedialog.asksaveasfilename(filetypes = self.listeTypes,defaultextension = self.listeTypes)
        open(self.actual_file, "w").write(self.texte.get(0., END))

if __name__ == "__main__":
    fenetre = Tk()
    fenetre = Affichage(fenetre)
    fenetre.application()
