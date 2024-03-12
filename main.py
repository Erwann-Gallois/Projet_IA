import numpy as np
import random as rd
import matplotlib.pyplot as plt
from city import City

# -------------------------------------------------------------
# Definition des constantes
# -------------------------------------------------------------
taille_x = 1500

taille_y = 1500

nbre_ville = 6

nbre_parents = 2

nbre_generation = 100

score_seuil = 50

mutation_rate = 0.01


cities = []

# -------------------------------------------------------------
# Creer des villes aleatoires
# -------------------------------------------------------------
for i in range(nbre_ville):
    cities.append(City(str(i+1), rd.randrange(0, taille_x), rd.randrange(0, taille_y)))

# -------------------------------------------------------------
# Generations des parents
# -------------------------------------------------------------
def getParent(n, cities):
    parents = [[None for _ in range(0, len(cities)+1)] for _ in range(0, n)]
    for i in range(n):
        # print("Parent " + str(i) + ":" )
        rd.shuffle(cities)
        for j in range(len(cities)):
            parents[i][j] = (cities[j])
        parents[i][-1] = parents[i][0]
    return parents

# -------------------------------------------------------------
# Generation de l'enfant a partie de deux parents
# -------------------------------------------------------------
def getEnfant(parent1, parent2):
    enfant = []
    demi_taille = int((len(parent1)-1)/2)
    enfant[0:demi_taille-1] = parent1[0:demi_taille-1]
    while (len(enfant) < nbre_ville):
        for i in range(0, len(parent2)):
            if parent2[i] not in enfant:
                enfant.append(parent2[i])
    enfant.append(enfant[0])
    return enfant
# -------------------------------------------------------------
# Fonction qui affiche la liste des villes (un chemin) pour les parents
# -------------------------------------------------------------
def afficheParentsListe(parents):
    for index_ligne, ligne in enumerate(parents):
        print("Parent " + str(index_ligne) + ":" )
        for j in ligne:
            print(j.toString())
# -------------------------------------------------------------
# Fonction qui affiche la liste des villes (un chemin) pour les enfants
# -------------------------------------------------------------            
def afficheEnfantsListe(enfants):
    print("Enfant")
    for ligne in enfants:
        print (ligne.toString())

# -------------------------------------------------------------
# Fonction qui affiche le graph du chemin pour les parents
# -------------------------------------------------------------
def afficheParentsGraph(parents):
    for i in range(len(parents)):
        # Créer une nouvelle figure pour chaque parent
        fig, ax = plt.subplots()
        color = ["blue", "red"]
        # Parcourir toutes les villes
        for city in cities:
            # Créer un point pour chaque ville avec une couleur aléatoire
            ax.scatter(city.x, city.y, color= "red")
            ax.text(city.x, city.y, city.name) # Affiche le nom de la ville

        # Parcourir toutes les villes du parent actuel
        for j in range(0, len(parents[i])-1):
            print(parents[i][j+1].toString())
            # Afficher le chemin pour chaque ville du parent
            ax.plot([parents[i][j].x, parents[i][j+1].x], [parents[i][j].y, parents[i][j+1].y],color= color[i] , linestyle='dotted')
        # Modifier les paramètres de l'axe
        ax.set_xticks([])  # Supprimer les marques sur l'axe x
        ax.set_yticks([])  # Supprimer les marques sur l'axe y
        ax.axis('off')  # Supprimer les axes
        ax.grid(True)  # Afficher la grille

        # Afficher la figure pour le parent actuel
        plt.title("Parent " + str(i))  # Ajouter un titre
# -------------------------------------------------------------
# Fonction qui affiche le graph du chemin pour les enfants
# -------------------------------------------------------------
def afficheEnfantsGraph(enfants):
    # Créer une nouvelle figure pour chaque parent
    fig, ax = plt.subplots()
    color = np.random.rand(3,)
    # Parcourir toutes les villes
    for city in cities:
        # Créer un point pour chaque ville avec une couleur aléatoire
        ax.scatter(city.x, city.y, color= "red")
        ax.text(city.x, city.y, city.name) # Affiche le nom de la ville

    # Parcourir toutes les villes du parent actuel
    for j in range(0, len(enfants)-1):
        # Afficher le chemin pour chaque ville du parent
        ax.plot([enfants[j].x, enfants[j+1].x], [enfants[j].y, enfants[j+1].y],color= color , linestyle='dotted')

    # Modifier les paramètres de l'axe
    ax.set_xticks([])  # Supprimer les marques sur l'axe x
    ax.set_yticks([])  # Supprimer les marques sur l'axe y
    ax.axis('off')  # Supprimer les axes
    ax.grid(True)  # Afficher la grille

    # Afficher la figure pour le parent actuel
    plt.title("Enfant")  # Ajouter un titre

def afficheGraph():
    plt.tight_layout()  # Ajuster la disposition des subplots
    plt.show()

parents = getParent(nbre_parents, cities)
enfants = getEnfant(parents[0], parents[1])
afficheParentsGraph(parents)
afficheEnfantsGraph(enfants)
afficheGraph()
