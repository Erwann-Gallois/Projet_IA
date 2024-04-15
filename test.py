import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import main as main

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
fig, ax = plt.subplots()
ax.set_title('Carte des Villes', fontsize=20)
ax.set_xlabel('coordonnées x')
ax.set_ylabel('coordonnées y')

ax.set_ylim(0, main.TAILLE_GRILLE_Y)
ax.set_xlim(0, main.TAILLE_GRILLE_X)

canvas = FigureCanvasTkAgg(fig, master=graph)
canvas.draw()
canvas.get_tk_widget().pack(side= "left", fill="both", expand=True)
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
button.grid(row=7, column=1,columnspan = 2, rowspan = 2, sticky="nsew")

# ------------------------------- Partie ville ------------------------------- #
# -------------------------------- Label Title ------------------------------- #
label7 = ctk.CTkLabel(text="Problème du voyageur de commerce", font=("Arial", 24), master = city)
label7.grid(row=0, column=0, columnspan=5)

button = ctk.CTkButton(master = city, text="Ville Aléatoire", font=("Arial", 16), command=lambda: main.add_city(None, "Ville " + str(len(main.ville_df)+1)))
button.grid(row=1, column=4)

label8 = ctk.CTkLabel(text="Nom de la ville: ", master = city, font = ("Arial", 16))
entry8 = ctk.CTkEntry(master = city)
label8.grid(row=1, column=1, sticky = "e")
entry8.grid(row=1, column=2)

button = ctk.CTkButton(master = city, text="Ajouter", font=("Arial", 16), command= lambda: main.add_city(entry8))
button.grid(row=1, column=3, sticky = "w")

button = ctk.CTkButton(master = city, text="Supp", font=("Arial", 16), command=lambda:main.remove_last_city)
button.grid(row=1, column=0, sticky = "w")



# ---------------------------- initiate the window --------------------------- #
root.mainloop()
root.destroy()