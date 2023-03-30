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

def estimation_temps_minpower_k(graphe, profondeurs, parents, routes, fichier_sortie):
    """
    Mesure et retourne le temps d'exécution moyen de min_power_kruskal sur les trajets d'un fichier routes.
    On calcule le temps de 10 trajets puis on le multiplie par le nombre de trajets du fichier routes.
    Par ailleurs, on crée des fichiers pour stocker la puissance minimum de chaque trajet.
    """
    t1=perf_counter()
    for i in range(len(trajets)):
        src, dest = trajets[i]
        src = int(src)
        dest = int(dest)
        power=graphe.min_power_kruskal(profondeurs, parents, src, dest)[1]
        fichier_sortie.write(str(power))
        fichier_sortie.write("\n")
    t2=perf_counter()
    temps_total=t2-t1
    print(temps_total)
    return fichier_sortie
# Application des fonctions à chaque fichier routes et affichage du temps d'exécution
g=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.5.in")
mst = g.kruskal() #on réduit la complexité en utilisant l'arbre recouvrant de poids minimal
profondeurs, parents = mst.resultat_dfs() #on stocke les dictionnaires représentant les profondeurs et parents des noeuds

sortie=open("/home/onyxia/work/ensae-prog23/fichiers_tests_routes/route1.txt", "w", encoding="utf-8")
routes=open("/home/onyxia/work/ensae-prog23/input/routes.1.in", "r", encoding="utf-8")
trajets=lire_routes(routes)
fichier = estimation_temps_minpower_k(mst,profondeurs, parents, routes, sortie)
sortie.close()
routes.close()

sortie=open("/home/onyxia/work/ensae-prog23/fichiers_tests_routes/route2.txt", "w", encoding="utf-8")
routes=open("/home/onyxia/work/ensae-prog23/input/routes.2.in", "r", encoding="utf-8")
trajets=lire_routes(routes)
fichier = estimation_temps_minpower_k(mst,profondeurs, parents, routes, sortie)
sortie.close()
routes.close()

sortie=open("/home/onyxia/work/ensae-prog23/fichiers_tests_routes/route3.txt", "w", encoding="utf-8")
routes=open("/home/onyxia/work/ensae-prog23/input/routes.3.in", "r", encoding="utf-8")
trajets=lire_routes(routes)
fichier = estimation_temps_minpower_k(mst,profondeurs, parents, routes, sortie)
sortie.close()
routes.close()


sortie=open("/home/onyxia/work/ensae-prog23/fichiers_tests_routes/route4.txt", "w", encoding="utf-8")
routes=open("/home/onyxia/work/ensae-prog23/input/routes.4.in", "r", encoding="utf-8")
trajets=lire_routes(routes)
fichier = estimation_temps_minpower_k(mst,profondeurs, parents, routes, sortie)
sortie.close()
routes.close()


sortie=open("/home/onyxia/work/ensae-prog23/fichiers_tests_routes/route5.txt", "w", encoding="utf-8")
routes=open("/home/onyxia/work/ensae-prog23/input/routes.5.in", "r", encoding="utf-8")
trajets=lire_routes(routes)
fichier = estimation_temps_minpower_k(mst,profondeurs, parents, routes, sortie)
sortie.close()
routes.close()

sortie=open("/home/onyxia/work/ensae-prog23/fichiers_tests_routes/route6.txt", "w", encoding="utf-8")
routes=open("/home/onyxia/work/ensae-prog23/input/routes.6.in", "r", encoding="utf-8")
trajets=lire_routes(routes)
fichier = estimation_temps_minpower_k(mst,profondeurs, parents, routes, sortie)
sortie.close()
routes.close()


sortie=open("/home/onyxia/work/ensae-prog23/fichiers_tests_routes/route7.txt", "w", encoding="utf-8")
routes=open("/home/onyxia/work/ensae-prog23/input/routes.7.in", "r", encoding="utf-8")
trajets=lire_routes(routes)
fichier = estimation_temps_minpower_k(mst,profondeurs, parents, routes, sortie)
sortie.close()
routes.close()


sortie=open("/home/onyxia/work/ensae-prog23/fichiers_tests_routes/route8.txt", "w", encoding="utf-8")
routes=open("/home/onyxia/work/ensae-prog23/input/routes.8.in", "r", encoding="utf-8")
trajets=lire_routes(routes)
fichier = estimation_temps_minpower_k(mst,profondeurs, parents, routes, sortie)
sortie.close()
routes.close()


sortie=open("/home/onyxia/work/ensae-prog23/fichiers_tests_routes/route9.txt", "w", encoding="utf-8")
routes=open("/home/onyxia/work/ensae-prog23/input/routes.9.in", "r", encoding="utf-8")
trajets=lire_routes(routes)
fichier = estimation_temps_minpower_k(mst,profondeurs, parents, routes, sortie)
sortie.close()
routes.close()