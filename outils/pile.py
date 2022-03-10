
class Pile:
    def __init__(self):
        self.liste = []

    def empiler(self, *args):
        for element in args:
            self.liste.insert(0,element)

    def depiler(self):
        if not est_pile_vide(self.liste):
            element = self.liste[0]
            del self.liste[0]
            return element
        return None

    def derniere_element(self):
        return self.liste[0]

    def est_pile_vide(self):
        return len(self.liste) == 0

def cree_pile_vide():
    return list()

def empiler(P,*args):
    for element in args:
        P.insert(0,element)
    return P

def depiler(P):
    if not est_pile_vide(P):
        element = P[0]
        del P[0]
        return P, element
    return P, None

def derniere_element(P):
    return P[0]

def est_pile_vide(P):
    if len(P) == 0:
        return True
    return False

if __name__ == '__main__':
    uneSuperbePile = cree_pile_vide()
    print("uneSuperbePile = cree_pile_vide() ->", uneSuperbePile)

    print("est_pile_vide(uneSuperbePile) ->",est_pile_vide(uneSuperbePile))

    uneSuperbePile, element = depiler(uneSuperbePile)
    print("uneSuperbePile, element = depiler(uneSuperbePile) ->", uneSuperbePile, element)

    uneSuperbePile = empiler(uneSuperbePile, 'Une chose')
    print("uneSuperbePile = empiler(uneSuperbePile, 'Une chose') ->", uneSuperbePile)

    print("est_pile_vide(uneSuperbePile)",est_pile_vide(uneSuperbePile))

    uneSuperbePile = empiler(uneSuperbePile, 'Une autre chose')
    print("uneSuperbePile = empiler(uneSuperbePile, 'Une autre chose') ->", uneSuperbePile)


    uneSuperbePile = empiler(uneSuperbePile, 'Une autre derniere chose')
    print("uneSuperbePile = empiler(uneSuperbePile, 'Une autre derniere chose') ->", uneSuperbePile)

    uneSuperbePile, element = depiler(uneSuperbePile)
    print("uneSuperbePile, element = depiler(uneSuperbePile) ->", uneSuperbePile, element)