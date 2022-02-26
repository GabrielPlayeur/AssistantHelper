
class Pile:
    def __init__(self):
        self.liste = []

    def empiler(self,e):

        self.liste.append(e)

    def depiler(self):
        elementDepiler = None
        if len(self.liste) > 0:
            elementDepiler = self.liste.pop()
        return elementDepiler

    def est_pile_vide(self):

        if len(self.liste) == 0:
            return True
        return False

    def get(self):
        return self.liste

if __name__== "__main__":

    Liste = Pile()
    print("est vide:",Liste.est_pile_vide())
    print(Liste.empiler(6))


    print("liste",Liste.get())