import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import random as rd
import pandas as pd
import numpy as np

# --------------------------- DataFrame des villes --------------------------- #
ville_df = pd.DataFrame(columns=["Nom", "x", "y"])

# --------------------------- DataFrame des chemins -------------------------- #

# ---------------------------------------------------------------------------- #
#                                  Constantes                                  #
# ---------------------------------------------------------------------------- #
TAILLE_POPULATION = 10
CHANCE_MUTATION = 0.1  # 10%
PERCENT_GOOD_INDIVIDU = 0.4  # Pourcentage d'individus ayant les meilleurs scores pris pour la prochaine génération
PERCENT_BAD_INDIVIDU = 0.05  # Pourcentage d'indivudus ayant un score en dessous de la moyenne pour la prochaine génration
NBRE_MAX_GENERATION = 100
NBRE_GOOF_INDIVIDU = int(TAILLE_POPULATION * PERCENT_GOOD_INDIVIDU)
TAILLE_GRILLE_X = 200
TAILLE_GRILLE_Y = 200
NBRE_VILLE = 10

# ----------------------- Creation ville aléatoirement ----------------------- #
for i in range(NBRE_VILLE):
    new_ville = pd.DataFrame({"Nom": ["Ville " + str(i)], "x": [rd.randrange(0, TAILLE_GRILLE_X)], "y": [rd.randrange(0, TAILLE_GRILLE_Y)]})
    ville_df = pd.concat([ville_df, new_ville], ignore_index=True)

# ------------------------ Distance entre deux villes ------------------------ #
def getDistance(nomVille1, nomVille2):
    x1 = ville_df.loc[ville_df["Nom"] == nomVille1, 'x'].values[0]
    x2 = ville_df.loc[ville_df["Nom"] == nomVille2, 'x'].values[0]
    y1 = ville_df.loc[ville_df["Nom"] == nomVille1, 'y'].values[0]
    y2 = ville_df.loc[ville_df["Nom"] == nomVille2, 'y'].values[0]
    xDis = abs(x1 - x2)
    yDis = abs(y1 - y2)
    distance = np.sqrt((xDis ** 2) + (yDis ** 2))
    return distance

# --------------------------- Creation un individu --------------------------- #
def getIndividus():
    rand = ville_df.sample(frac=1).reset_index(drop=True)
    distances = []
    for i in range(len(rand) - 1):
        distance = getDistance(rand.loc[i, 'Nom'], rand.loc[i + 1, 'Nom'])
        distances.append(distance)
    villes = ", ".join(rand["Nom"])
    score = sum(distances)
    return {"Villes": villes, "Score": score}


# ------------------------- Creation d'une population ------------------------ #
def getPopulation():
    population_df = pd.DataFrame([], columns=["Villes", "Score"])
    for _ in range(TAILLE_POPULATION):
        dict_individu = getIndividus()
        individu = pd.DataFrame(dict_individu, index = [0])
        population_df = pd.concat([population_df, individu], ignore_index=True)
    return population_df

# --------------------------- Creation des enfants --------------------------- #
def getEnfants(parent1, parent2):
    liste_ville1 = parent1["Villes"]
    liste_ville2 = parent2["Villes"]
    liste_ville1 = liste_ville1.split(", ")
    liste_ville2 = liste_ville2.split(", ")
    enfant1 = liste_ville1[:int(len(liste_ville1)/2)]
    enfant2 = liste_ville2[:int(len(liste_ville2)/2)]
    for i in range (len(liste_ville2)-1, -1, -1):
        if liste_ville2[i] not in enfant1:
            enfant1.append(liste_ville2[i])
    for i in range (len(liste_ville1)-1, -1, -1):
        if liste_ville1[i] not in enfant2:
            enfant2.append(liste_ville1[i])
    

pop = getPopulation()
print(pop)
getEnfants(pop.iloc[0], pop.iloc[1])
