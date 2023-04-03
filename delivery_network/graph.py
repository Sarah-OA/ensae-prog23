""" Définition de la classe Graph 
"""

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.edges=[]
    

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
        self.edges.append([node1, node2, power_min])
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

    def trouve_la_racine(self, parent, i):
        """ on code un graphe de la manière suivante: une liste "parent" de sorte que parent[i] soit la racine de l'élément i. 
        Si un noeud est le sommet du de l'arbre, alors parent[noeud]=noeud.
        La fonction trouve_la_racine renvoie la racine de l'élément i (le sommet de l'abre couvrant de poids minimal auquel i appartient)"""
        if parent[i] == i: #i est-il racine? 
            return i #si oui, on renvoie i
        return self.trouve_la_racine(parent, parent[i]) #sinon, on renvoie la racine du parent de i
    
    def union(self, parent, rank, x, y):
        """ La fonction union permet de faire créer un trajet entre les noeuds x et y. Il modifie donc la liste parent du graphe 
        auquel x et y appartiennent pour actualiser leurs racines. Pour cela, on actualise la liste rank qui nous sert 
        à savoir quel des deux noeuds mettre en parent"""
        x_racine = self.trouve_la_racine(parent, x)
        y_racine = self.trouve_la_racine(parent, y)
        if rank[x_racine]<rank[y_racine]: #Si le rank de la racine de x est plus petit que celui de y, on prendra y parent de x
            parent[x_racine]=y_racine
        elif rank[x_racine]>rank[y_racine]: #Si le rank de la racine de x est plus grand que celui de y, on prendra x parent de y
            parent[y_racine]=x_racine
        else: #Si les racines de x et y ont le même rank, on prend arbitrairement x parent de y et on augement de rang de x
            parent[y_racine] = x_racine
            rank[x_racine] += 1   

    def kruskal(self):
        """ La fonction kruskal renvoie l'arbre couvrant de poids minimal de self."""
        mst = Graph([]) #création d'un graphe vide
        i=0
        e=0  # e compte le nombre d'arrêtes ajoutées au nouveau graphe
        liste_trajets_ranges = sorted(self.edges, key=lambda item: item[2]) #on range les arrêtes de self selon leur poids
        parent =[] 
        rank=[]
        for j in range(self.nb_nodes+1):
            parent.append(j)
            rank.append(0)
        # on initialise la liste parent représentant le nouveau graphe à [0, 1, ..., n] car au départ aucun noeuds ne sont reliés
        # donc ils sont tous racine d'eux mêmes
        # idem, rank =[0, ..., 0] car en l'absence de trajets reliant les noeurs, ils ont tous le même rang
        
        while e < (self.nb_nodes - 1) and i < len(liste_trajets_ranges): #pour un abre couvrant on veut que le nombre d'arrêtes = nombre de noeurds -1
            u, v, w = liste_trajets_ranges[i]
            i = i + 1
            x = self.trouve_la_racine(parent, u)
            y = self.trouve_la_racine(parent, v)
            #Si les racines de u et v sont identiques, alors créer un trajet entre u et v créerait un cycle
            #(en effet on pourrait trouver un trajet de sorte que u->racine de u = racine de v-> v -> u)
            if x!= y:
                #Si x et y sont différents, on rajoute un trajet entre x et y
                e = e+1
                mst.add_edge(u,v,w) # on actualise notre graphe
                mst.union(parent, rank, x, y) #on actualise les listes rank et parent représentant le nouveau graphe
        return mst

    def dfs_kruskal(self, sommet, parents, profondeurs, profondeur, deja_vu):
        """
        Parcours en profondeur d'un arbre couvrant de poids minimal, à partir d'un sommet. La fonction renvoie le dictionnaire de ses parents et profondeurs.
        """
        for voisin, puissance, distance in self.graph[sommet]: #en partant du sommet, on visite ses voisins si ceux-ci n'ont pas déjà été vus        
            if voisin not in deja_vu:
                profondeurs[voisin] = profondeur +1 #on actualise la profondeur du noeud qu'on visite
                parents[voisin]=(sommet, puissance) #on actualise le parent du noeud qu'on visite
                deja_vu.append(voisin) 
                self.dfs_kruskal(voisin, parents, profondeurs, profondeur+1, deja_vu) #ensuite, on appelle la fonction en prenant alors comme sommet
                #les voisins du sommet initial, parents et profondeurs ont été actualisés, et on incrémente la profondeur de 1 en descendant dans l'arbre

    def resultat_dfs(self):
        """
        Exécute le parcours en profondeur un d'arbre couvrant de poids minimal.
        Retourne un dictionnaire composé des éléments sommet : profondeur.
        Retourne un dictionnaire composé des éléments sommet : parent.
        """
        profondeurs = {}
        parents = {}
        #on prend arbitrairement le noeud 1 comme sommet, la profondeur initale 
        #est 0 et les dictionnaires parents et profondeurs sont vides
        profondeurs[1]=0 #on atualise la profondeur de la racine (1) à 0
        self.dfs_kruskal(1, parents, profondeurs, 0, [1]) #on applique la fonction à notre arbre ainsi qu'à nos dictionnaires qui 
        #vont être modifiés
        return (profondeurs, parents)
        
    def min_power_kruskal(self, profondeurs, parents, src, dest):
        """ La fonction renvoie une liste représentant le chemin à emprunter pour aller de src à dest ainsi que la puissance
        minimale nécessaire pour effectuer ce trajet."""
        depart = [src] #chemin parcouru depuis le départ
        arrivee = [dest] #chemin parcouru depuis l'arrivée
        a = src # le "départ"
        b = dest #l' "arrivée"
        p_min = 0 #puissance minimale pour réaliser le trajet
        while a != b: #tant que le départ et l'arrivée sont différents:
            if profondeurs[a]>profondeurs[b]: #si a est un noeud plus profond que b, on remonte au parent de a
                a,p = parents[a]
                depart.append(a) #on actualise le chemin parcouru depuis le départ
                if p>p_min: #si la puissance nécessaire à faire ce trajet est supérieure à p_min, on l'actualise
                    p_min = p
            elif profondeurs[a]<profondeurs[b]: # idem si b est un noeud plus profond que a
                b,p = parents[b]
                arrivee = [b] + arrivee
                if p>p_min:
                    p_min = p
            else: # Si les deux noeuds sont à la même profondeur, ont revient aux parents de a et de b
                a,p1 = parents[a]
                b,p2 = parents[b]
                depart.append(a) #cette fois ci les deux listes contenant le début et la fin du chemin sont actualisées
                arrivee = [b] + arrivee
                if max(p1, p2)>p_min: #on considère le max des puissances des trajets parcourus pour actualiser p_min
                    p_min = max(p1, p2)
        depart.pop()
        return (depart + arrivee, p_min)
         
    def minimiser_le_prix(self, profondeur, parents, camion, trajet, i): 
        """ trouve le camion j le moins cher pour effectuer le trajet i """
        l,a = self.min_power_kruskal(profondeur, parents, trajet[i][0], trajet[i][1])
        
        prix_min = float('inf')
        camion_choisi = 0
        for j in range(len(camion)):
            if camion[j][0]>=a:
                if camion[j][1]<prix_min:
                    prix_min = camion[j][1]
                    camion_choisi = j
        if prix_min == float('inf'):
            return None
        else:
            return camion[camion_choisi]

    def knapSack(self, profondeur, parents, B, camions, trajets, n): 
        if n==0 or B==0:
            return 0
        if camions[n]==None:
            return self.knapSack(profondeur, parents, B, camions, trajets, n-1)
        else:
            if camions[n][1]>B:
                return self.knapSack(profondeur, parents, B, camions, trajets, n-1)
            else:
                return (max(trajets[n][2] + self.knapSack(profondeur, parents, B-camions[n][1], camions, trajets, n-1),self.knapSack(profondeur, parents, B, camions, trajets, n-1)))

    def optimisation(self, profondeur, parents, camions, trajets, B):
        camions_choisis = [self.minimiser_le_prix(profondeur, parents, camions, trajets, i) for i in range(len(trajets))]
        return self.knapSack(profondeur, parents, B, camions_choisis, trajets, len(trajets)-1, [])

    def lire_trajets(self, routes):
        """
        Lit les trajets présents dans un fichier route et retourne une liste de listes [départ, arrivée, utilité].
        """
        lines = routes.readlines()
        L=[]
        for line in lines[1:len(lines)]:
            line=line.split(" ")
            trajet=[int(line[0]), int(line[1]), int(line[2])]
            L.append(trajet)
        return L

    def lire_camions(self, trucks):
        """ Lit les camions présents dans un fichier trucks et retourne une liste de listes [puissance, prix]
        """
        lines = trucks.readlines()
        L=[]
        for line in lines[1:len(lines)]:
            line=line.split(" ")
            camion=[int(line[0]), int(line[1])]
            L.append(camion)
        return L

    def greedy(self,profondeur,parents,camions,trajets,B):
            profit = 0
            resultat = []
            camions_choisis = [self.minimiser_le_prix(profondeur, parents, camions, trajets, i) for i in range(len(trajets)-1)]
            ratio = []
            for i in range(len(camions_choisis)):
                if camions_choisis != None:
                    a = camions_choisis[i][1]
                    b = trajets[i][2]
                else:
                    a=1
                    b=0
                ratio.append([b/a,i,a,b])
            ratio_range = sorted(ratio, reverse=True, key=lambda item: item[0])
            for i in range(len(ratio_range)):
                if B>0 and ratio_range[i][2]<= B:
                    B = B - ratio_range[i][2]
                    profit = profit + ratio_range[i][3]
                    resultat.append(ratio_range[i][1])
            camion_final=[]
            for i in resultat:
                camion_final.append((trajets[i],camions_choisis[i]))
            for i in resultat:
                print('le trajet ', trajets[i], 'sera réalisé par le camion ', camions_choisis[i], '\n')
            print('le profit est de ', profit,'\n')
            return (profit,camion_final)


def graph_from_file(filename):
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

