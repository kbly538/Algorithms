class Dijkstra:

    def __init__(self, data):
        self.data = data
        self.vertices, self.graph = self._parse_data()

    # utility function to parse data into vertices and graph
    def _parse_data(self):
        with open(self.data, "r+") as data:
            vertices = set()
            graph = dict()
            nodes = data.readlines()
            for node in nodes:
                from_, to_, weight = node.strip().split()
                vertices.add(from_)
                if from_ not in graph:
                    graph[from_] = {to_: float(weight)}
                else:
                    graph[from_].update({to_: float(weight)})

            return vertices, graph

    def find_route(self, start, end):
        unvisited = {vertex: float('inf') for vertex in self.vertices}
        unvisited[start] = 0
        visited = {}
        parents = {}
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)
            for neighbor, dist in self.graph.get(min_vertex).items():
                if neighbor in visited:
                    continue
                new_distance_to_neighbor = unvisited[min_vertex] + dist
                if new_distance_to_neighbor < unvisited[neighbor]:
                    unvisited[neighbor] = new_distance_to_neighbor
                    parents[neighbor] = min_vertex

            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)

            if min_vertex == end:
                break
        print(f"Shortest path to {end} from {start} is {visited[end]}")


d = Dijkstra("shortest_path_sample_data.txt")  # directed graph
d.find_route("2", "4")



""" 
SAMPLE DATA
data =  4 5 0.35
        5 4 0.35
        4 7 0.37
        5 7 0.28
        7 5 0.28
        5 1 0.32
        0 4 0.38
        0 2 0.26
        7 3 0.39
        1 3 0.29
        2 7 0.34
        6 2 0.40
        3 6 0.52
        6 0 0.58
        6 4 0.93
"""

