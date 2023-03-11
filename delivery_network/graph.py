class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 
        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node1 in self.graph:
            self.graph[node1].append([node2, power_min, dist])
        else: 
            self.graph[node1]=[[node2, power_min, dist]]
            self.nb_nodes+=1
        if node2 in self.graph:
            self.graph[node2].append([node1, power_min, dist])
        else: 
            self.graph[node2]=[[node1, power_min, dist]]
            self.nb_nodes+=1
        self.nb_edges+=1

    
    def parcours_en_profondeur(self, node, seen=None):
        """
        Parcourt en profondeur un graphe et retourne la liste des sommets connexes dans la liste seen.
        Pour chaque node qui n'est pas dans la liste seen, recherche ses voisins.
        Si le voisin n'est pas déjà dans la liste seen, l'ajoute et parcourt récursivement ses voisins.
        """
        if seen is None:
            seen=[]
        if node not in seen:
            seen.append(node)
            unseen=[]
            for t in self.graph[node]:
                if t[0] not in seen:
                    unseen.append(t[0])
            for node in unseen:
                self.parcours_en_profondeur(node, seen)
        return seen

    def connected_components(self):
        """
        Retourne une liste de composantes connexes d'un graphe. 
        """
        ccs=[]
        for node in self.nodes:
            if ccs==[]:        
                ccs.append(self.parcours_en_profondeur(node))
            else:
                a=True
                for cc in ccs:
                    if node in cc:
                        a=False
                if a:
                    ccs.append(self.parcours_en_profondeur(node))
        return ccs

    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
        
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        i = 0
        while self.get_path_with_power(src, dest, 2**i) == None: 
            # On teste les puissances de 2 jusqu'à ce qu'il existe un chemin entre src et dest avec une puissance=2**i
            i = i + 1
        """
            Recherche binaire : on pose d'abord en bornes la puissance de 2 trouvée précedemment et la puissance inférieure.
            On pose c le milieu du segment [a,b] et on teste si la puissance c permet de trouver un chemin. 
            Si oui, on pose b=c, sinon on pose a=c+1. On s'arrête quand le segment [a,b] est nul et on retourne b comme puissance
            minimale.
        """
        a = 2**(i-1)
        b = 2**i
        c=0
        while b>a:
            c=(a+b)//2
            if self.get_path_with_power(src, dest, c)==None:
                a=c+1
            else:
                b=c
        return b, self.get_path_with_power(src, dest, b)
        
    def get_path_with_power(self, src, dest, power):
        """
        Teste s'il existe un chemin possible entre src et dest avec la puissance power.
        """
        file = [(src,[src])] # Crée une file avec les sommets à examiner et le chemin qui se construit entre src et dest
        chemins = []
        deja_vu =[]
        while file != []:
            sommet, chemin = file.pop(0) # retire le premier élément de la file et sépare le sommet et le chemin
            deja_vu.append(sommet)
            for t in self.graph[sommet]: # parcourt les voisins du sommet 
                if t[0] not in deja_vu :
                    if t[1]<= power: # vérifie que l'arète peut être parcourue avec la puissance du camion
                        if t[0] == dest:
                            chemins.append(chemin + [t[0]])
                            return chemins[0]
                            file=[] # retourne le chemin entre src et dest et vide la file pour sortir de la boucle
                        else:
                            file.append((t[0], chemin + [t[0]])) # ajoute le voisin à la file à examiner et au chemin en construction 
        return None

def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.
    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.
    Parameters: 
    -----------
    filename: str
        The name of the file
    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    file = open(filename,'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    g=Graph([i for i in range(1, int(lines.pop(0).split()[0])+1)])
    for line in lines:
        words= line.split()
        if len(words)==3:
            g.add_edge(int(words[0]), int(words[1]), int(words[2]))
        else:
            g.add_edge(int(words[0]), int(words[1]), int(words[2]), int(words[3]))
    return(g)

    def kruskal(g):
        g_mst=0
        return g_mst
    
    def get_path_with_power_kruskal(self, src, dest, power):
        """
        Adaptation de la fonction get_path_with_power à l'arbre couvrant de poids minimal.
        """
        return 'coucou'
    
    def min_power_kruskal(self, src, dest):
        """
        Adaptation de la fonction min_power à l'arbre couvrant de poids minimal.
        On utilise la fonction get_path_with_power_kruskal plutôt que la fonction get_path_with_power.
        """
        i = 0
        while self.get_path_with_power_kruskal(src, dest, 2**i) == None:
            i = i + 1
        a = 2**(i-1)
        b = 2**i
        c=0
        while b>a:
            c=(a+b)//2
            if self.get_path_with_power_kruskal(src, dest, c)==None:
                a=c+1
            else:
                b=c
        return b, self.get_path_with_power_kruskal(src, dest, b)