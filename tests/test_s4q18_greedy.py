"""
    Test de la fonction greedy sur un gros graphe
"""
from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")

import unittest 
from graph import Graph, graph_from_file


g=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.2.in")
arbre=g.kruskal()
profondeur, parents=arbre.resultat_dfs()
routes=open("/home/onyxia/work/ensae-prog23/input/routes.2.in", "r", encoding="utf-8")
trucks=open("/home/onyxia/work/ensae-prog23/input/trucks.2.in", "r", encoding="utf-8")
camions=arbre.lire_camions(trucks)
trajets=arbre.lire_trajets(routes)
B=25*10**9
final=arbre.greedy(profondeur, parents, camions, trajets, B)
