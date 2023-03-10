    """
    Test des fonctions graph_from_file, get_path_with_power et min_power avec un graphe simple et un graphe plus complexe.
    """

from graph import graph_from_file
import unittest   # The test framework

class Test_Algorithms(unittest.TestCase):

    def test_network1(self):
        # Test des algorithmes sur un petit graphe
        g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.03.in") # Création du graphe
        puissance=g.min_power(1,4) # Calcul de la puissance nécessaire sur le trajet entre les points 1 et 4
        self.assertEqual(g.min_power(1,4), (10, [[1, 2, 3, 4]]))
    
    def test_network3(self):
        # Test des algorithmes sur un grand graphe
        g= graph_from_file("/home/onyxia/work/ensae-prog23/input/network.1.in") # Création du graphe
        puissance=g.min_power(20,5) # Calcul de la puissance nécessaire sur le trajet entre les points 20 et 5
        self.assertEqual(g.min_power(20,5), (13, [[20, 8, 1, 5]]))
if __name__ == '__main__':
    unittest.main()