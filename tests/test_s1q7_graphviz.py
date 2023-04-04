""" 
    Test de l'affichage des graphes et du chemin à parcourir entre deux sommets avec graphviz.    
"""

from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")
from generate_graphviz import graphviz_generate_graph, get_path_with_power_graphviz
from graph import Graph, graph_from_file

# Test sur un petit graphe
graphe1=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.01.in")
graphe_chemin1=graphviz_generate_graph(graphe1)
dessin1=get_path_with_power_graphviz(graphe_chemin1, graphe1, 1, 3, 1)

# Test sur un graphe plus grand
graphe2=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.1.in")
graphe_chemin2=graphviz_generate_graph(graphe2)
dessin2=get_path_with_power_graphviz(graphe_chemin2, graphe2, 4, 16, 40)