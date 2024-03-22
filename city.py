import numpy as np
class City :
    # * Constructeur de la classe "city"
    def __init__ (self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def getDistance (self, city):
        # * Distance entre deux villes en x
        xDis = abs(self.x - city.x)
        # * Distance entre deux villes en y
        yDis = abs(self.y - city.y)
        # * Distance entre deux villes en utilisant le théorème de Pythagore
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def toString (self):
        print(self.name + "(" + str(self.x) + "," + str(self.y) + ")")
    
