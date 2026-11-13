r"""Assessment 3.3 - Graph for the last name BACULI.

Edges: B-A, B-C, A-U, A-L, C-L, C-I

Level 0:           B
                 /   \
Level 1:        A     C
               / \   / \
Level 2:      U   L-+   I

When there is a choice of neighbor, letters are visited in alphabetical order.
"""
from collections import deque


def build_graph(edges):
    """Build an undirected graph as an adjacency list (dictionary)."""
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    for vertex in graph:
        graph[vertex].sort()  # alphabetical order
    return graph


def bfs(graph, start):
    """Breadth-First Search: visit all neighbors first, using a queue."""
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def dfs(graph, vertex, visited=None, order=None):
    """Depth-First Search: go as deep as possible, then backtrack (recursion)."""
    if visited is None:
        visited, order = set(), []
    visited.add(vertex)
    order.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order


if __name__ == "__main__":
    edges = [("B", "A"), ("B", "C"), ("A", "U"), ("A", "L"), ("C", "L"), ("C", "I")]
    graph = build_graph(edges)
    print("Graph for: BACULI")
    print("Adjacency list:", graph)
    print("BFS:", " - ".join(bfs(graph, "B")))
    print("DFS:", " - ".join(dfs(graph, "B")))
