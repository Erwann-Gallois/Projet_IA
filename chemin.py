class Chemin:
    def __init__(self, depart, arrivee):
        self.depart = depart
        self.arrivee = arrivee
        self.score = depart.distance(arrivee)
        self.chemin = [depart, arrivee]

    def toString(self):
        return self.depart.toString() + " -> " + self.arrivee.toString() + " : " + str(self.score)
    