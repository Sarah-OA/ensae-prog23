"""
    Test de la fonction greedy sur un gros graphe
"""
from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")

import unittest 
from graph import Graph, graph_from_file
from time import perf_counter

g=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.2.in")
arbre=g.kruskal()
profondeur, parents=arbre.resultat_dfs()
routes=open("/home/onyxia/work/ensae-prog23/input/routes.2.in", "r", encoding="utf-8")
trucks=open("/home/onyxia/work/ensae-prog23/input/trucks.2.in", "r", encoding="utf-8")
camions=arbre.lire_camions(trucks)
trajets=arbre.lire_routes(routes)
B=25*10**9
temps1= perf_counter()
final=arbre.greedy(profondeur, parents, camions, trajets, B)
temps2= perf_counter()
temps_final= temps2 - temps1
print(final, temps_final)