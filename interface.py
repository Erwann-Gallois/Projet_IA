import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import main as main
from CTkMessagebox import CTkMessagebox
import random as rd
import pandas as pd

# ---------------------------------- Fontion --------------------------------- #
def center_window(window, width=300, height=200):
    # Obtenir la taille de l'écran
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculer la position de la fenêtre pour la centrer
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
def start():
    # ------------- Verirification la valeur de taille de population ------------- #
    if (len(main.ville_df) <= 3):
        CTkMessagebox(title="Erreur", message="Il faut ajouter au moins une ville", icon="cancel")
        return
    taille_pop = taille_pop_entry.get()
    if (taille_pop == "" or (int(taille_pop) <= 0)):
        CTkMessagebox(title="Erreur", message="La taille de le population ne doit pas être vide ou doit etre un entier positif", icon="cancel")
        return
    elif (int(taille_pop) >= 100 and len(main.ville_df) < 6):
        CTkMessagebox(title="Erreur", message="La taille de le population est trop grande par rapport au nombre de villes", icon="cancel")
        return
    else:
        taille_pop = int(taille_pop)
    # ------------- Verirification la valeur de chance de mutation ------------- #
    mutation_rate = mutation_rate_entry.get()
    if (mutation_rate == "" or (float(mutation_rate) <= 0 or float(mutation_rate) > 1)):
        CTkMessagebox(title="Error", message="La chance de mutation ne doit pas être vide ou doit etre une probabilité", icon="cancel")
        return
    else:
        mutation_rate = float(mutation_rate)
    # ------------- Verirification la valeur de nombre de generation ------------- #
    nbre_gene = nbre_gene_entry.get()
    if (nbre_gene == "" or (int(nbre_gene) <= 0)):
        CTkMessagebox(title="Error", message="Le nombre de generation ne doit pas être vide ou doit etre un entier positif", icon="cancel")
        return
    else:
        nbre_gene = int(nbre_gene)
    # ------------- Verirification la valeur de pourcentage bon individu ------------- #
    percent_good_individu = percent_good_individu_entry.get()
    if (percent_good_individu == "" or (float(percent_good_individu) <= 0 or float(percent_good_individu) > 1)):
        CTkMessagebox(title="Error", message="Le pourcentage bon individu ne doit pas être vide ou doit etre une probabilité", icon="cancel")
        return
    else:
        percent_good_individu = float(percent_good_individu)
    # ------------- Verirification la valeur de pourcentage mauvais individu ------------- #
    percent_bad_individu = percent_bad_individu_entry.get()
    if (percent_bad_individu == "" or (float(percent_bad_individu) <= 0 or float(percent_bad_individu) > 1)):
        CTkMessagebox(title="Error", message="Le pourcentage mauvais individu ne doit pas être vide ou doit etre une probabilité", icon="cancel")
        return
    else:
        percent_bad_individu = float(percent_bad_individu)
    # -------------------- Mettre tout les boutons en disabled ------------------- #
    ville_random_btn.configure(state = "disabled")
    add_city_btn.configure(state = "disabled")
    supp_city_btn.configure(state = "disabled")    
    start_btn.configure(state = "disabled")
    taille_pop_entry.configure(state = "disabled")
    mutation_rate_entry.configure(state = "disabled")
    nbre_gene_entry.configure(state = "disabled")
    percent_good_individu_entry.configure(state = "disabled")
    percent_bad_individu_entry.configure(state = "disabled")
    main.algo_genetique(taille_pop, mutation_rate, nbre_gene, percent_good_individu, percent_bad_individu, canvas= canvas, axes= ax, canvas2= canvas2, axes2= ax2, root= root)
    # ------------------------- Mettre tout en modifiable ------------------------ #
    ville_random_btn.configure(state = "normal")
    add_city_btn.configure(state = "normal")
    supp_city_btn.configure(state = "normal") 
    start_btn.configure(state = "normal")
    taille_pop_entry.configure(state = "normal")
    mutation_rate_entry.configure(state = "normal")
    nbre_gene_entry.configure(state = "normal")
    percent_good_individu_entry.configure(state = "normal")
    percent_bad_individu_entry.configure(state = "normal")
# ---------------------------- Generation du root ---------------------------- #
root = ctk.CTk()
root.resizable(0, 0)

# ---------------------------- Création des frames --------------------------- #
var = ctk.CTkFrame(master=root)  # Frame à droite
graph = ctk.CTkFrame(master=root)  # Frame pour le graphique
graph2 = ctk.CTkFrame(master=root)  # Frame pour le graphique
city = ctk.CTkFrame(master = root)  # Frame en haut à gauche

# --------------------------- Placement des frames --------------------------- #
var.grid(row=0, column=15, rowspan=10, columnspan=5, sticky="nsew")  
graph.grid(row=3, column=0, rowspan=7, columnspan=7, sticky="nsew")  
graph2.grid(row=3, column=7, rowspan=7, columnspan=8, sticky="nsew")
city.grid(row=0, column=0, rowspan=3, columnspan=15, sticky="nsew")

# Redimensionnement des lignes et colonnes pour que les frames s'adaptent à la taille de la fenêtre
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
for i in range(20):
    root.grid_columnconfigure(i, weight=1)

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

# -------------------------------- Pratie var ------------------------------- #
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
percent_good_individu_label = ctk.CTkLabel(text="% bon individu pour la prochaine génération: ", master = var, font = ("Arial", 16))
percent_good_individu_entry = ctk.CTkEntry(master = var)
percent_good_individu_label.grid(row=4, column=0, columnspan=2)
percent_good_individu_entry.grid(row=4, column=2, columnspan=2, sticky = "w")

# ----------------------- Pourcentage mauvais individu ----------------------- #
percent_bad_individu_label = ctk.CTkLabel(text="Chance de retenu de mauvais individu: ", master = var, font = ("Arial", 16))
percent_bad_individu_entry = ctk.CTkEntry(master = var)
percent_bad_individu_label.grid(row=5, column=0, columnspan=2)
percent_bad_individu_entry.grid(row=5, column=2, columnspan=2, sticky = "w")

# ------------------------------ Bouton Start ------------------------------- #
start_btn = ctk.CTkButton(master = var, text="Start", font=("Arial", 34), command= lambda: start())
start_btn.grid(row=7, column=1,columnspan = 2, rowspan = 2, sticky="nsew")

# ------------------------------- Partie ville ------------------------------- #
main_title_label = ctk.CTkLabel(text="Problème du voyageur de commerce", font=("Arial", 24), master = city)
main_title_label.grid(row=0, column=0, columnspan=5)

ville_random_btn = ctk.CTkButton(master = city, text="Ville Aléatoire", font=("Arial", 16), command=lambda: main.add_city("Ville " + str(len(main.ville_df)+1), ax, canvas,root ,None))
ville_random_btn.grid(row=1, column=4)

nom_ville_title = ctk.CTkLabel(text="Nom de la ville: ", master = city, font = ("Arial", 16))
nom_ville_entry = ctk.CTkEntry(master = city)
nom_ville_title.grid(row=1, column=1, sticky = "e")
nom_ville_entry.grid(row=1, column=2)

add_city_btn = ctk.CTkButton(master = city, text="Ajouter", font=("Arial", 16), command= lambda: main.add_city(nom_ville_entry, ax, canvas, root, 2))
add_city_btn.grid(row=1, column=3, sticky = "w")

supp_city_btn = ctk.CTkButton(master = city, text="Supp", font=("Arial", 16), command=lambda:main.remove_last_city(axes= ax, canvas= canvas))
supp_city_btn.grid(row=1, column=0, sticky = "w")
# ------------------------ Initilisation de la fenetre ----------------------- #
center_window(root, 1800, 800)
root.title("Problème du voyageur de commerce")
root.mainloop()