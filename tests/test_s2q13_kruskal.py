"""
    Test de la fonction kruskal
"""
from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")

import unittest 
from graph import Graph, graph_from_file


class Test_TreeLoading(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.02.in")
        arbre=g.kruskal()
        self.assertEqual(arbre.nb_nodes, 4)
        self.assertEqual(arbre.nb_edges, 3)
    def test_network1(self):
        g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.03.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 4)

if __name__ == '__main__':
    unittest.main()
