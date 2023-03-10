from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")

from graph import Graph, graph_from_file
from time import perf_counter

# Test des algorithmes sur un petit graphe
g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.03.in") # Création du graphe
trajet=g.get_path_with_power(2,4,7) # Essai de trajet entre deux villes et une puissance de 7
puissance=g.min_power(2,4) # Calcul de la puissance nécessaire sur le trajet 
print("Pour faire le trajet entre 2 et 4, il faut utiliser l'itinéraire suivant : ", trajet)
print("Cela demande la puissance minimale suivante : ", puissance)
# Test des algorithmes sur un grand graphe
g_2 = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.1.in") # Création du graphe
trajet_2=g_2.get_path_with_power(20,5,95) # Essai de trajet entre deux villes et une puissance de 1000000
puissance_2=g_2.min_power(20,5) # Calcul de la puissance nécessaire sur le trajet 
print("Pour faire le trajet entre 20 et 5, il faut utiliser l'itinéraire suivant : ", trajet_2)
print("Cela demande la puissance minimale suivante : ", puissance_2)

# S2 Q1
def lire_routes(routes):
    lines = routes.readlines()
    L=[]
    for line in lines[1:len(lines)]:
        line=line.split(" ")
        src, dest=line[0], line[1]
        L.append((src, dest))
    return L

def estimation_temps_minpower(routes):
    t1=perf_counter()
    g=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.2.in")
    trajets=lire_routes(routes)
    for i in range(1,10):
        print("coucou")
        src, dest = trajets[i]
        src = int(src)
        dest = int(dest)
        g.min_power(src, dest)
        print("min power ok :)")
    t2=perf_counter()
    temps_minpower=((t2-t1)/10)*len(trajets)
    return temps_minpower

test=open("/home/onyxia/work/ensae-prog23/input/routes.1.in", "r", encoding="utf-8")
print(estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.2.in", "r", encoding="utf-8")
print(estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.3.in", "r", encoding="utf-8")
print(estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.4.in", "r", encoding="utf-8")
print(estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.5.in", "r", encoding="utf-8")
print(estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.6.in", "r", encoding="utf-8")
print(estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.7.in", "r", encoding="utf-8")
print(estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.8.in", "r", encoding="utf-8")
print(estimation_temps_minpower(test))
test.close()
test=open("/home/onyxia/work/ensae-prog23/input/routes.9.in", "r", encoding="utf-8")
print(estimation_temps_minpower(test))
test.close()