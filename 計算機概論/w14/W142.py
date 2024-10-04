# # Figure 14-7 on page 294
class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name


class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self._src = src
        self._dest = dest

    def get_source(self):
        return self._src

    def get_destination(self):
        return self._dest

    def __str__(self):
        return self._src.get_name() + "->" + self._dest.get_name()


class Weighted_edge(Edge):
    def __init__(self, src, dest, weight=1.0):
        """Assumes src and dest are nodes, weight a number"""
        self._src = src
        self._dest = dest
        self._weight = weight

    def get_weight(self):
        return self._weight

    def __str__(self):
        return f"{self._src.get_name()}->({self._weight})" + f"{self._dest.get_name()}"


# # Figure 14-8 on page 296


class Digraph(object):
    # nodes is a list of the nodes in the graph
    # edges is a dict mapping each node to a list of its children
    def __init__(self):
        self._nodes = []
        self._edges = {}

    def add_node(self, node):
        if node in self._nodes:
            raise ValueError("Duplicate node")
        else:
            self._nodes.append(node)
            self._edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self._nodes and dest in self._nodes):
            raise ValueError("Node not in graph")
        self._edges[src].append(dest)

    def children_of(self, node):
        return self._edges[node]

    def has_node(self, node):
        return node in self._nodes

    def __str__(self):
        result = ""
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src.get_name() + "->" + dest.get_name() + "\n"
        return result[:-1]  # omit final newline


class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)


# # Figure 14-9 on page 299


def print_path(path):
    """Assumes path is a list of nodes"""
    result = ""
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + "->"
    return result


def DFS(graph, start, end, path, shortest, to_print=False):
    """Assumes graph is a Digraph; start and end are nodes;
       path and shortest are lists of nodes
    Returns a shortest path from start to end in graph"""
    path = path + [start]
    if to_print:
        print("Current DFS path:", print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:  # avoid cycles
            if shortest == None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest, to_print)
                if new_path != None:
                    shortest = new_path
    return shortest


def shortest_path(graph, start, end, to_print=False):
    """Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, to_print)


# # Figure 14-10 on page 301


def test_SP():
    nodes = []
    for name in range(6):  # Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[1], nodes[2]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[0]))
    g.add_edge(Edge(nodes[3], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[0]))
    sp = shortest_path(g, nodes[0], nodes[5], to_print=True)
    print("Shortest path found by DFS:", print_path(sp))
    sp = BFS(g, nodes[0], nodes[5], to_print=True)
    print("Shortest path found by BFS:", print_path(sp))


# # Figure 14-11 on page 303


def BFS(graph, start, end, to_print=False):
    """Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph"""
    init_path = [start]
    path_queue = [init_path]
    while len(path_queue) != 0:
        # Get and remove oldest element in path_queue
        tmp = path_queue.pop(0)
        if to_print:
            print("Current BFS path:", print_path(tmp))
        last_node = tmp[-1]
        if last_node == end:
            return tmp
        for nd in graph.children_of(last_node):
            if nd not in tmp:
                np = tmp + [nd]
                path_queue.append(np)
    return None


test_SP()
