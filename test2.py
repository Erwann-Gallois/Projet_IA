import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
import numpy as np
import main as main
import pandas as pd
import random as rd

# generate root
root = ctk.CTk()
root.title("Shortest Path")
root.geometry("1200x800")
root.resizable(0, 0)

# ---------------------------- Création des frames --------------------------- #
var = ctk.CTkFrame(master=root)  # Frame à droite
graph = ctk.CTkFrame(master=root)  # Frame pour le graphique
city = ctk.CTkFrame(master = root)  # Frame en haut à gauche

# --------------------------- Placement des frames --------------------------- #
var.grid(row=0, column=7, rowspan=10, columnspan=3, sticky="nsew")  # Frame à droite prend 5 colonnes et toutes les lignes
graph.grid(row=3, column=0, rowspan=7, columnspan=7, sticky="nsew")  # Frame pour le graphique prend 5 colonnes et 7 lignes
city.grid(row=0, column=0, rowspan=3, columnspan=7, sticky="nsew")  # Frame en haut à gauche prend 5 colonnes et 3 lignes

# Redimensionnement des lignes et colonnes pour que les frames s'adaptent à la taille de la fenêtre
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
for i in range(10):
    root.grid_columnconfigure(i, weight=1)

# Redimensionnement des lignes et colonnes pour que les frames s'adaptent à la taille de la fenêtre
for i in range(10):
    var.grid_rowconfigure(i, weight=1)
for i in range(4):
    var.grid_columnconfigure(i, weight=1)

for i in range(2):
    city.grid_rowconfigure(i, weight=1)
for i in range(4):
    city.grid_columnconfigure(i, weight=1)
# ------------------------------- Partie graph ------------------------------- #
fig, ax = plt.subplots(figsize=(10, 5))
# ------------------------------ Partie variable ----------------------------- #

# label = ctk.CTkLabel(text="Colonne 0", font=("Arial", 20), master = var)
# label.grid(row=0, column=0, sticky="nsew")

# label21 = ctk.CTkLabel(text="Colonne 1", font=("Arial", 20), master = var)
# label21.grid(row=0, column=1, sticky="nsew")

# label22 = ctk.CTkLabel(text="Colonne 2", font=("Arial", 20), master = var)
# label22.grid(row=0, column=2, sticky="nsew")

# label23 = ctk.CTkLabel(text="Colonne 3", font=("Arial", 20), master = var)
# label23.grid(row=0, column=3, sticky="nsew")
# -------------------------------- Label Title ------------------------------- #
label1 = ctk.CTkLabel(text="Variables", font=("Arial", 24), master = var)
label1.grid(row=0, column=0, columnspan=4)

# ----------------------------- Taille Population ---------------------------- #
label2 = ctk.CTkLabel(text="Taille de la population: ", master = var, font = ("Arial", 16))
entry2 = ctk.CTkEntry(master = var)
label2.grid(row=1, column=0, columnspan=2)
entry2.grid(row=1, column=2, columnspan=2, sticky="w")

# ------------------------------ Chance Mutation ----------------------------- #
label3 = ctk.CTkLabel(text="Chance de mutation: ", master = var, font = ("Arial", 16))
entry3 = ctk.CTkEntry(master = var)
label3.grid(row=2, column=0, columnspan=2)
entry3.grid(row=2, column=2, columnspan=2, sticky="w")

# ----------------------------- Nombre Generation ---------------------------- #
label4 = ctk.CTkLabel(text="Nbre de generation: ", master = var, font = ("Arial", 16))
entry4 = ctk.CTkEntry(master = var)
label4.grid(row=3, column=0, columnspan=2)
entry4.grid(row=3, column=2, columnspan=2, sticky="w")

# ------------------------- Pourcentage bon individu ------------------------- #
label5 = ctk.CTkLabel(text="% bon individu: ", master = var, font = ("Arial", 16))
entry5 = ctk.CTkEntry(master = var)
label5.grid(row=4, column=0, columnspan=2)
entry5.grid(row=4, column=2, columnspan=2, sticky = "w")

# ----------------------- Pourcentage mauvais individu ----------------------- #
label6 = ctk.CTkLabel(text="% mauvais individu: ", master = var, font = ("Arial", 16))
entry6 = ctk.CTkEntry(master = var)
label6.grid(row=5, column=0, columnspan=2)
entry6.grid(row=5, column=2, columnspan=2, sticky = "w")

# ----------------------- Pourcentage mauvais individu ----------------------- #
label9 = ctk.CTkLabel(text="Meilleur Score: ", master = var, font = ("Arial", 16))
label9.grid(row=6, column=0, columnspan=2)
label10 = ctk.CTkLabel(text="0", master = var)
label10.grid(row=6, column=2, columnspan=2,  sticky = "w")

# ------------------------------ Bouton Start ------------------------------- #

button = ctk.CTkButton(master = var, text="Start", font=("Arial", 34))
button.grid(row=7, column=1,columnspan = 2, rowspan = 3, sticky="w")

# ------------------------------- Partie ville ------------------------------- #
# -------------------------------- Label Title ------------------------------- #
label7 = ctk.CTkLabel(text="Problème du voyageur de commerce", font=("Arial", 24), master = city)
label7.grid(row=0, column=0, columnspan=5)

button = ctk.CTkButton(master = city, text="Ville Aléatoire")
button.grid(row=1, column=4)

label8 = ctk.CTkLabel(text="Nom de la ville: ", master = city)
entry8 = ctk.CTkEntry(master = city)
label8.grid(row=1, column=1)
entry8.grid(row=1, column=2)

button = ctk.CTkButton(master = city, text="Ajouter")
button.grid(row=1, column=3)

def plot_valeur(valeur_df, fig, ax):
    ax.cla()  # Efface l'ancien graphique
    ax.plot(valeur_df["Generation"], valeur_df["Min"], label='Min')
    ax.plot(valeur_df["Generation"], valeur_df["Moy"], label='Moy')
    ax.legend(loc='upper right')
    plt.title("Evolution des valeurs")
    plt.xlabel("Generation")
    plt.ylabel("Valeur")
    plt.grid()
    plt.tight_layout()
    update_graph()

def update_graph():
    global valeur_df
    plot_valeur(valeur_df, fig, ax)
    canvas.draw()
    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().pack(fill='both', expand=True)

def algo_genetique (pop):
    i = 0
    global valeur_df 
    valeur_df = pd.DataFrame(columns=["Generation", "Min", "Moy"])
    while i < 10:
        new_valeur = {"Generation": i, "Min": pop["Score"].min(), "Moy": pop["Score"].mean()}
        valeur_df = pd.concat([valeur_df, pd.DataFrame([new_valeur], index = [0])], ignore_index=True)
        plot_valeur(valeur_df, fig, ax)
        # -------------------- Classe parents par score croissant -------------------- #
        pop_trie = pop.sort_values(by = "Score").reset_index(drop=True)
        new_pop = pd.DataFrame(columns = ["Villes", "Score"])
        # ---------------------- On selectionne les bon parents ---------------------- #
        new_pop = pop_trie[:40]
        # ---------------- On ajoute possiblement des mauvais parents ---------------- #
        for j in range(40, len(pop_trie)):
            rand = rd.random()
            if rand <= 0.01:
                bad_individu = pop_trie.iloc[[j]]
                new_pop = pd.concat([new_pop, bad_individu], ignore_index= True)
        # --------------------------- Creation des enfants --------------------------- #
        while len(new_pop) < 10:
            parents = new_pop.sample(n=2).reset_index(drop=True)
            enfants = main.getEnfants(parent1= parents.iloc[0], parent2= parents.iloc[1])
            if 10 - len(new_pop) >= 2:
                new_pop = pd.concat([new_pop, enfants], ignore_index=True)
            else:
                rand = rd.randint(0,1)
                enfant = pop_trie.iloc[[rand]]
                new_pop = pd.concat([new_pop, enfant], ignore_index=True)
        # --------------------------------- Mutations -------------------------------- #
        for k in range(len(new_pop)):
            rand = rd.random()
            if rand <=0.01:
                indivudu = new_pop.iloc[k]
                new_pop = new_pop.drop(k).reset_index(drop=True)
                new_individu = main.mutate(indivudu)
                new_pop = pd.concat([new_pop, new_individu], ignore_index=True)
        # -------------- Recursivité pour generer la nouvelle population ------------- #
        i = i + 1
        pop = new_pop
    new_pop = pop.sort_values(by = "Score").reset_index(drop=True)
    return new_pop, valeur_df
root.mainloop()
root.after(1, algo_genetique(main.getPopulation()))