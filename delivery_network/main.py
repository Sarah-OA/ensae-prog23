# Changement de dossier de travail et import de la classe Graph
from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")
from graph import Graph, graph_from_file


def lire_trajets(routes):
"""
Lit les trajets présents dans un fichier route et retourne une liste de listes [départ, arrivée, utilité].
"""
lines = routes.readlines()
L=[]
for line in lines[1:len(lines)]:
    line=line.split(" ")
    trajet=[int(line[0]), int(line[1]), int(line[2])]
    L.append(trajet)
return L

def lire_camions(trucks):
    """ Lit les camions présents dans un fichier trucks et retourne une liste de listes [puissance, prix]
    """
    lines = trucks.readlines()
    L=[]
    for line in lines[1:len(lines)]:
        line=line.split(" ")
        camion=[int(line[0]), int(line[1])]
        L.append(camion)
    return L

routes=open("/home/onyxia/work/ensae-prog23/input/routes.8.in", "r", encoding="utf-8")
trajets=lire_trajets(routes)
trucks=open("/home/onyxia/work/ensae-prog23/input/trucks.2.in", "r", encoding="utf-8")
camions=lire_camions(trucks)
routes.close()
trucks.close()
        
g=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.1.in")
arbre=g.kruskal()
profondeur, parents=arbre.resultat_dfs()
routes=open("/home/onyxia/work/ensae-prog23/input/routes.1.in", "r", encoding="utf-8")
trucks=open("/home/onyxia/work/ensae-prog23/input/trucks.1.in", "r", encoding="utf-8")
"""
trajets=lire_trajets(routes)
camions=lire_camions(trucks)
camions_choisis=arbre.minimiser_le_prix(profondeur, parents, camions, trajets, 12)
print(camions_choisis)
B=1000000
resultat=arbre.optimisation(profondeur, parents, camions, trajets)
print(resultat)
"""
# Penser à régler le problème suivant : lorsque minimiser_le_prix renvoie None, knap_sack va renvoyer une erreur