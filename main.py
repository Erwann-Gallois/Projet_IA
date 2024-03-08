import numpy as np
import random as rd
import matplotlib.pyplot as plt
from city import City
from chemin import Chemin

taille_x = 1500

taille_y = 1500

nbre_ville = 10

nbre_parents = 2

nbre_generation = 100

score_seuil = 50

mutation_rate = 0.01


cities = []
# Creer des villes aleatoires
for i in range(nbre_ville):
    city = City("Ville " + str(i+1), rd.randrange(0, taille_x), rd.randrange(0, taille_y))
    cities.append(city)

# Generations des parents
def getParent(n, cities):
    parents = [[None for _ in range(0, len(cities)-1)] for _ in range(0, n)]
    for i in range(n):
        # print("Parent " + str(i) + ":" )
        rd.shuffle(cities)
        for j in range(len(cities)-1):
            parents[i][j] = (Chemin(cities[j], cities[j+1]))
    return parents
def afficheParentListe(parents):
    for ligne in parents:
        print("Parent " + str(ligne) + ":" )
        for j in ligne:
            print(j.toString())
            
def getEnfants(parent1, parent2):
    enfant1 = [len(parent1)]
    enfant2 = [len(parent2)]
    demi_taille1 = int(len(parent1)/2)
    demi_taille2 = int(len(parent2)/2)
    enfant1[0:demi_taille1] = parent1[0:demi_taille1]
    enfant2[0:demi_taille2] = parent2[0:demi_taille2]
    enfant1[demi_taille1:len(enfant2)] = parent1[demi_taille1:len(parent1)]
    enfant2[demi_taille2:len(enfant2)] = parent2[demi_taille2:len(parent2)]
    return enfant1, enfant2

def afficheParentsGraph(parents):
    for i in range(len(parents)):
        # Créer une nouvelle figure pour chaque parent
        fig, ax = plt.subplots()
        color = np.random.rand(3,)
        # Parcourir toutes les villes
        for city in cities:
            # Créer un point pour chaque ville avec une couleur aléatoire
            ax.scatter(city.x, city.y, color= "red")
            ax.text(city.x, city.y, city.name) # Affiche le nom de la ville

        # Parcourir toutes les villes du parent actuel
        for j in range(nbre_ville - 1):
            # Afficher le chemin pour chaque ville du parent
            ax.plot([parents[i][j].depart.x, parents[i][j].arrivee.x], [parents[i][j].depart.y, parents[i][j].arrivee.y],
                    color= color , linestyle='dotted')

        # Modifier les paramètres de l'axe
        ax.set_xticks([])  # Supprimer les marques sur l'axe x
        ax.set_yticks([])  # Supprimer les marques sur l'axe y
        ax.axis('off')  # Supprimer les axes
        ax.grid(True)  # Afficher la grille

        # Afficher la figure pour le parent actuel
        plt.title("Parent " + str(i))  # Ajouter un titre

    plt.tight_layout()  # Ajuster la disposition des subplots
    plt.show()
parents = getParent(nbre_parents, cities)
afficheParentListe(parents)
enf1, enf2 = getEnfants(parents[0], parents[1])
print("Enfant 1\n")
for enf in enf1:
    print(enf.toString())

print("Enfant 2\n")
for enf in enf2:
    print(enf.toString())
    # print(enfa.toString())
# print(enfants)
