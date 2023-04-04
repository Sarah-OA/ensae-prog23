    """
    Test de la fonction min_power
    """

# This will work if ran from the root folder.
from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")

from graph import graph_from_file
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.00.in")
        mst=g.kruskal()
        profondeurs, parents = mst.resultat_dfs()
        self.assertEqual(g.min_power_kruskal(profondeurs, parents, 1, 4)[1], 11)
        self.assertEqual(g.min_power_kruskal(profondeurs, parents, 2, 4)[1], 10)
    def test_network1(self):
        g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.04.in")
        mst=g.kruskal()
        profondeurs, parents = mst.resultat_dfs()
        self.assertEqual(g.min_power_kruskal(profondeurs, parents, 1, 4)[1], 4)

if __name__ == '__main__':
    unittest.main()
