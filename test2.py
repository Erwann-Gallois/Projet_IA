import tkinter as tk

root = tk.Tk()
root.geometry("600x400")  # Taille de la fenêtre

# Création des frames
frame1 = tk.Frame(root, bg="blue", width=200, height=400)  # Réduction de la largeur à 200
frame2 = tk.Frame(root, bg="green", width=300, height=280)
frame3 = tk.Frame(root, bg="red", width=300, height=120)

# Placement des frames
frame1.grid(row=0, column=4, rowspan=10, columnspan=4, sticky="nsew")  # Réduction de la colonne à 4
frame2.grid(row=7, column=0, rowspan=7, columnspan=6, sticky="nsew")
frame3.grid(row=0, column=0, rowspan=3, columnspan=6, sticky="nsew")

# Redimensionnement des lignes et colonnes pour que les frames s'adaptent à la taille de la fenêtre
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
for i in range(10):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
