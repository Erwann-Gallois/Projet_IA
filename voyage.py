class Voyage :
    def __init__(self, chemin):
        self.chemin = chemin
        self.score = self.setScore()
    
    def setScore(self):
        sum = 0
        for i in range(0, len(self.chemin) - 1):
            sum = sum + self.chemin[i].getDistance(self.chemin[i+1])
        return sum
    
    def toString(self):
        for i in range(len(self.chemin)):
            self.chemin[i].toString()
        print("Score : " + str(self.score))