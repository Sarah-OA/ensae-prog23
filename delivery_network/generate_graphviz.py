import graphviz
from graph import Graph, graph_from_file

def graphviz_generate_graph(graphe):
    """
        Crée la représentation visuelle du graphe.
    """
    dessin=graphviz.Graph("Graphe", format="png")
    for node in graphe.nodes:
        dessin.node(str(node)) # ajoute chaque sommet du graphe
    for edge in graphe.edges:
        dessin.edge(str(edge[0]), str(edge[1])) # ajoute chaque arète du graphe
    dessin.render(directory="/home/onyxia/work/ensae-prog23/output_graphviz")
    return dessin

def get_path_with_power_graphviz(graphe_chemin, graphe, src, dest, power):
    """
        Crée la représentation visuelle du chemin
    """
    chemin=graphe.get_path_with_power(src,dest,power)
    if chemin==None:
        return None
    else:
        for list in chemin[0:len(chemin)-1]:
            graphe_chemin.edge(str(list), str(list+1), color="red") # ajoute une arète rouge entre chaque sommet du chemin
        graphe_chemin.render(directory="/home/onyxia/work/ensae-prog23/output_graphviz")
        return graphe_chemin