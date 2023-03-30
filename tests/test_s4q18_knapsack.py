    """
    Test de la fonction knapsack sur un petit graphe
    """

from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")

from graph import graph_from_file

g=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.02.in")
arbre=g.kruskal()
profondeur, parents=arbre.resultat_dfs()
routes=open("/home/onyxia/work/ensae-prog23/input/routes.02.in", "r", encoding="utf-8")
trucks=open("/home/onyxia/work/ensae-prog23/input/trucks.02.in", "r", encoding="utf-8")
camions=arbre.lire_camions(trucks)
trajets=arbre.lire_trajets(routes)
camions_choisis=arbre.minimiser_le_prix(profondeur, parents, camions, trajets, 5)
B=80
resultat=arbre.optimisation(profondeur, parents, camions, trajets, B)
print("Profit : ", resultat)
print("Trajets à parcourir :", routes_choix)
print("Camions à choisir : ", camions_choisis)
