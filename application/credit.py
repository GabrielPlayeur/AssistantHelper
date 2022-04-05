from tkinter import *

class Credit(Tk):
    def __init__(self,application):
        Tk.__init__(self)
        self.application = application
        self.geometry("500x600")
        self.title("Assistant Didier - Credit")
        self.iconbitmap('application/asset/logo.ico')

        self.resizable(width=False, height=False)
        self.fenetre_texte()
        self.mainloop()

    def fenetre_texte(self):
        """
            Entree:
            Sortie:
            Fonction: initialisation des widgets present sur la page
        """
        self.label = Label(self,text = "Crédit :",justify = 'center',font = ("Arial", 24, "bold")).pack(side = "top",pady = 5)
        self.sousLabel = Label(self,text = "Développeur : Gabriel Teigné, Axel Bonneau\nDesigner interface utilisateur: Gabriel Teigné, Axel Bonneau\nGraphiste : Axel Bonneau\nPour l'image : Didier\n",justify = 'left',font = ("Arial", 12),wraplength = 490).pack(pady = 50,side = TOP)

    def destroy(self,*args):
        """
            Entree:
            Sortie:
            Fonction: Reinitialiser la possibilite de lancer une autre fenetre de credit
        """
        self.application.creditsActif = False
        super().destroy()



