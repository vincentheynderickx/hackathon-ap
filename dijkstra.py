import create_graph_osdm
import numpy as np

matrice = create_graph_osdm.get_graph_destinations()

#conversion de la matrice de distances en un dictionnaire de voisins pour dijkstra
m=np.array([[0,2,3],[2,0,5],[3,5,0]])
g={}
l=np.shape(matrice)[0] 
for i in range(l):
    voisins=[0 for k in range(l-1)]
    for j in range(l):
        if j<i:
            voisins[j]=(j,matrice[i,j]) 
        if j>i:
            voisins[j-1]=(j,matrice[i,j]) 
    g[i]=voisins


def dijkstra(g, entree, sortie, infini=2 ** 30):
    marques = []  # Contiendra le nom des sommets visités
 
    # Distance minimale trouvée pour chaque valeur dès le départ
    distances = {sommet: (None, infini) for sommet in g}
    #     Sommet d'origine (None par défaut), distance
 
    distances[entree] = 0  # On initialise la distance du départ
 
    # Nombre de sommets du graphe, longueur du dictionnaire
    taille_graph = len(g)
 
    selection = entree
    coefficient = 0
 
    while len(marques) < taille_graph:
        # On marque la 'selection'
        marques.append(selection)
        print(f"On marque la sélection {selection} avec poids {coefficient}")
        # On parcours les voisins de 'selection'
        for voisin in g[selection]:
            # voisin est le couple (sommet, poids de l'arête)
 
            sommet = voisin[0]  # Le sommet qu'on, parcours
            poids = voisin[1]  # Le poids de selection au sommet
            if sommet not in marques:
                # Pour chaque voisin non marqué,
                # on compare coefficient + arête
                # avec la distance du dictionnaire
                d = distances[sommet][1]
                if coefficient + poids < d:
                    # Si c'est plus petit, on remplace
                    print(f"Pour {sommet}, on remplace {distances[sommet]}", end='')
                    print(f" par {(selection, coefficient + poids)}")
                    distances[sommet] = (selection, coefficient + poids)
 
        # On recherche le minimum parmi les non marqués
        minimum = (None, infini)
        for sommet in g:
            if sommet not in marques and distances[sommet][1] < minimum[1]:
                minimum = (sommet, distances[sommet][1])
 
        # puis il devient notre nouvelle 'selection'
        selection, coefficient = minimum
 
    sommet = sortie
    parcours = [sortie]
    longueur = distances[sortie][1]
    # On parcours le graphe à l'envers pour obtenir le chemin
    while sommet != entree:
        sommet = distances[sommet][0]
        parcours.append(sommet)
    parcours.reverse()
 
    # On renvoie le chemin le plus court et la longueur
    return parcours, longueur


