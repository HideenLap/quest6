from collections import deque
import heapq


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, start, end, weight):
        self.adj_matrix[start][end] = weight
        self.adj_matrix[end][start] = weight

    def display(self):
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))

    def bfs(self, start):
        visited = [False] * self.num_vertices
        queue = deque([start])
        visited[start] = True

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=' ')

            for neighbor in range(self.num_vertices):
                if self.adj_matrix[current_vertex][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs(self, start, visited):
        visited[start] = True
        print(start, end=' ')

        for neighbor in range(self.num_vertices):
            if self.adj_matrix[start][neighbor] == 1 and not visited[neighbor]:
                self.dfs(neighbor, visited)

    def dfs_traversal(self):
        visited = [False] * self.num_vertices
        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                self.dfs(vertex, visited)

    def has_cycle(self):
        visited = [False] * self.num_vertices

        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                if self.dfs_has_cycle(vertex, visited, parent=-1):  # -1 represents no parent for the first node
                    return True

        return False

    def dfs_has_cycle(self, current_vertex, visited, parent):
        visited[current_vertex] = True

        for neighbor in range(self.num_vertices):
            if self.adj_matrix[current_vertex][neighbor] == 1:
                if not visited[neighbor]:
                    if self.dfs_has_cycle(neighbor, visited, current_vertex):
                        return True
                elif parent != neighbor:  # If the neighbor is visited and not the parent, there is a cycle
                    return True

        return False

    def shortest_path(self, start, end):
        if start == end:
            return [start]

        visited = [False] * self.num_vertices
        queue = deque([(start, [start])])
        visited[start] = True

        while queue:
            current_vertex, path_so_far = queue.popleft()

            for neighbor in range(self.num_vertices):
                if self.adj_matrix[current_vertex][neighbor] == 1 and not visited[neighbor]:
                    new_path = path_so_far + [neighbor]

                    if neighbor == end:
                        return new_path

                    queue.append((neighbor, new_path))
                    visited[neighbor] = True
        return None

    def dijkstra(self, start, end):
        heap = [(0, start)]
        visited = set()

        while heap:
            current_cost, current_vertex = heapq.heappop(heap)

            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            if current_vertex == end:
                path = self.reconstruct_path(start, end, visited)
                return current_cost, path

            for neighbor, weight in enumerate(self.adj_matrix[current_vertex]):
                if weight > 0 and neighbor not in visited:
                    heapq.heappush(heap, (current_cost + weight, neighbor))

        return float('inf'), []

    def reconstruct_path(self, start, end, visited):
        path = [end]
        current_vertex = end

        while current_vertex != start:
            for neighbor, weight in enumerate(self.adj_matrix[current_vertex]):
                if weight > 0 and neighbor in visited:
                    path.append(neighbor)
                    current_vertex = neighbor
                    break

        return list(reversed(path))

    def kosaraju_scc(self):
        stack = []
        visited = set()

        def dfs_first_pass(vertex):
            visited.add(vertex)
            for neighbor in range(self.num_vertices):
                if self.adj_matrix[vertex][neighbor] == 1 and neighbor not in visited:
                    dfs_first_pass(neighbor)
            stack.append(vertex)

        for vertex in range(self.num_vertices):
            if vertex not in visited:
                dfs_first_pass(vertex)

        transposed_graph = [[self.adj_matrix[j][i] for j in range(self.num_vertices)] for i in range(self.num_vertices)]

        visited.clear()
        strongly_connected_components = []

        def dfs_second_pass(vertex, component):
            visited.add(vertex)
            component.append(vertex)
            for neighbor in range(self.num_vertices):
                if transposed_graph[vertex][neighbor] == 1 and neighbor not in visited:
                    dfs_second_pass(neighbor, component)

        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                component = []
                dfs_second_pass(current_vertex, component)
                strongly_connected_components.append(component)

        return strongly_connected_components


