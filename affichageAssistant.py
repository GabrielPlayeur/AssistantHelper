from tkinter import *
from time import *
from tkinter import filedialog

class Affichage:
    def __init__(self,fenetre):
        self.fenetre = fenetre
        self._texte = StringVar()
        self.actual_file = False
        self.listeTypes =[("fichier texte",".txt"),("autre fichier",".*")]

    def application(self):
        self.fenetre.geometry("500x600")
        self.fenetre.title("Assistant")
        self.fenetre.resizable(width = False,height = False)

        cadreDuBas = Frame(self.fenetre,bg = "#33A2FF")
        cadreDuBas.pack(side = BOTTOM,fill = X)
        self.cadreDuHaut = Frame(self.fenetre)
        self.cadreDuHaut.pack(side=TOP)

        self.saisieDeTexte = Entry(cadreDuBas,textvariable = self._texte,width = 30,justify=CENTER,bd=1,takefocus=0)
        self.saisieDeTexte.pack(side='left',padx = 85,pady = 25)

        boutonVerif = Button(cadreDuBas,text="verifier",command = self.verifTexte)
        boutonVerif.pack(padx = 5,pady = 25)

        self.texte = Text(self.cadreDuHaut,height=20,width=50,font="Calibri",maxundo = 14,undo=True,relief=FLAT)
        self.texte.configure(state='disabled')
        self.texte.pack(pady = 20,padx = 5,side = LEFT)

        mainmenu = Menu(self.fenetre)
        premierMenu = Menu(mainmenu,tearoff= 0)
        deuxiemeMenu = Menu(mainmenu,tearoff= 0)
        troisiemeMenu = Menu(mainmenu,tearoff= 0)

        premierMenu.add_command(label="Enregistrer",command = self.sauvegarder)
        premierMenu.add_command(label="Enregistrer Sous",command = self.sauvegarder_sous)

        deuxiemeMenu.add_command(label="retour en arriere",command = self.texte.edit_undo)
        deuxiemeMenu.add_command(label="retour en avant",command = self.texte.edit_redo)

        troisiemeMenu.add_command(label="comment ça marche ?",command = self.info)
        troisiemeMenu.add_command(label="Crédits",command = self.credits)

        mainmenu.add_cascade(label="Fichier",menu = premierMenu)
        mainmenu.add_cascade(label="Edit",menu = deuxiemeMenu)
        mainmenu.add_cascade(label="Info",menu = troisiemeMenu)

        scrol = Scrollbar(self.cadreDuHaut,orient=VERTICAL,command = self.texte.yview)
        scrol.pack(side = RIGHT,padx = 5,pady = 20,fill=Y)

        self.texte.bind("<Control-s>", self.sauvegarder)
        self.saisieDeTexte.bind("<Control-s>", self.sauvegarder)
        self.saisieDeTexte.bind("<Return>", self.verifTexte)

        self.fenetre.config(menu=mainmenu)
        self.fenetre.mainloop()

    def verifTexte(self,*args):
        if self.saisieDeTexte.get() != "":
            self.texte.configure(state='normal')
            self.texte.delete("1.0",END)
            self.texte.insert(INSERT,self.saisieDeTexte.get())
            tempsLocal = localtime()
            tempsStr = strftime("%d/%m/%Y, %Hh %Mm %Ss", tempsLocal)
            self.texte.insert(INSERT,"\n"*10+"fut demandé le : {}".format(tempsStr))
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

    def sauvegarder_sous(self):
        self.actual_file = filedialog.asksaveasfilename(filetypes = self.listeTypes,defaultextension = self.listeTypes)
        open(self.actual_file, "w").write(self.texte.get(0., END))

if __name__ == "__main__":
    fenetre = Tk()
    fenetre = Affichage(fenetre)
    fenetre.application()
