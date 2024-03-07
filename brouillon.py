chemins = []
for i in range(nbre_ville - 1):
    chemin = Chemin(cities[i], cities[i+1])
    chemins.append(chemin)

# Assurez-vous que chaque ville a au moins un chemin en créant un chemin supplémentaire entre la dernière ville et la première ville
chemin = Chemin(cities[-1], cities[0])
chemins.append(chemin)

# Creer des chemins aleatoires entre chaque ville sans doublons
for i in range(nbre_ville - 1):
    depart = cities[np.random.randint(0, nbre_ville)]
    arrivee = cities[np.random.randint(0, nbre_ville)]
    # Verifie si le depart et l'arrivee sont les memes
    if depart == arrivee:
        while depart == arrivee:
            arrivee = cities[np.random.randint(0, nbre_ville)]
    # Verifie si le chemin existe deja
    for chemin in chemins : 
        if (depart == chemin.depart and arrivee == chemin.arrivee) or (depart == chemin.arrivee and arrivee == chemin.depart):
            while (depart == chemin.depart and arrivee == chemin.arrivee) or (depart == chemin.arrivee and arrivee == chemin.depart):
                depart = cities[np.random.randint(0, nbre_ville)]
                arrivee = cities[np.random.randint(0, nbre_ville)]
                if depart == arrivee:
                    while depart == arrivee:
                        arrivee = cities[np.random.randint(0, nbre_ville)]
    chemin = Chemin(depart, arrivee)
    chemins.append(chemin) 

for chemin in chemins:
    print(chemin.toString())