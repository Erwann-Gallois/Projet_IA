import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import main as main

# generate root
root = ctk.CTk()
root.title("Shortest Path")
root.geometry("900x600")
root.resizable(0, 0)

# ---------------------------- Création des frames --------------------------- #
var = ctk.CTkFrame(master=root)  # Frame à droite
graph = ctk.CTkFrame(master=root)  # Frame pour le graphique
city = ctk.CTkFrame(root, fg_color="red")  # Frame en haut à gauche

# --------------------------- Placement des frames --------------------------- #
var.grid(row=0, column=7, rowspan=10, columnspan=4, sticky="nsew")  # Frame à droite prend 5 colonnes et toutes les lignes
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
for i in range(10):
    var.grid_columnconfigure(i, weight=1)
# ------------------------------- Partie graph ------------------------------- #
fig, ax = plt.subplots()
ax.set_title('Carte des Villes')
ax.set_xlabel('coordonnées x')
ax.set_ylabel('coordonnées y')

ax.set_ylim(0, main.TAILLE_GRILLE_Y)
ax.set_xlim(0, main.TAILLE_GRILLE_X)

canvas = FigureCanvasTkAgg(fig, master=graph)
canvas.draw()
canvas.get_tk_widget().pack(side= "left", fill="both", expand=True)
# ------------------------------ Partie variable ----------------------------- #

# -------------------------------- Label Title ------------------------------- #
label1 = ctk.CTkLabel(text="Variables", font=("Arial", 20), master = var)
label1.grid(row=0, column=0, columnspan=2, pady=(10, 10))

# ----------------------------- Taille Population ---------------------------- #
label2 = ctk.CTkLabel(text="Taille de la population: ", master = var)
entry2 = ctk.CTkEntry(master = var)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1, sticky="ew", ipadx=10)

# ------------------------------ Chance Mutation ----------------------------- #
label3 = ctk.CTkLabel(text="Chance de mutation: ", master = var)
entry3 = ctk.CTkEntry(master = var)
label3.grid(row=2, column=0)
entry3.grid(row=2, column=1, sticky="ew", ipadx=10)

# ----------------------------- Nombre Generation ---------------------------- #
label4 = ctk.CTkLabel(text="Nombre de generation: ", master = var)
entry4 = ctk.CTkEntry(master = var)
label4.grid(row=3, column=0)
entry4.grid(row=3, column=1, sticky="nsew", ipadx=2)

# ------------------------- Pourcentage bon individu ------------------------- #
label5 = ctk.CTkLabel(text="Pourcentage bon individu: ", master = var)
entry5 = ctk.CTkEntry(master = var)
label5.grid(row=4, column=0)
entry5.grid(row=4, column=1, sticky="ew", ipadx=10)

# ----------------------- Pourcentage mauvais individu ----------------------- #
label6 = ctk.CTkLabel(text="Pourcentage mauvais individu: ", master = var)
entry6 = ctk.CTkEntry(master = var)
label6.grid(row=5, column=0)
entry6.grid(row=5, column=1, sticky="ew", ipadx=10)

# ---------------------------- initiate the window --------------------------- #
root.mainloop()