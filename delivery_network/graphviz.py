import graphviz
from graph import Graph, graph_from_file

def graphviz_generate_graph(graphe):
    dessin=graphviz.Graph("Graphe", format="png")
    for node in graphe.nodes:
        dessin.node(str(node))
    for edge in graphe.edges:
        dessin.edge(str(edge[0]), str(edge[1]))
    dessin.render(directory="/home/onyxia/work/ensae-prog23/output_graphviz")
    return dessin

def get_path_with_power_graphviz(graphe_chemin, graphe, src, dest, power):
    chemin=graphe.get_path_with_power(src,dest,power)
    if chemin==None:
        return None
    else:
        for list in chemin[0:len(chemin)-1]:
            print(list)
            graphe_chemin.edge(str(list), str(list+1), color="red")
        graphe_chemin.render(directory="/home/onyxia/work/ensae-prog23/output_graphviz")
        return graphe_chemin

graphe=graph_from_file("/home/onyxia/work/ensae-prog23/input/network.1.in")
graphe_chemin=graphviz_generate_graph(graphe)
dessin=get_path_with_power_graphviz(graphe_chemin, graphe, 4, 16, 40)

