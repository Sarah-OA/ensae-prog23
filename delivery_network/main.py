# Changement de dossier de travail et import de la classe Graph
from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")
from graph import Graph, graph_from_file


# Penser à régler le problème suivant : lorsque minimiser_le_prix renvoie None, knap_sack va renvoyer une erreur

"""
g=Graph([])
g.add_edge(0,1,8)
g.add_edge(0,2,8)
g.add_edge(1,3,7)
g.add_edge(1,4,2)
g.add_edge(1,5,5)
g.add_edge(3,7,20)
g.add_edge(5,6,4)
trajets=[[7, 6, 20], [0, 4, 40], [1, 8, 10]]
camions=[[20, 30], [10, 15], [5, 8]]
B=45
profondeur, parent=g.resultat_dfs()
final=g.greedy(profondeur, parent, camions, trajets, B)
print(final)
"""
g=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.2.in")
arbre=g.kruskal()
profondeur, parents=arbre.resultat_dfs()
routes=open("/home/onyxia/work/ensae-prog23/input/routes.2.in", "r", encoding="utf-8")
trucks=open("/home/onyxia/work/ensae-prog23/input/trucks.2.in", "r", encoding="utf-8")
camions=arbre.lire_camions(trucks)
trajets=arbre.lire_trajets(routes)
B=25*10**9
final=arbre.greedy(profondeur, parents, camions, trajets, B)
