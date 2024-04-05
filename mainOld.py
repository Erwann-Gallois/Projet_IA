import numpy as np
import random as rd
import matplotlib.pyplot as plt
from city import City
from voyage import Voyage
# -------------------------------------------------------------
# Definition des constantes
# -------------------------------------------------------------
taille_x = 200

taille_y = 200

nbre_ville = 6

nbre_parents = 2

nbre_generation = 10

mutation_rate = 10

# -------------------------------------------------------------
# Creer des villes aleatoires
# -------------------------------------------------------------
cities = []
for i in range(nbre_ville):
    cities.append(City(str(i+1), rd.randrange(0, taille_x), rd.randrange(0, taille_y)))

# -------------------------------------------------------------
# Generations des parents
# -------------------------------------------------------------
def getParent(cities):
    parent = [None for _ in range(0, len(cities)+1)]
    # print("Parent " + str(i) + ":" )
    rd.shuffle(cities)
    for j in range(len(cities)):
        parent[j] = (cities[j])
    parent[-1] = parent[0]
    parent = Voyage(parent)
    return parent

# -------------------------------------------------------------
# Generation de l'enfant a partie de deux parents
# -------------------------------------------------------------
def getEnfant(parent1, parent2):
    enfant1 = []
    enfant2 = []
    demi_taille = int((len(parent1.chemin)-1)/2)
    demi_taille2 = int((len(parent2.chemin)-1)/2)
    enfant1[0:demi_taille-1] = parent1.chemin[0:demi_taille-1]
    enfant2[0:demi_taille2-1] = parent2.chemin[0:demi_taille2-1]
    for i in range(demi_taille2, (len(parent2.chemin))):
        if parent2.chemin[i] not in enfant1:
            enfant1.append(parent2.chemin[i])
    while(len(enfant1) < nbre_ville):
        for i in range(0, nbre_ville):
            if cities[i] not in enfant1:
                enfant1.append(cities[i])
    enfant1.append(enfant1[0])
    for i in range(demi_taille2, (len(parent1.chemin))):
        if parent1.chemin[i] not in enfant2:
            enfant2.append(parent1.chemin[i])
    while(len(enfant2) < nbre_ville):
        for i in range(0, nbre_ville):
            if cities[i] not in enfant2:
                enfant1.append(cities[i])
    enfant2.append(enfant2[0])
    enfant1 = Voyage(enfant1)
    enfant2 = Voyage(enfant2)
    return enfant1, enfant2

# -------------------------------------------------------------
# Fonction qui creer le graph du chemin pour les parents
# -------------------------------------------------------------
def mutate(tab_ville):
    i = rd.randint(0, len(tab_ville))
    j = rd.randint(0, len(tab_ville))
    while (j == i):
        j = rd.randint(0,len(tab_ville))
    tempo = tab_ville[i]
    tab_ville[i] = tab_ville[j]
    tab_ville[j] = tempo
    return tab_ville

# -------------------------------------------------------------
# Fonction qui creer le graph du chemin pour les parents
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
            # print(parents[i][j+1].toString())
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
# Fonction qui creer le graph du chemin pour les enfants
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
        ax.plot([enfants[j].chemin.x, enfants[j+1].chemin.x], [enfants[j].chemin.y, enfants[j+1].chemin.y],color= color , linestyle='dotted')

    # Modifier les paramètres de l'axe
    ax.set_xticks([])  # Supprimer les marques sur l'axe x
    ax.set_yticks([])  # Supprimer les marques sur l'axe y
    ax.axis('off')  # Supprimer les axes
    ax.grid(True)  # Afficher la grille

    # Afficher la figure pour le parent actuel
    plt.title("Enfant")  # Ajouter un titre

# -------------------------------------------------------------
# Fonction qui affiche tout les graphs
# -------------------------------------------------------------
def afficheGraph():
    plt.tight_layout()  # Ajuster la disposition des subplots
    plt.show()

# -------------------------------------------------------------
# Fonction qui affiche tout les graphs
# -------------------------------------------------------------
def getScore (tab_citie):
    sum = 0
    for i in range(0, len(tab_citie) - 1):
        sum = sum + tab_citie[i].getDistance(tab_citie[i+1])
    return sum
# -------------------------------------------------------------
# Main
# -------------------------------------------------------------
def algo_genetique(parent1, parent2, i, nbre_generation):
    if i >= nbre_generation:
        if parent1.score < parent2.score:
            return parent1
        else:
            return parent2
    enfant1, enfant2 = getEnfant(parent1, parent2)
    # Mutation Possible pour l'enfant 1
    rand = rd.random()*100
    if (rand < mutation_rate):
        enfant1.chemin = mutate(enfant1.chemin)
    # Mutation Possible pour l'enfant 2
    rand = rd.random()*100
    if (rand < mutation_rate):
        enfant2.chemin = mutate(enfant2.chemin)
    # Crée une liste de parents et enfants, puis les trie par score
    famille = [parent1, parent2, enfant1, enfant2]
    famille.sort(key=lambda x: x.score)
    # Les deux individus avec les scores les plus bas deviennent les nouveaux parents
    nouveau_parent1, nouveau_parent2 = famille[:2]
    print("iteration" + str(i) + "\n")
    print("Min 1 :" + str(nouveau_parent1.score) + "\n")
    print("Min 2 :" + str(nouveau_parent2.score)+ "\n")

    return algo_genetique(nouveau_parent1, nouveau_parent2, i + 1, nbre_generation)

parent1_depart = getParent(cities)
parent2_depart = getParent(cities)

# best_paths = []
result = algo_genetique(parent1_depart, parent2_depart, 0, nbre_generation)

# Tracer les meilleurs chemins au fil des générations
# def plot_evolution(best_paths):
#     fig, ax = plt.subplots()
#     for path in best_paths:
#         x = [city.x for city in path.chemin]
#         y = [city.y for city in path.chemin]
#         ax.plot(x, y, marker='o', label=f'Generation {best_paths.index(path) + 1}')
#     ax.legend()
#     plt.title("Evolution des chemins au fil des generations")
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.show()

# plot_evolution(best_paths)
print("Resultat : \n" )
print(result.toString())

