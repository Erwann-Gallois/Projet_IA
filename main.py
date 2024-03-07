import numpy as np
import random as rd
import matplotlib.pyplot as plt
from city import City
from chemin import Chemin

taille_x = 500
taille_y = 500
nbre_ville = 5
nbre_parents = 2
nbre_generation = 100
score_seuil = 50
mutation_rate = 0.01
cities = []
# Creer des villes aleatoires
for i in range(nbre_ville):
    city = City("Ville " + str(i+1), rd.randrange(0, taille_x), rd.randrange(0, taille_y))
    cities.append(city)

# Creation des chemins (Toutes les villes sont connectées)
# chemins = []
# for i in range(nbre_ville - 1):
#     for j in range (i, len(cities)):
#         if (cities[i] != cities[j]):
#             chemins.append(Chemin(cities[i], cities[j]))

# Generations des parents
parents = []
for i in range (0, nbre_parents):
    rd.shuffle(cities)
    for j in range(0, (len(cities)-1)):
        parents[i] = (Chemin(cities[j], cities[j+1]))

for parent in parents:
    print (parent.toString())
        

# Afficher les villes sur une grille
fig, ax = plt.subplots()
for city in cities:
    # Creer un point pour chaque ville avec une couleur aleatoire
    ax.scatter(city.x, city.y, color=np.random.rand(3,))
    ax.text(city.x, city.y, city.name) # Affiche le nom de la ville

# Creer un chemin entre chaque ville
# for chemin in chemins:
#     ax.plot([chemin.depart.x, chemin.arrivee.x], [chemin.depart.y, chemin.arrivee.y], color=np.random.rand(3,), label = "{:.2f}".format(chemin.score))

ax.legend(loc='best') # Affiche la légende en haut à droite
ax.set_xticks([])  # Crée une grille x avec des intervalles de 20
ax.set_yticks([])  # Crée une grille y avec des intervalles de 20
ax.axis('off')
ax.grid(True)  # Affiche la grille

plt.show()