"""
    Test de la fonction greedy sur un graphe
"""
from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")

import unittest 
from graph import Graph, graph_from_file
from time import perf_counter

# Ouverture du fichier et création de l'arbre couvrant de poids minimal
g=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.1.in")
arbre=g.kruskal()
profondeurs, parents=arbre.resultat_dfs()
routes=open("/home/onyxia/work/ensae-prog23/input/routes.1.in", "r", encoding="utf-8")
trucks=open("/home/onyxia/work/ensae-prog23/input/trucks.0.in", "r", encoding="utf-8") # Ouverture du premier fichier de camions
camions=arbre.lire_camions(trucks)
trajets=arbre.lire_routes(routes)
B=25*10**9
temps1= perf_counter()
final=arbre.greedy(profondeurs, parents, camions, trajets, B) # Test de greedy
temps2= perf_counter()
temps_final= temps2 - temps1
print(final[0], temps_final)
trucks.close()
trucks=open("/home/onyxia/work/ensae-prog23/input/trucks.1.in", "r", encoding="utf-8")
camions=arbre.lire_camions(trucks)
temps1= perf_counter()
final=arbre.greedy(profondeurs, parents, camions, trajets, B)
temps2= perf_counter()
temps_final= temps2 - temps1
print(final[0], temps_final) # affichage du profit et du temps de calcul de greedy
trucks.close()
trucks=open("/home/onyxia/work/ensae-prog23/input/trucks.2.in", "r", encoding="utf-8")
camions=arbre.lire_camions(trucks)
temps1= perf_counter()
final=arbre.greedy(profondeurs, parents, camions, trajets, B)
temps2= perf_counter()
temps_final= temps2 - temps1
print(final[0], temps_final)
trucks.close()