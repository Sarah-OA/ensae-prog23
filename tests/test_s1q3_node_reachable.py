"""
    Test de la fonction get_path_with_power
"""
from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.00.in")
        self.assertEqual(g.get_path_with_power(1, 4, 11), [1, 2, 3, 4])
        self.assertEqual(g.get_path_with_power(1, 4, 10), None)

    def test_network2(self):
        g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.02.in")
        self.assertIn(g.get_path_with_power(1, 2, 11), [[1, 2], [1, 4, 3, 2]])
        self.assertEqual(g.get_path_with_power(1, 2, 5), [1, 4, 3, 2])

if __name__ == '__main__':
    unittest.main()