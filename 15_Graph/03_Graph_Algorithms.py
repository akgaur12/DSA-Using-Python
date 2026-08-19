"""
===========================================================
Weighted Graph Algorithms in Python
===========================================================

Implements the classic shortest-path and minimum-spanning-tree
algorithms, operating on an adjacency list of the form
`{vertex: [(neighbor, weight), ...], ...}` — the same format
produced by the `Graph` class in `02_Graph.py`.

Algorithms:
------------
1. dijkstra(graph, source)      -> shortest distances from source.
                                    O((V + E) log V). Non-negative
                                    weights only.
2. bellman_ford(vertices, edges, source)
                                 -> shortest distances from source.
                                    O(V * E). Handles negative
                                    weights; detects negative cycles.
3. DisjointSet                  -> Union-Find with path compression
                                    and union by rank. O(alpha(N))
                                    per operation (near O(1)).
4. kruskal_mst(vertices, edges) -> Minimum Spanning Tree via
                                    Disjoint Set. O(E log E).
5. prim_mst(graph, start)       -> Minimum Spanning Tree via a
                                    min-heap. O(E log V).

===========================================================
"""

import heapq


# --------------------------------------------------------
# Dijkstra's Algorithm (single-source shortest path)
# --------------------------------------------------------
def dijkstra(graph, source):
    """Shortest distance from `source` to every reachable vertex.
    Requires non-negative edge weights. O((V + E) log V).
    """
    distances = {vertex: float("inf") for vertex in graph}
    distances[source] = 0
    visited = set()
    min_heap = [(0, source)]

    while min_heap:
        dist, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            new_dist = dist + weight
            if new_dist < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return distances


# --------------------------------------------------------
# Bellman-Ford Algorithm (handles negative weights)
# --------------------------------------------------------
def bellman_ford(vertices, edges, source):
    """Shortest distance from `source` to every vertex.
    `edges` is a list of (u, v, weight) directed edges.
    Handles negative weights; raises ValueError if a negative
    weight cycle is reachable from `source`. O(V * E).
    """
    distances = {vertex: float("inf") for vertex in vertices}
    distances[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # One more pass: if any distance can still be improved, there's
    # a negative-weight cycle reachable from the source.
    for u, v, weight in edges:
        if distances[u] != float("inf") and distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return distances


# --------------------------------------------------------
# Disjoint Set / Union-Find (used by Kruskal's MST)
# --------------------------------------------------------
class DisjointSet:
    """Union-Find with path compression + union by rank.
    Near-O(1) amortized `find`/`union`.
    """

    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing x and y. Returns False if they
        were already in the same set (i.e. adding edge (x, y) would
        create a cycle).
        """
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True


# --------------------------------------------------------
# Kruskal's Algorithm (Minimum Spanning Tree)
# --------------------------------------------------------
def kruskal_mst(vertices, edges):
    """Minimum Spanning Tree via Kruskal's algorithm.
    `edges` is a list of (u, v, weight) undirected edges.
    Returns (mst_edges, total_weight). O(E log E).
    """
    dsu = DisjointSet(vertices)
    mst_edges = []
    total_weight = 0

    for u, v, weight in sorted(edges, key=lambda e: e[2]):
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight

    return mst_edges, total_weight


# --------------------------------------------------------
# Prim's Algorithm (Minimum Spanning Tree)
# --------------------------------------------------------
def prim_mst(graph, start):
    """Minimum Spanning Tree via Prim's algorithm, using a min-heap.
    `graph` is an adjacency list {u: [(v, weight), ...]}.
    Returns (mst_edges, total_weight). O(E log V).
    """
    visited = {start}
    mst_edges = []
    total_weight = 0
    min_heap = [(weight, start, neighbor) for neighbor, weight in graph.get(start, [])]
    heapq.heapify(min_heap)

    while min_heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(min_heap)
        if v in visited:
            continue
        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight += weight

        for neighbor, edge_weight in graph.get(v, []):
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, v, neighbor))

    return mst_edges, total_weight


# --------------------------------------------------------
# Example Usage
# --------------------------------------------------------
if __name__ == "__main__":
    print("--- Dijkstra's Algorithm ---")
    #        (2)      (1)
    #   A --------B--------C
    #   |         |
    #  (4)       (7)
    #   |         |
    #   D---------+
    weighted_graph = {
        "A": [("B", 2), ("D", 4)],
        "B": [("A", 2), ("C", 1), ("D", 7)],
        "C": [("B", 1)],
        "D": [("A", 4), ("B", 7)],
    }
    print(dijkstra(weighted_graph, "A"))
    # {'A': 0, 'B': 2, 'C': 3, 'D': 4}

    print("\n--- Bellman-Ford Algorithm (with a negative edge) ---")
    vertices = ["A", "B", "C", "D"]
    directed_edges = [
        ("A", "B", 4),
        ("A", "C", 5),
        ("B", "D", -2),
        ("C", "D", 3),
    ]
    print(bellman_ford(vertices, directed_edges, "A"))
    # {'A': 0, 'B': 4, 'C': 5, 'D': 2}

    print("\n--- Kruskal's MST ---")
    mst_vertices = ["A", "B", "C", "D"]
    undirected_edges = [
        ("A", "B", 2), ("A", "D", 4),
        ("B", "C", 1), ("B", "D", 7),
    ]
    edges, weight = kruskal_mst(mst_vertices, undirected_edges)
    print("MST edges:", edges, "| Total weight:", weight)
    # MST edges: [('B', 'C', 1), ('A', 'B', 2), ('A', 'D', 4)] | Total weight: 7

    print("\n--- Prim's MST ---")
    edges, weight = prim_mst(weighted_graph, "A")
    print("MST edges:", edges, "| Total weight:", weight)
    # MST edges: [('A', 'B', 2), ('B', 'C', 1), ('A', 'D', 4)] | Total weight: 7
