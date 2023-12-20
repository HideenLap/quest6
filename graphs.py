class Vertex:
    """Класс вершин"""

    def __init__(self, x):
        """
        Не вызывается на прямую, а вызывается через Graph.insert_vertex(x)
        :param x:
        """
        self._element = x

    def element(self):
        """Просмотр элемента вершины"""
        return self._element

    def __hash__(self):  # позволяет вершине быть ключем словаря
        return hash(id(self))


class Edge:
    def __init__(self, u, v, x):
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        return (self._origin, self._destination)

    def opposite(self, v):
        return self._destination if v is self._origin else self._origin

    def element(self):
        return self._element

    def __hash__(self):
        return hash(self._origin, self._destination)


class Graph:
    def __init__(self, directed=False):
        """Создание пустого графа"""
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edges(self, u, v, x=None):
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e


graph = Graph(directed=True)
graph.insert_vertex("A")
graph.insert_vertex("B")
graph.insert_vertex("C")
graph.insert_vertex("D")
print(graph._incoming["A"])

