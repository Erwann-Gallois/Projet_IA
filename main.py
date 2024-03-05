import numpy as np
import matplotlib.pyplot as plt
from city import City
from chemin import Chemin

taille_x = 500
taille_y = 500
nbre_ville = 5
nbre_generation = 100
score_seuil = 50
mutation_rate = 0.01
cities = []
# Creer des villes aleatoires
for i in range(nbre_ville):
    city = City("Ville " + str(i+1), np.random.randint(0, taille_x), np.random.randint(0, taille_y))
    cities.append(city)

# Creer des chemins aleatoires
chemins = []
for i in range(nbre_ville - 1):
    chemin = Chemin(cities[i], cities[i+1])
    chemins.append(chemin)

# Assurez-vous que chaque ville a au moins un chemin en créant un chemin supplémentaire entre la dernière ville et la première ville
chemin = Chemin(cities[-1], cities[0])
chemins.append(chemin)

# Creer des chemins aleatoires entre chaque ville sans doublons
for i in range(nbre_ville - 1):
    depart = cities[np.random.randint(0, nbre_ville)]
    arrivee = cities[np.random.randint(0, nbre_ville)]
    if depart == arrivee:
        while depart == arrivee:
            arrivee = cities[np.random.randint(0, nbre_ville)]
    for chemin in chemins : 
        if (depart == chemin.depart and arrivee == chemin.arrivee) or (depart == chemin.arrivee and arrivee == chemin.depart):
            while (depart == chemin.depart and arrivee == chemin.arrivee) or (depart == chemin.arrivee and arrivee == chemin.depart):
                depart = cities[np.random.randint(0, nbre_ville)]
                arrivee = cities[np.random.randint(0, nbre_ville)]
                if depart == arrivee:
                    while depart == arrivee:
                        arrivee = cities[np.random.randint(0, nbre_ville)]
    chemin = Chemin(depart, arrivee)
    chemins.append(chemin) 

for chemin in chemins:
    print(chemin.toString())

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
    ax.plot([chemin.depart.x, chemin.arrivee.x], [chemin.depart.y, chemin.arrivee.y], color=np.random.rand(3,), label = str(chemin.score))

ax.legend(loc='upper right') # Affiche la légende en haut à droite
ax.set_xticks([])  # Crée une grille x avec des intervalles de 20
ax.set_yticks([])  # Crée une grille y avec des intervalles de 20
ax.axis('off')
ax.grid(True)  # Affiche la grille

plt.show()