# Projet_IA : Problème du voyageur de commerce

## Introduction

Un commercant doit aller dans plusieurs villes et doit passer dans toutes les villes, seulement il doit y passer qu'une seule fois. Il doit aussi retourner à sa position de départ. 

## Objectifs du projet
- Faire une interface graphique :
    - Pouvoir rentrer le nom des villes 
    - Voir une "carte" des villes rentrées (les villes sont placés aléatoirement)
    - Voir le chemin retenu a la fin de chaque itération
- Implémenter l'algorithme génétique
    - Trouver comment former un enfant, et la mutation (par exemple, inversion de deux paires de villes) 
    - Fonction d'évaluation : longueur du chemin

## Rendu du projet
- Soutenance de 10 min
    - Montrer le programme
    - Savoir expliquer le code

- Rapport de 3 - 4 pages
    - Qu'est qu'on a implémenter (individus, fonction d'évaluation, mutation)
    - Performances : Tableau avec pour chaque ville les distances du chemin le plus court
    - Code en annexe

## Idée de mutation 

1. **Mutation par inversion :** Sélectionnez une sous-séquence de villes et inversez l'ordre des villes dans cette sous-séquence.

2. **Mutation par échange :** Choisissez deux paires de villes adjacentes et échangez-les de manière à créer une nouvelle séquence.

3. **Mutation par inversion partielle :** Choisissez deux positions aléatoires dans la séquence de villes et inversez l'ordre des villes entre ces deux positions.

4. **Mutation par inversion double :** Choisissez deux paires de positions aléatoires dans la séquence de villes et inversez l'ordre des villes entre ces deux paires.

5. **Mutation par échange circulaire :** Choisissez une position de départ et une longueur pour un échange circulaire dans la séquence de villes.

6. **Mutation par décalage :** Décalez un groupe de villes vers la droite ou la gauche dans la séquence.
