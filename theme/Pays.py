from outils import Theme

class Pays(Theme.Theme):
    def __init__(self):
        super().__init__("pays", 1)

        super().ajouterReconnaisseur("capital","capitale","pays")
        super().ajouterConnecteur("capital","capitale","de","du")
    
    def action(self):
        element = self.getElement()[0].split(" ")
        fd = open("src/pays.csv","r")
        for ligne in fd:
            data = ligne.split(";")
            if element[-1].lower() == data[0].lower():
                
                self.resetElement()
                message = f"La capital de {data[3]} {data[0]} est {data[5][:-1]}."
                return message
        self.resetElement()
        return "Pas de capital trouvé pour {element}."   
        