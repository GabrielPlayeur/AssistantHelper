from tkinter import *

class Information(Tk):
    def __init__(self,application):
        Tk.__init__(self)
        self.application = application
        self.geometry("500x600")
        self.title("Assistant Didier - Information")
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
        self.label1 = Label(self,text = "Information :",justify = 'left',font = ("Arial", 24, "bold")).pack(pady = 5)
        self.label2 = Label(self,text = "Présentation des différentes option de l'Assistant Didier :",justify = 'left',font = ("Arial", 16, "bold"),wraplength = 490).pack(pady=5,padx=5)
        self.fonctionnement = Label(self, text = "Exemple de phrase sur les thèmes :",justify = 'left',font = ("Arial", 16, "bold"),wraplength = 490).pack(pady=5,padx=5)
        self.theme = Label(self, text = "Météo : Quelle est la météo à Beaupreau ?\n\nCryptomonnaie : Qu'elle est le cours de BTC ?\n\nBlague : Donne moi ta meilleure blague !\n\nFuseau Horaire : Quelle est l'heure à Paris ?\n\nCalculatrice : Calcule : 5 + 5\n\nDictionnaire : Donne moi la définition de chat\n\nE-Mail : Envoie un mail a mail@gmail.com : Bonjour comment vas tu ?\n\nTweeter : Tweet : Bonjour comment allez vous ?\n\nPierre-Papier-Ciseau : Jouons papier\n\nActualité : News de tesla\n\nCapital : Capital de la France",justify = 'left',font = ("Arial", 12),wraplength = 490).pack(pady=5,padx=5)

    def destroy(self,*args):
        """
            Entree:
            Sortie:
            Fonction: Reinitialiser la possibilite de lancer une autre fenetre d'information
        """
        self.application.infoActif = False
        super().destroy()

