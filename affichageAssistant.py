from tkinter import *
from time import localtime, strftime
from tkinter import filedialog

class Application(Tk):
    def __init__(self):        
        Tk.__init__(self)

        self.geometry("500x600")
        self.title("Assistant")
        self.resizable(width = False,height = False)

        self._texte = StringVar()
        self.actual_file = False
        self.listeTypes =[("fichier texte",".txt"),("autre fichier",".*")]

        self.creerWidgets()
        self.creerMenu()
        self.creerAction()

        self.config(menu=self.mainmenu)

    def creerWidgets(self):
        self.cadreDuBas = Frame(self,bg = "#33A2FF")        
        self.cadreDuBas.pack(side = BOTTOM,fill = X)
        self.cadreDuHaut = Frame(self)
        self.cadreDuHaut.pack(side=TOP)

        self.saisieDeTexte = Entry(self.cadreDuBas,textvariable = self._texte,width = 30,justify=CENTER,bd=1,takefocus=0)
        self.saisieDeTexte.pack(side='left',padx = 85,pady = 25)

        self.boutonVerif = Button(self.cadreDuBas,text="verifier",command = self.verifTexte)
        self.boutonVerif.pack(padx = 5,pady = 25)

        self.texte = Text(self.cadreDuHaut,height=20,width=50,font="Calibri",maxundo = 14,undo=True,relief=FLAT)
        self.texte.configure(state='disabled')
        self.texte.pack(pady = 20,padx = 5,side = LEFT)        

        self.scrol = Scrollbar(self.cadreDuHaut,orient=VERTICAL,command = self.texte.yview)
        self.scrol.pack(side = RIGHT,padx = 5,pady = 20,fill=Y)

    def creerMenu(self):
        self.mainmenu = Menu(self)
        self.premierMenu = Menu(self.mainmenu,tearoff= 0)
        self.deuxiemeMenu = Menu(self.mainmenu,tearoff= 0)
        self.troisiemeMenu = Menu(self.mainmenu,tearoff= 0)

        self.premierMenu.add_command(label="Enregistrer",command = self.sauvegarder)
        self.premierMenu.add_command(label="Enregistrer Sous",command = self.sauvegarder_sous)

        self.deuxiemeMenu.add_command(label="retour en arriere",command = self.texte.edit_undo)
        self.deuxiemeMenu.add_command(label="retour en avant",command = self.texte.edit_redo)

        self.troisiemeMenu.add_command(label="comment ça marche ?",command = self.info)
        self.troisiemeMenu.add_command(label="Crédits",command = self.credits)

        self.mainmenu.add_cascade(label="Fichier",menu = self.premierMenu)
        self.mainmenu.add_cascade(label="Edit",menu = self.deuxiemeMenu)
        self.mainmenu.add_cascade(label="Info",menu = self.troisiemeMenu)

    def creerAction(self):
        self.texte.bind("<Control-s>", self.sauvegarder)
        self.saisieDeTexte.bind("<Control-s>", self.sauvegarder)
        self.saisieDeTexte.bind("<Return>", self.verifTexte)        

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
    app = Application()
    app.mainloop()
