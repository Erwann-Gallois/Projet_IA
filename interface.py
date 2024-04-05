# import customtkinter as tk



# app = tk.CTk()
# app.title('Shortest Path')
# app.geometry('900x600')

# label = tk.CTkLabel(app, text="Diagramme des villes")
# label.grid(row=0, column=0, pady=(550,10),padx=(200,10))

# button = tk.CTkButton(app, text="Ville Aléatoire", command=clic)


# app.mainloop()

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import main as main

# Fonction pour créer un graphique simple
def create_graph():

    fig, ax = plt.subplots()
    ax.set_title('Carte des Villes')
    ax.set_xlabel('coordonnées x')
    ax.set_ylabel('coordonnées y')

    ax.set_ylim(0, main.TAILLE_GRILLE_Y)
    ax.set_xlim(0, main.TAILLE_GRILLE_X)
    
    return fig

# Fonction pour intégrer le graphique dans le widget Frame
def embed_graph(frame):
    fig = create_graph()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(sticky='sw')



# Création de la fenêtre principale tkinter
root = tk.Tk()
root.title("Shortest Path")
root.geometry("900x600")

# Création d'un widget Frame pour contenir les boutons
random_button = tk.Button(root, text="Random",font=("Arial",30),bg="lightgrey")
random_button.grid(row=0, column=0, sticky="nw", pady=(65, 0), padx=(465, 0))

# Création d'un widget Frame pour contenir le graphique
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
graph_frame = ttk.Frame(root, padding=(10, 10, 0, 0))
graph_frame.grid(row=1, column=0, sticky="sw")

# Intégration du graphique dans le widget Frame
embed_graph(graph_frame)

# Configurer l'étirement de la grille pour que le graphique s'adapte à la taille de la fenêtre
#root.columnconfigure(0, weight=1)


root.mainloop()

            