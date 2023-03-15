    """
    Mesure le temps moyen d'exécution de la fonction min_power sur les trajets présents dans les fichiers route.
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

def estimation_temps_minpower(routes):
    """
    Mesure et retourne le temps d'exécution moyen de min_power sur les trajets d'un fichier routes.
    On calcule le temps de 10 trajets puis on le multiplie par le nombre de trajets du fichier routes.
    """
    t1=perf_counter()
    g=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.2.in")
    trajets=lire_routes(routes)
    for i in range(1,10):
        src, dest = trajets[i]
        src = int(src)
        dest = int(dest)
        g.min_power(src, dest)
    t2=perf_counter()
    temps_minpower=((t2-t1)/10)*len(trajets)
    return temps_minpower

# Application des fonctions à chaque fichier routes et affichage du temps d'exécution

test=open("/home/onyxia/work/ensae-prog23/input/routes.1.in", "r", encoding="utf-8")
print("route 1 : ", estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.2.in", "r", encoding="utf-8")
print("route 2 :", estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.3.in", "r", encoding="utf-8")
print("route 3 :", estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.4.in", "r", encoding="utf-8")
print("route 4 :", estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.5.in", "r", encoding="utf-8")
print("route 5 :", estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.6.in", "r", encoding="utf-8")
print("route 6 :", estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.7.in", "r", encoding="utf-8")
print("route 7 :", estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.8.in", "r", encoding="utf-8")
print("route 8 :", estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.9.in", "r", encoding="utf-8")
print("route 9 :", estimation_temps_minpower(test))
test.close()
