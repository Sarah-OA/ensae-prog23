""" 
    Test de l'affichage des graphes et du chemin à parcourir entre deux sommets avec graphviz.    
"""

from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")
from generate_graphviz import graphviz_generate_graph, get_path_with_power_graphviz, minpower_kruskal_graphviz
from graph import Graph, graph_from_file

# Test sur un petit graphe
graphe1=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.02.in")
arbre1=graphe1.kruskal()
profondeurs, parents= arbre1.resultat_dfs()
graphe_chemin1=graphviz_generate_graph(arbre1)

# Test sur un graphe plus grand
graphe2=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.03.in")
arbre2=graphe2.kruskal()
profondeurs, parents=arbre2.resultat_dfs()
graphe_chemin2=graphviz_generate_graph(arbre2)
