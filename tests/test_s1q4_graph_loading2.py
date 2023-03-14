    """
    Test de lecture de la distance
    """
from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")

import unittest 
from graph import Graph, graph_from_file

class Test_GraphLoading(unittest.TestCase):
    def test_network4(self):
        g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.04.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 4)
        self.assertEqual(g.graph[1][0][2], 6)

if __name__ == '__main__':
    unittest.main()