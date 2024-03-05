import numpy as np
nbre_ville = 5
nbre_chemin = 10
nbre_generation = 100

cities = []
for i in range(nbre_ville):
    city = City("Ville " + str(i), np.random.randint(0, 200), np.random.randint(0, 200))
