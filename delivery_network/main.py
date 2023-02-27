from graph import Graph, graph_from_file


g = g.graph_from_file("/home/onyxia/work/ensae-prog23/input/network.03.in")
print(g)
test=g.get_path_with_power(2,4,2)
print(test)
puissance=g.min_power(2,4)
print(puissance)