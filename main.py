import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import random as rd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix
from CTkMessagebox import CTkMessagebox
import time

# ---------------------------------------------------------------------------- #
#                                  Constantes                                  #
# ---------------------------------------------------------------------------- #
TAILLE_POPULATION = 100
CHANCE_MUTATION = 0.01  # 10%
PERCENT_GOOD_INDIVIDU = 0.4  # Pourcentage d'individus ayant les meilleurs scores pris pour la prochaine génération
PERCENT_BAD_INDIVIDU = 0.05  # Pourcentage d'indivudus ayant un score en dessous de la moyenne pour la prochaine génration
NBRE_MAX_GENERATION = 100
NBRE_GOOD_INDIVIDU = int(TAILLE_POPULATION * PERCENT_GOOD_INDIVIDU)
TAILLE_GRILLE_X = 2000
TAILLE_GRILLE_Y = 2000
# --------------------------- DataFrame des villes --------------------------- #
ville_df = pd.DataFrame(columns=["Nom", "x", "y"])
dist_matrix = None  # Ajout d'une variable globale pour la matrice de distance

# ---------------------------------------------------------------------------- #
#                               Fonctions utiles                               #
# ---------------------------------------------------------------------------- #
def getX (ville):
    return ville_df.loc[ville_df["Nom"] == ville, "x"].values[0]

def getY (ville):
    return ville_df.loc[ville_df["Nom"] == ville, "y"].values[0]
# ----------------------- Creation ville aléatoirement ----------------------- #
def verifier(entry_widget):
    if not entry_widget.get():
        CTkMessagebox(title="Error", message="Le champs 'Nom de ville' est vide", icon="cancel")
        return False
    return True

def add_city(entry_widget, axes, canvas, nom=None):
    global dist_matrix  # Utilisation de la variable globale
    global ville_df
    
    if nom is None:
        nom_ville = "Ville " + str(len(ville_df)+1)
        new_ville = pd.DataFrame(
            {"Nom": nom_ville, 
             "x": rd.randrange(0, TAILLE_GRILLE_X), 
             "y": rd.randrange(0, TAILLE_GRILLE_Y)
            }, index = [0])
    else:
        if not verifier(entry_widget):  # Vérifie si le champ d'entrée n'est pas vide
            return
        nom_ville = entry_widget.get()
        new_ville = pd.DataFrame({
            "Nom": nom_ville, 
            "x": rd.randrange(0, TAILLE_GRILLE_X), 
            "y": rd.randrange(0, TAILLE_GRILLE_Y)
            }, index = [0])
    ville_df = pd.concat([ville_df, new_ville], ignore_index=True)
    # Mise à jour de la matrice de distance chaque fois qu'une nouvelle ville est ajoutée
    coords = ville_df[['x', 'y']].to_numpy()
    dist_matrix = pd.DataFrame(distance_matrix(coords, coords), index=ville_df["Nom"], columns=ville_df["Nom"])
    # Plot the new city on the graph
    axes.clear()
    axes.set_title("Carte des Villes")  # Set the title
    axes.set_xlabel("Coordonnées X")  # Set the x-axis label
    axes.set_ylabel("Coordonnées Y")  # Set the y-axis label
    axes.set_xlim(0, TAILLE_GRILLE_X)  # Set the x-axis limits
    axes.set_ylim(0, TAILLE_GRILLE_Y)  # Set the y-axis limits
    for i, row in ville_df.iterrows():
        axes.scatter(row['x'], row['y'])
        axes.text(row['x'], row['y'], row['Nom'], fontsize=12)
    canvas.draw()

# ------------------------ Suppression d'une ville ------------------------ #
def remove_last_city(axes, canvas):
    global dist_matrix  # Utilisation de la variable globale
    global ville_df
    if not ville_df.empty:  # Check if ville_df is not empty
        ville_df = ville_df.iloc[:-1]  # Remove the last row from ville_df
        # Mise à jour de la matrice de distance chaque fois qu'une ville est supprimée
        coords = ville_df[['x', 'y']].to_numpy()
        dist_matrix = pd.DataFrame(distance_matrix(coords, coords), index=ville_df["Nom"], columns=ville_df["Nom"])
        # Update the graph
        axes.clear()
        axes.set_title("Carte des Villes")  # Set the title
        axes.set_xlabel("Coordonnées X")  # Set the x-axis label
        axes.set_ylabel("Coordonnées Y")  # Set the y-axis label
        axes.set_xlim(0, TAILLE_GRILLE_X)  # Set the x-axis limits
        axes.set_ylim(0, TAILLE_GRILLE_Y)  # Set the y-axis limits
        for i, row in ville_df.iterrows():
            axes.scatter(row['x'], row['y'], color=row['color'])
            axes.text(row['x'], row['y'], row['Nom'], fontsize=12)
        canvas.draw()

# ------------------------ Distance entre deux villes ------------------------ #
def getDistance(nomVille1, nomVille2):
    global dist_matrix  # Utilisation de la variable globale
    return dist_matrix[nomVille1][nomVille2]

# --------------------------- Creation un individu --------------------------- #
def getIndividus():
    rand = ville_df.sample(frac=1).reset_index(drop=True)
    # ------------------------ Ajout ville depart a la fin ----------------------- #
    first_row = rand.iloc[[0]]
    rand = pd.concat([rand, first_row], ignore_index=True)
    distances = []
    for i in range(len(rand) - 1):
        distance = getDistance(rand.loc[i, 'Nom'], rand.loc[i + 1, 'Nom'])
        distances.append(distance)
    villes = ", ".join(rand["Nom"])
    score = sum(distances)
    return {"Villes": villes, "Score": score}


# ------------------------- Creation d'une population ------------------------ #
def getPopulation(taille_population):
    population_df = pd.DataFrame([], columns=["Villes", "Score"])
    for _ in range(taille_population):
        dict_individu = getIndividus()
        while dict_individu["Villes"] in population_df["Villes"].values:
            dict_individu = getIndividus()
        individu = pd.DataFrame(dict_individu, index = [0])
        population_df = pd.concat([population_df, individu], ignore_index=True)
    return population_df

# --------------------------- Creation des enfants --------------------------- #
def getEnfants(parent1, parent2):
    # *Recuperation ville venant du dataFrame
    liste_ville1 = parent1["Villes"]
    liste_ville2 = parent2["Villes"]
    # ---------------------------------------------------------------------------- #
    # *Creation d'un tableau contenant les villes
    liste_ville1 = liste_ville1.split(", ")
    liste_ville2 = liste_ville2.split(", ")
    # ---------------------------------------------------------------------------- #
    # *Creation de la premiere partie des enfants
    enfant1 = liste_ville1[:int(len(liste_ville1)/2)]
    enfant2 = liste_ville2[:int(len(liste_ville2)/2)]
    # ---------------------------------------------------------------------------- #
    # *Ajout de la seconde partie en partant de la fin de la liste des villes
    for i in range (len(liste_ville2)-1, -1, -1):
        if liste_ville2[i] not in enfant1:
            enfant1.append(liste_ville2[i])
    enfant1.append(enfant1[0])
    for i in range (len(liste_ville1)-1, -1, -1):
        if liste_ville1[i] not in enfant2:
            enfant2.append(liste_ville1[i])
    enfant2.append(enfant2[0])
    # ---------------------------------------------------------------------------- #
    # * Calcul Score des enfants
    distances = []
    for i in range(len(enfant1) - 1):
        distance = getDistance(enfant1[i], enfant1[i+1])
        distances.append(distance)
    enfant1 = {"Villes" : ", ".join(enfant1), "Score" : sum(distances)}
    distances = []
    for i in range(len(enfant2) - 1):
        distance = getDistance(enfant2[i], enfant2[i+1])
        distances.append(distance)
    enfant2 = {"Villes" : ", ".join(enfant2), "Score" : sum(distances)}
    enfants_df = pd.DataFrame([enfant1, enfant2])
    return enfants_df

# --------------------------------- Mutation --------------------------------- #
def mutate (individu):
    liste_ville = individu["Villes"]
    liste_ville = liste_ville.split(", ")
    i = rd.randint(0, len(liste_ville)-2)
    j = rd.randint(0, len(liste_ville)-2)
    while (j == i):
        j = rd.randint(0,len(liste_ville)-2)
    tempo = liste_ville[i]
    liste_ville[i] = liste_ville[j]
    liste_ville[j] = tempo
    liste_ville.pop(-1)
    liste_ville.append(liste_ville[0])
    distances = []
    for i in range(len(liste_ville) - 1):
        distance = getDistance(liste_ville[i], liste_ville[i+1])
        distances.append(distance)
    new_individu = {"Villes" : ", ".join(liste_ville), "Score" : sum(distances)}
    return pd.DataFrame([new_individu])

# ---------------------------------------------------------------------------- #
#                               Partie Graphique                               #
# ---------------------------------------------------------------------------- #

def plot_valeur(valeur_df, canvas, ax):
    ax.clear()  # Efface l'ancien graphique
    ax.plot(valeur_df["Generation"], valeur_df["Min"], label='Min')
    ax.plot(valeur_df["Generation"], valeur_df["Moy"], label='Moy')
    ax.legend(loc='upper right')
    ax.set_title("Evolution des valeurs")
    ax.set_xlabel("Génération")
    ax.set_ylabel("Valeur")
    canvas.draw()

def plot_chemin(best_individu, generation, axes, canvas):
    list_ville = best_individu["Villes"].split(", ")
    axes.clear()
    for i in range(len(list_ville)-1):
        if i == 0:
            axes.scatter(getX(list_ville[i]), getY(list_ville[i]), color='green')
            axes.annotate(list_ville[i], (getX(list_ville[i]), getY(list_ville[i])))
        else:
            axes.scatter(getX(list_ville[i]), getY(list_ville[i]), color='blue')
            axes.annotate(list_ville[i], (getX(list_ville[i]), getY(list_ville[i])))
    for i in range(len(list_ville) - 1):
        x1 = getX(list_ville[i])
        y1 = getY(list_ville[i])
        x2 = getX(list_ville[i+1])
        y2 = getY(list_ville[i+1])
        axes.plot([x1, x2], [y1, y2], color='blue', label = "Score: " + str(best_individu["Score"]))
     # Efface l'ancien graphique
    axes.set_title("Meilleur chemin trouvé à la génération " + str(generation))
    axes.set_xlabel("Coordonnées X")
    axes.set_ylabel("Coordonnées Y")
    axes.set_xlim(0, TAILLE_GRILLE_X)
    axes.set_ylim(0, TAILLE_GRILLE_Y)
    # axes.legend(loc='upper right')
    canvas.draw()
# ---------------------------------------------------------------------------- #
#                             Algorithme Génétique                             #
# ---------------------------------------------------------------------------- #
def algo_genetique (taille_pop, chance_mutation, nbre_generation, percent_good_individu, percent_bad_individu, canvas, axes, root, canvas2, axes2):
    i = 0
    NBRE_GOOD_INDIVIDU = int(taille_pop * percent_good_individu)
    pop = getPopulation(taille_pop)
    valeur_df = pd.DataFrame(columns=["Generation", "Min", "Moy"])
    while i < nbre_generation:
        new_valeur = {"Generation": i, "Min": pop["Score"].min(), "Moy": pop["Score"].mean()}
        valeur_df = pd.concat([valeur_df, pd.DataFrame([new_valeur], index = [0])], ignore_index=True)
        # -------------------- Classe parents par score croissant -------------------- #
        pop_trie = pop.sort_values(by = "Score").reset_index(drop=True)
        plot_chemin(pop_trie.iloc[0], i, axes, canvas)
        plot_valeur(valeur_df, canvas2, axes2)
        root.update()
        new_pop = pd.DataFrame(columns = ["Villes", "Score"])
        # ---------------------- On selectionne les bon parents ---------------------- #
        new_pop = pop_trie[:NBRE_GOOD_INDIVIDU]
        # ---------------- On ajoute possiblement des mauvais parents ---------------- #
        for j in range(NBRE_GOOD_INDIVIDU, len(pop_trie)):
            rand = rd.random()
            if rand <= percent_bad_individu:
                bad_individu = pop_trie.iloc[[j]]
                new_pop = pd.concat([new_pop, bad_individu], ignore_index= True)
        # --------------------------- Creation des enfants --------------------------- #
        while len(new_pop) < taille_pop:
            parents = new_pop.sample(n=2).reset_index(drop=True)
            enfants = getEnfants(parent1= parents.iloc[0], parent2= parents.iloc[1])
            if taille_pop - len(new_pop) >= 2:
                new_pop = pd.concat([new_pop, enfants], ignore_index=True)
            else:
                rand = rd.randint(0,1)
                enfant = pop_trie.iloc[[rand]]
                new_pop = pd.concat([new_pop, enfant], ignore_index=True)
        # --------------------------------- Mutations -------------------------------- #
        for k in range(len(new_pop)):
            rand = rd.random()
            if rand <= chance_mutation:
                indivudu = new_pop.iloc[k]
                new_pop = new_pop.drop(k).reset_index(drop=True)
                new_individu = mutate(indivudu)
                new_pop = pd.concat([new_pop, new_individu], ignore_index=True)
        # -------------- Recursivité pour generer la nouvelle population ------------- #
        i = i + 1
        pop = new_pop
        time.sleep(0.05)
    new_pop = pop.sort_values(by = "Score").reset_index(drop=True)
    return new_pop, valeur_df