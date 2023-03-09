from os import chdir
chdir("/home/onyxia/work/ensae-prog23/delivery_network")

from graph import Graph, graph_from_file


g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.03.in")
test=g.get_path_with_power(2,4,2)

puissance=g.min_power(2,4)
