import numpy as np
import random as rd
import matplotlib.pyplot as plt
from city import City

taille_x = 1500

taille_y = 1500

nbre_ville = 6

nbre_parents = 2

nbre_generation = 100

score_seuil = 50

mutation_rate = 0.01


cities = []

# Creer des villes aleatoires
for i in range(nbre_ville):
    cities.append(City(str(i+1), rd.randrange(0, taille_x), rd.randrange(0, taille_y)))

# Generations des parents
def getParent(n, cities):
    parents = [[None for _ in range(0, len(cities)+1)] for _ in range(0, n)]
    for i in range(n):
        # print("Parent " + str(i) + ":" )
        rd.shuffle(cities)
        for j in range(len(cities)):
            parents[i][j] = (cities[j])
        parents[i][-1] = parents[i][0]
    return parents
def getEnfants(parent1, parent2):
    enfant1 = [None for _ in range(len(parent1))]
    enfant2 = [None for _ in range(len(parent2))]
    demi_taille1 = int(len(parent1)/2)
    demi_taille2 = int(len(parent2)/2)
    enfant1[0:demi_taille1] = parent1[0:demi_taille1]
    enfant2[0:demi_taille2] = parent2[0:demi_taille2]
    for i in range(demi_taille1, len(parent1)):
        if parent1[i] not in enfant1:
            enfant1[i] = parent2
    
    enfants = [enfant1, enfant2]
    return enfants

def afficheParentsListe(parents):
    for index_ligne, ligne in enumerate(parents):
        print("Parent " + str(index_ligne) + ":" )
        for j in ligne:
            print(j.toString())
            
def afficheEnfantsListe(enfants):
    for index_ligne, ligne in enumerate(enfants):
        print("Enfant " + str(index_ligne) + ":" )
        for j in ligne:
            print(j.toString())

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
        for j in range(len(parents[i])):
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

def afficheEnfantsGraph(enfants):
    for i in range(len(enfants)):
        # Créer une nouvelle figure pour chaque parent
        fig, ax = plt.subplots()
        color = np.random.rand(3,)
        # Parcourir toutes les villes
        for city in cities:
            # Créer un point pour chaque ville avec une couleur aléatoire
            ax.scatter(city.x, city.y, color= "red")
            ax.text(city.x, city.y, city.name) # Affiche le nom de la ville

        # Parcourir toutes les villes du parent actuel
        for j in range(len(enfants[i])):
            # Afficher le chemin pour chaque ville du parent
            ax.plot([enfants[i][j].depart.x, enfants[i][j].arrivee.x], [enfants[i][j].depart.y, enfants[i][j].arrivee.y],color= color , linestyle='dotted')

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
print(parents)
enfants = getEnfants(parents[0], parents[1])
afficheParentsListe(parents)
afficheEnfantsListe(enfants)