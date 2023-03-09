from graph import graph_from_file
import unittest   # The test framework

class Test_Algorithms(unittest.TestCase):
    def test_network03(self):
       # Test des algorithmes sur un petit graphe
        g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.03.in") # Création du graphe
        trajet=g.get_path_with_power(2,4,7) # Essai de trajet entre deux villes et une puissance de 7
        puissance=g.min_power(2,4) # Calcul de la puissance nécessaire sur le trajet 
        print("Pour faire le trajet entre 2 et 4, il faut utiliser l'itinéraire suivant : ", trajet)
        print("Cela demande la puissance minimale suivante : ", puissance)
    def test_network1(self):
        # Test des algorithmes sur un grand graphe
        g_2 = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.1.in") # Création du graphe
        trajet_2=g_2.get_path_with_power(20,5,95) # Essai de trajet entre deux villes et une puissance de 1000000
        puissance_2=g_2.min_power(20,5) # Calcul de la puissance nécessaire sur le trajet 
        print("Pour faire le trajet entre 20 et 5, il faut utiliser l'itinéraire suivant : ", trajet_2)
        print("Cela demande la puissance minimale suivante : ", puissance_2)

if __name__ == '__main__':
    unittest.main()