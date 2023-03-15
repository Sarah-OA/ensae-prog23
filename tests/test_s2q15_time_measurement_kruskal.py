"""
    Mesure le temps moyen d'exécution de la fonction min_power_kruskal sur les trajets présents dans les fichiers route.
    Applique les trajets au fichier network.2.in.
"""

from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")

from graph import Graph, graph_from_file
from time import perf_counter

def lire_routes(routes):
    """
    Lit les trajets présents dans un fichier route et retourne une liste de tuples (départ, arrivée).
    """
    lines = routes.readlines()
    L=[]
    for line in lines[1:len(lines)]:
        line=line.split(" ")
        src, dest=line[0], line[1]
        L.append((src, dest))
    return L

def estimation_temps_minpower_k(routes, fichier_sortie):
    """
    Mesure et retourne le temps d'exécution moyen de min_power_kruskal sur les trajets d'un fichier routes.
    On calcule le temps de 10 trajets puis on le multiplie par le nombre de trajets du fichier routes.
    Par ailleurs, on crée des fichiers pour stocker la puissance minimum de chaque trajet.
    """
    t1=perf_counter()
    g=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.2.in")
    trajets=lire_routes(routes)
    for i in range(2):
        src, dest = trajets[i]
        src = int(src)
        dest = int(dest)
        power=g.min_power_kruskal(src, dest)[1]
        fichier_sortie.write(str(power))
        fichier_sortie.write("\n")
    t2=perf_counter()
    temps_total=t2-t1
    print(temps_total)
    return fichier_sortie
# Application des fonctions à chaque fichier routes et affichage du temps d'exécution
test=open("/home/onyxia/work/ensae-prog23/input/routes.1.in", "r", encoding="utf-8")
sortie=open("/home/onyxia/work/ensae-prog23/fichiers_tests_routes/route1.txt", "w", encoding="utf-8")
fichier = estimation_temps_minpower_k(test, sortie)
test.close()
sortie.close()