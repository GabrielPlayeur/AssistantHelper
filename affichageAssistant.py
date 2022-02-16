from tkinter import *
from time import *
from tkinter import filedialog



class Affichage:
    def __init__(self,fenetre):
        self.fenetre = fenetre
        self._texte = StringVar()
        actualfile = False
        self.listeTypes =[("fichier texte",".txt"),("fichier word",".docx"),("autre fichier",".*")]

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
        self.texte.pack(pady = 20,padx = 5,side = LEFT)

        mainmenu = Menu(self.fenetre)
        premierMenu = Menu(mainmenu)
        deuxiemeMenu = Menu(mainmenu)
        troisiemeMenu = Menu(mainmenu)

        premierMenu.add_command(label="Enregistrer",command = self.sauvegarder)
        premierMenu.add_command(label="Enregistrer Sous",command = self.sauvegarder_sous)

        deuxiemeMenu.add_command(label="retour en arriere",command = self.texte.edit_undo)
        deuxiemeMenu.add_command(label="retour en avant",command = self.texte.edit_redo)

        troisiemeMenu.add_command(label="comment ça marche ?",command = self.info)

        mainmenu.add_cascade(label="Fichier",menu = premierMenu)
        mainmenu.add_cascade(label="Edit",menu = deuxiemeMenu)
        mainmenu.add_cascade(label="Info",menu = troisiemeMenu)

        scrol = Scrollbar(self.cadreDuHaut,orient=VERTICAL,command = self.texte.yview)
        scrol.pack(side = RIGHT,padx = 5,pady = 20,fill=Y)

        self.texte.bind("<Control-s>", self.sauvegarder)

        self.fenetre.config(menu=mainmenu)
        self.fenetre.mainloop()

    def verifTexte(self):
        self.texte.delete("1.0",END)
        self.texte.insert(INSERT,self.saisieDeTexte.get())
        tempsLocal = localtime()
        tempsStr = strftime("%d/%m/%Y, %Hh %Mm %Ss", tempsLocal)
        self.texte.insert(INSERT,"\n"*10+"fut demandé le : {}".format(tempsStr))
        self.saisieDeTexte.delete(0,END)

    def info(self):
        nouvellefenetre = Tk()
        nouvellefenetre.geometry("500x600")
        nouvellefenetre.mainloop()

    def sauvegarder(self,*inutile):
        actual_file = False
        if not actual_file:
            self.sauvegarder_sous()
        else:
            open(actual_file, "w").write(self.texte.get(0.,END))

    def sauvegarder_sous(self):
        global actual_file
        actual_file = filedialog.asksaveasfilename(filetypes = self.listeTypes,defaultextension = self.listeTypes)
        open(actual_file, "w").write(self.texte.get(0., END))


if __name__ == "__main__":
    fenetre = Tk()
    fenetre = Affichage(fenetre)
    fenetre.application()
