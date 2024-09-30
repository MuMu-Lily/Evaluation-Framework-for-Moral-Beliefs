from tqdm import tqdm

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def is_connected(self, u, v):
        visited = set()
        self.dfs(u, visited)
        return v in visited

    def dfs(self, v, visited):
        visited.add(v)
        if v in self.graph:
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited)

def find_disconnected_pairs(graph):
    disconnected_pairs = []
    vertices = list(graph.graph.keys())
    for i in tqdm(range(len(vertices))):
        for j in range(i + 1, len(vertices)):
            if not graph.is_connected(vertices[i], vertices[j]):
                disconnected_pairs.append((vertices[i], vertices[j]))
    return disconnected_pairs

def not_first():
    not_first_point = []
    not_big = [130, 249, 253, 328, 400, 450, 463, 479, 512, 550, 553, 571, 594, 629, 672, 712]
    for i in range(len(not_big)):
        for j in range(i + 1, len(not_big)):
            not_first_point.append((not_big[i], not_big[j]))
    return not_first_point

"""g = Graph(7)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 3)
g.add_edge(6, 6)

disconnected_pairs = find_disconnected_pairs(g)

print("不连通的点对数量：", len(disconnected_pairs))
print("不连通的两个点：", disconnected_pairs)"""

"""not_first_point = []
not_big = [130, 249, 253, 328, 400, 450, 463, 479, 512, 550, 553, 571, 594, 629, 672, 712]
for i in range(len(not_big)):
    for j in range(i+1, len(not_big)):
        not_first_point.append((not_big[i], not_big[j]))

print(len(not_first_point))
print(not_first_point)"""
