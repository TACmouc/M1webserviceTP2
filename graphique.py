import tkinter as tk

# Fonction appelée lorsqu'une cellule est cliquée
def colorier_cellule(event):
    # Obtient les coordonnées de la cellule cliquée
    x, y = event.widget.grid_info()["row"], event.widget.grid_info()["column"]
    # Obtient la couleur sélectionnée dans la palette
    couleur = couleur_palette.get()
    # Applique la couleur à la cellule
    event.widget.itemconfig(cellules[y][x], fill=couleur)

# Crée la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Tableau de 1000x700")

# Crée une palette de couleurs
couleur_palette = tk.StringVar()
couleur_palette.set("red")  # Couleur par défaut
palette = tk.OptionMenu(fenetre, couleur_palette, "red", "blue", "green", "yellow")
palette.grid(row=0, column=0)

# Crée un tableau de cellules
cellules = []
for i in range(70):
    ligne = []
    for j in range(100):
        cellule = tk.Canvas(fenetre, width=10, height=10, bg="white")
        cellule.grid(row=i+1, column=j+1)
        cellule.bind("<Button-1>", colorier_cellule)
        ligne.append(cellule)
    cellules.append(ligne)

# Exécute la boucle principale de l'interface graphique
fenetre.mainloop()

