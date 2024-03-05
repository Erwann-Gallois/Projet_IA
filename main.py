import numpy as np
import matplotlib.pyplot as plt
from city import City
from chemin import Chemin

taille_x = 500
taille_y = 500
nbre_ville = 20
nbre_generation = 100



cities = []
# Creer des villes aleatoires
for i in range(nbre_ville):
    city = City("Ville " + str(i+1), np.random.randint(0, taille_x), np.random.randint(0, taille_y))
    cities.append(city)

# Creer des chemins aleatoires
chemins = []
for i in range(nbre_ville - 1):
    depart = cities[np.random.randint(0, nbre_ville)]
    arrivee = cities[np.random.randint(0, nbre_ville)]
    if depart == arrivee:
        while depart == arrivee:
            arrivee = cities[np.random.randint(0, nbre_ville)]
    chemin = Chemin(depart, arrivee, depart.distance(arrivee))
    chemins.append(chemin)

for i in range(nbre_ville - 1):
    print(chemins[i].toString())

# Afficher les villes sur une grille
fig, ax = plt.subplots()
for city in cities:
    # Creer un point pour chaque ville avec une couleur aleatoire
    ax.scatter(city.x, city.y, color=np.random.rand(3,))
    ax.text(city.x, city.y, city.name) # Affiche le nom de la ville

# Creer un chemin entre chaque ville
for chemin in chemins:
    ax.plot([chemin.depart.x, chemin.arrivee.x], [chemin.depart.y, chemin.arrivee.y], color='black')
    mid_x = (chemin.depart.x + chemin.arrivee.x) / 2
    mid_y = (chemin.depart.y + chemin.arrivee.y) / 2
    ax.annotate(str(chemin.score), (mid_x, mid_y))
ax.set_xticks([])  # Crée une grille x avec des intervalles de 20
ax.set_yticks([])  # Crée une grille y avec des intervalles de 20
ax.axis('off')
ax.grid(True)  # Affiche la grille
plt.show()