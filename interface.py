import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import main as main
from CTkMessagebox import CTkMessagebox as ctkmsg


# generate root
root = ctk.CTk()
root.title("Shortest Path")
root.geometry("1800x800")
root.resizable(0, 0)

# ---------------------------- Création des frames --------------------------- #
var = ctk.CTkFrame(master=root)  # Frame à droite
graph = ctk.CTkFrame(master=root)  # Frame pour le graphique
graph2 = ctk.CTkFrame(master=root)  # Frame pour le graphique
city = ctk.CTkFrame(master = root)  # Frame en haut à gauche

# --------------------------- Placement des frames --------------------------- #
var.grid(row=0, column=15, rowspan=10, columnspan=5, sticky="nsew")  # Frame à droite prend 5 colonnes et toutes les lignes
graph.grid(row=3, column=0, rowspan=7, columnspan=7, sticky="nsew")  # Frame pour le graphique prend 5 colonnes et 7 lignes
graph2.grid(row=3, column=7, rowspan=7, columnspan=8, sticky="nsew")  # Frame pour le graphique prend 5 colonnes et 7 lignes
city.grid(row=0, column=0, rowspan=3, columnspan=15, sticky="nsew")  # Frame en haut à gauche prend 5 colonnes et 3 lignes

# Redimensionnement des lignes et colonnes pour que les frames s'adaptent à la taille de la fenêtre
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
for i in range(20):
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
fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=graph)
canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)

fig2 = Figure(figsize=(5, 5), dpi=100)
ax2 = fig2.add_subplot(111)
canvas2 = FigureCanvasTkAgg(fig2, master=graph2)
canvas2.get_tk_widget().pack(fill=ctk.BOTH, expand=True)

# -------------------------------- Label Title ------------------------------- #
var_title = ctk.CTkLabel(text="Variables", font=("Arial", 24), master = var)
var_title.grid(row=0, column=0, columnspan=4)

# ----------------------------- Taille Population ---------------------------- #
taille_pop_label = ctk.CTkLabel(text="Taille de la population: ", master = var, font = ("Arial", 16))
taille_pop_entry = ctk.CTkEntry(master = var)
taille_pop_label.grid(row=1, column=0, columnspan=2)
taille_pop_entry.grid(row=1, column=2, columnspan=2, sticky="w")

# ------------------------------ Chance Mutation ----------------------------- #
mutation_rate_label = ctk.CTkLabel(text="Chance de mutation: ", master = var, font = ("Arial", 16))
mutation_rate_entry = ctk.CTkEntry(master = var)
mutation_rate_label.grid(row=2, column=0, columnspan=2)
mutation_rate_entry.grid(row=2, column=2, columnspan=2, sticky="w")

# ----------------------------- Nombre Generation ---------------------------- #
nbre_gene_label = ctk.CTkLabel(text="Nbre de generation: ", master = var, font = ("Arial", 16))
nbre_gene_entry = ctk.CTkEntry(master = var)
nbre_gene_label.grid(row=3, column=0, columnspan=2)
nbre_gene_entry.grid(row=3, column=2, columnspan=2, sticky="w")

# ------------------------- Pourcentage bon individu ------------------------- #
percent_good_individu_label = ctk.CTkLabel(text="% bon individu: ", master = var, font = ("Arial", 16))
percent_good_individu_entry = ctk.CTkEntry(master = var)
percent_good_individu_label.grid(row=4, column=0, columnspan=2)
percent_good_individu_entry.grid(row=4, column=2, columnspan=2, sticky = "w")

# ----------------------- Pourcentage mauvais individu ----------------------- #
percent_bad_individu_label = ctk.CTkLabel(text="% mauvais individu: ", master = var, font = ("Arial", 16))
percent_bad_individu_entry = ctk.CTkEntry(master = var)
percent_bad_individu_label.grid(row=5, column=0, columnspan=2)
percent_bad_individu_entry.grid(row=5, column=2, columnspan=2, sticky = "w")

# ------------------------------ Bouton Start ------------------------------- #
start_btn = ctk.CTkButton(master = var, text="Start", font=("Arial", 34), command= lambda : main.algo_genetique(int(taille_pop_entry.get()), float(mutation_rate_entry.get()), int(nbre_gene_entry.get()), float(percent_good_individu_entry.get()), float(percent_bad_individu_entry.get()), canvas, ax, root, canvas2, ax2))
start_btn.grid(row=7, column=1,columnspan = 2, rowspan = 2, sticky="nsew")

# ------------------------------- Partie ville ------------------------------- #
# -------------------------------- Label Title ------------------------------- #
main_title_label = ctk.CTkLabel(text="Problème du voyageur de commerce", font=("Arial", 24), master = city)
main_title_label.grid(row=0, column=0, columnspan=5)

ville_random_btn = ctk.CTkButton(master = city, text="Ville Aléatoire", font=("Arial", 16), command=lambda: main.add_city("Ville " + str(len(main.ville_df)+1), ax, canvas, None))
ville_random_btn.grid(row=1, column=4)

nom_ville_title = ctk.CTkLabel(text="Nom de la ville: ", master = city, font = ("Arial", 16))
nom_ville_entry = ctk.CTkEntry(master = city)
nom_ville_title.grid(row=1, column=1, sticky = "e")
nom_ville_entry.grid(row=1, column=2)

add_city_btn = ctk.CTkButton(master = city, text="Ajouter", font=("Arial", 16), command= lambda: main.add_city(nom_ville_entry, ax, canvas, 2))
add_city_btn.grid(row=1, column=3, sticky = "w")

supp_city_btn = ctk.CTkButton(master = city, text="Supp", font=("Arial", 16), command=lambda:main.remove_last_city(axes= ax, canvas= canvas))
supp_city_btn.grid(row=1, column=0, sticky = "w")

# ---------------------------- initiate the window --------------------------- #


root.mainloop()