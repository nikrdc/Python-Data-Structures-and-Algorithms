from PriorityQueue import PriorityQueue

class Graph(object):
    """
    A graph (directed or undirected) represented by an adjacency matrix (a list 
    of lists). If a link exists between nodes a and b, the value of 
    self.adj_matrix[i][j] = True, where i and j are the indices of a and b in 
    the first row and column of the adjacency matrix. 

            DC      SF      NYC
    DC      False   True    False
    SF      False   False   True
    NYC     True    False   False

    In the adjacency matrix above, links exist:
        - from DC to NYC
        - from SF to DC
        - from NYC to SF

    If the graph is weighted, True values will be replaced with weights. 
    """
    def __init__(self, directed=False, weighted=False, nodes=[]):
        self.directed = directed
        self.weighted = weighted
        self.adj_matrix = [[False for i in xrange(len(nodes)+1)] for i in xrange(len(nodes)+1)]
        for i in xrange(len(nodes)):
            self.adj_matrix[0][i+1] = nodes[i]
            self.adj_matrix[i+1][0] = nodes[i]

    def __repr__(self):
        str_matrix = ''
        for i in xrange(len(self.adj_matrix)):
            for adj_list in self.adj_matrix:
                str_matrix = str_matrix + str(adj_list[i]) + '\t'
            str_matrix = str_matrix + '\n'
        return str_matrix

    def indices(self, node_a, node_b):
        """
        Returns the adjancency matrix indices of the two given nodes. indices
        need to be switched to handle undirected nodes.  
        """
        return self.adj_matrix[0].index(node_a), self.adj_matrix[0].index(node_b)

    def add_link(self, node_a, node_b, weight=True):
        index_a, index_b = self.indices(node_a, node_b)
        self.adj_matrix[index_a][index_b] = weight
        if not self.directed:
            self.adj_matrix[index_b][index_a] = weight

    def delete_link(self, node_a, node_b):
        index_a, index_b = self.indices(node_a, node_b)
        self.adj_matrix[index_a][index_b] = False
        if not self.directed:
            self.adj_matrix[index_b][index_a] = False

    def link_exist(self, node_a, node_b):
        """
        Returns whether a link exists between the two given nodes. 
        """
        index_a, index_b = self.indices(node_a, node_b)
        if self.adj_matrix[index_a][index_b]:
            return True
        else:
            return False

    def link_weight(self, node_a, node_b):
        """
        Returns the weight of a link between the two given nodes.  
        """
        index_a, index_b = self.indices(node_a, node_b)
        if self.link_exist(node_a, node_b):
            return self.adj_matrix[index_a][index_b]
        else:
            print "no link"
            # raise exception

    def add_node(self, node):
        self.adj_matrix.append([False for i in xrange(len(self.adj_matrix[0]))])
        self.adj_matrix[-1][0] = node
        for adj_list in self.adj_matrix:
            adj_list.append(False)
        self.adj_matrix[0][-1] = node

    def delete_node(self, node):
        del_index = self.adj_matrix[0].index(node)
        del self.adj_matrix[del_index]
        for adj_list in self.adj_matrix:
            del adj_list[del_index]

    def linked(self, node):
        """
        Returns a list of nodes linked to the given node. 
        """
        return [dst for dst in self.adj_matrix[0] if dst and self.link_exist(node, dst)]

    def dfs(self, start):
        """
        Uses the inner_dfs function to recursively traverse the Graph from 
        start. Includes a list of visited nodes to prevent traversing cycles. 
        """
        visited = []
        def inner_dfs(node):
            visited.append(node)
            linked = self.linked(node)
            for dst in linked:
                if dst in visited:
                    print 'Cycle Detected'
                else:
                    inner_dfs(dst)
        inner_dfs(start)
        return visited

    def bfs(self, start, min_distance=False):
        """
        This breadth-first search function can also be used to return minimum 
        distances from start if the graph is unweighted. Uses a Python list as 
        a queue to traverse nodes by distance from root. 
        """
        queue = []
        queue.append(start)
        distances = [0]
        while queue:
            node = queue[0]
            linked = self.linked(node)
            distance = distances[0]
            distances += [distance+1 for dst in linked]    
            queue += linked
            del queue[0]
            del distances[0]
            if min_distance:
                print node, distance
            else:
                print node

    def shortest_path(self, target):
        """
        Uses Dijkstra's algorithm to return the shortest paths between the 
        target and all other nodes in the graph.
        """
        if not self.weighted:
            print "Graph is not weighted; redirecting to BFS"
            return self.bfs(target, min_distance=True)
        distances_pq = PriorityQueue("min")
        distances_dict = {} 
        unvisited = []
        for node in self.adj_matrix[0]:
            if node == target:
                distances_pq.enqueue(0, node)
                distances_dict[node] = 0
            elif node != False:
                distances_pq.enqueue(float('inf'), node)
                distances_dict[node] = float('inf')
            else:
                continue
            unvisited.append(node)
        while unvisited:
            min_distance, min_node = distances_pq.dequeue()
            if min_node not in unvisited:
                continue
            neighbors = self.linked(min_node)
            for neighbor in neighbors:
                neighbor_distance = min(distances_dict[neighbor], 
                                        min_distance + self.link_weight(min_node, neighbor))
                if neighbor_distance != distances_dict[neighbor]:
                   distances_dict[neighbor] = neighbor_distance
                   distances_pq.enqueue(neighbor_distance, neighbor)
            unvisited.remove(min_node)
        return distances_dict

        


