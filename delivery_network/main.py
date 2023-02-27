from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.01.in"

g = graph_from_file("/home/onyxia/work/ensae-prog23/input/network.04.in")
print(g)
test=g.get_path_with_power(3,2,2)
print(test)