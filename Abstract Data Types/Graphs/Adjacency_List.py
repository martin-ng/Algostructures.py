class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, nodes, is_directed=False):
        self.nodes = nodes
        self.is_directed = is_directed
        self.adjacency_list = {}

        for node in nodes:
            self.adjacency_list[node] = []

    def print_list(self):
        for node in self.nodes:
            print(node, '->', self.adjacency_list[node])

    def size_nodes(self, node):
        return len(self.adjacency_list[node])

    def add_edge(self, u, v):
        if self.is_directed == False:
            self.adjacency_list[v].append(u)
        self.adjacency_list[u].append(v)

    def traversal(self, node):
        

if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E']
    graph = Graph(nodes, is_directed=True)

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('D', 'E')
    graph.print_list()
    print(graph.size_nodes('C'))
