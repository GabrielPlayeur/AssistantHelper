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
        self.label = Label(self,text = "Crédit :",justify = 'center',font = ("Arial", 24, "bold")).pack(side = "top",pady = 5)
        self.sousLabel = Label(self,text = "Développeur : Gabriel Teigné\nGraphiste : Axel Bonneau\nPour l'image : Didier\nA prêter sa voie : Didier\nMerci Didier !!!\nMerci aussi à Gabriel\net moi (Axel)",justify = 'left',font = ("Arial", 16,)).pack(pady = 5,side = LEFT)

    def destroy(self,*args):
        self.application.creditsActif = False
        super().destroy()



