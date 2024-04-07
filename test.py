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

# Création des frames
var = ctk.CTkFrame(root, fg_color="blue")  # Frame à droite
graph = ctk.CTkFrame(root, fg_color="green")  # Frame pour le graphique
city = ctk.CTkFrame(root, fg_color="red")  # Frame en haut à gauche

# Placement des frames
var.grid(row=0, column=7, rowspan=10, columnspan=4, sticky="nsew")  # Frame à droite prend 5 colonnes et toutes les lignes
graph.grid(row=3, column=0, rowspan=7, columnspan=7, sticky="nsew")  # Frame pour le graphique prend 5 colonnes et 7 lignes
city.grid(row=0, column=0, rowspan=3, columnspan=7, sticky="nsew")  # Frame en haut à gauche prend 5 colonnes et 3 lignes

# Redimensionnement des lignes et colonnes pour que les frames s'adaptent à la taille de la fenêtre
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
for i in range(10):
    root.grid_columnconfigure(i, weight=1)

fig, ax = plt.subplots()
ax.set_title('Carte des Villes')
ax.set_xlabel('coordonnées x')
ax.set_ylabel('coordonnées y')

ax.set_ylim(0, main.TAILLE_GRILLE_Y)
ax.set_xlim(0, main.TAILLE_GRILLE_X)

canvas = FigureCanvasTkAgg(fig, master=graph)
canvas.draw()
# initiate the window
root.mainloop()