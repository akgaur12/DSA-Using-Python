"""
===========================================================
Graph Implementation in Python (Adjacency List)
===========================================================

A **Graph** is represented here using an adjacency list —
a dict mapping each vertex to a list of its neighbors. This
is the standard representation for sparse graphs: O(V + E)
space instead of the O(V^2) an adjacency matrix would need.

Supported Operations:
----------------------
1. add_edge(u, v, weight=1) -> O(1), adds an edge (respects
                                the `directed` flag set at init).
2. bfs(start)               -> O(V + E), breadth-first order.
3. dfs(start)                -> O(V + E), depth-first order (recursive).
4. dfs_iterative(start)      -> O(V + E), depth-first order (stack-based).
5. count_connected_components() -> O(V + E), undirected graphs only.
6. has_cycle_undirected()    -> O(V + E)
7. has_cycle_directed()      -> O(V + E), 3-color DFS.
8. topological_sort_kahn()   -> O(V + E), BFS-based (in-degree).
9. topological_sort_dfs()    -> O(V + E), DFS-based (finish-time stack).
10. is_bipartite()           -> O(V + E), 2-coloring via BFS.

===========================================================
"""

from collections import deque


class Graph:
    """Graph backed by an adjacency list.

    Set `directed=True` at construction for a directed graph;
    defaults to undirected (each `add_edge` adds both directions).
    """

    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}

    # ----------------------------------------------------
    def add_vertex(self, v):
        """Ensure vertex v exists in the graph. O(1)."""
        self.adj.setdefault(v, [])

    # ----------------------------------------------------
    def add_edge(self, u, v, weight=1):
        """Add an edge u -> v (and v -> u if undirected). O(1)."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    # ----------------------------------------------------
    def neighbors(self, u):
        """Return the list of (neighbor, weight) pairs for u."""
        return self.adj.get(u, [])

    # ----------------------------------------------------
    def bfs(self, start):
        """Breadth-first traversal order starting at `start`. O(V + E)."""
        if start not in self.adj:
            return []
        visited = {start}
        order = []
        queue = deque([start])
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor, _ in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    # ----------------------------------------------------
    def dfs(self, start):
        """Depth-first traversal order starting at `start` (recursive). O(V + E)."""
        visited = set()
        order = []

        def _walk(node):
            visited.add(node)
            order.append(node)
            for neighbor, _ in self.adj.get(node, []):
                if neighbor not in visited:
                    _walk(neighbor)

        if start in self.adj:
            _walk(start)
        return order

    # ----------------------------------------------------
    def dfs_iterative(self, start):
        """Depth-first traversal order starting at `start`, using an
        explicit stack instead of recursion. O(V + E).
        """
        if start not in self.adj:
            return []
        visited = set()
        order = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            # Push in reverse so the first neighbor is processed first.
            for neighbor, _ in reversed(self.adj[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
        return order

    # ----------------------------------------------------
    def count_connected_components(self):
        """Number of connected components (undirected graphs). O(V + E)."""
        visited = set()
        components = 0
        for vertex in self.adj:
            if vertex not in visited:
                components += 1
                stack = [vertex]
                while stack:
                    node = stack.pop()
                    if node in visited:
                        continue
                    visited.add(node)
                    for neighbor, _ in self.adj[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
        return components

    # ----------------------------------------------------
    def has_cycle_undirected(self):
        """True if the undirected graph contains a cycle. O(V + E)."""
        visited = set()

        def _walk(node, parent):
            visited.add(node)
            for neighbor, _ in self.adj[node]:
                if neighbor not in visited:
                    if _walk(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True   # visited neighbor that isn't our parent -> cycle
            return False

        for vertex in self.adj:
            if vertex not in visited:
                if _walk(vertex, None):
                    return True
        return False

    # ----------------------------------------------------
    def has_cycle_directed(self):
        """True if the directed graph contains a cycle, using 3-color DFS.
        O(V + E).
        """
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {v: WHITE for v in self.adj}

        def _walk(node):
            color[node] = GRAY
            for neighbor, _ in self.adj[node]:
                if color[neighbor] == GRAY:
                    return True   # back edge -> cycle
                if color[neighbor] == WHITE and _walk(neighbor):
                    return True
            color[node] = BLACK
            return False

        for vertex in self.adj:
            if color[vertex] == WHITE:
                if _walk(vertex):
                    return True
        return False

    # ----------------------------------------------------
    def topological_sort_kahn(self):
        """Topological order via Kahn's algorithm (BFS on in-degree).
        Directed acyclic graphs only; raises ValueError on a cycle.
        O(V + E).
        """
        in_degree = {v: 0 for v in self.adj}
        for u in self.adj:
            for v, _ in self.adj[u]:
                in_degree[v] += 1

        queue = deque([v for v in in_degree if in_degree[v] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor, _ in self.adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(self.adj):
            raise ValueError("Graph has a cycle; topological sort is undefined")
        return order

    # ----------------------------------------------------
    def topological_sort_dfs(self):
        """Topological order via DFS finish-time stack.
        Directed acyclic graphs only. O(V + E).
        """
        visited = set()
        stack = []

        def _walk(node):
            visited.add(node)
            for neighbor, _ in self.adj[node]:
                if neighbor not in visited:
                    _walk(neighbor)
            stack.append(node)

        for vertex in self.adj:
            if vertex not in visited:
                _walk(vertex)
        return stack[::-1]

    # ----------------------------------------------------
    def is_bipartite(self):
        """True if vertices can be 2-colored so no edge joins two
        vertices of the same color. O(V + E).
        """
        color = {}
        for start in self.adj:
            if start in color:
                continue
            color[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor, _ in self.adj[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        return True


# --------------------------------------------------------
# Example Usage
# --------------------------------------------------------
if __name__ == "__main__":
    print("--- Undirected Graph ---")
    #   0 - 1
    #   |   |
    #   2 - 3
    g = Graph(directed=False)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)

    print("BFS from 0:", g.bfs(0))                       # [0, 1, 2, 3]
    print("DFS from 0:", g.dfs(0))                        # [0, 1, 3, 2]
    print("DFS (iterative) from 0:", g.dfs_iterative(0))  # [0, 1, 3, 2]
    print("Connected components:", g.count_connected_components())  # 1
    print("Has cycle (undirected)?", g.has_cycle_undirected())      # True
    print("Is bipartite?", g.is_bipartite())              # True

    print("\n--- Directed Acyclic Graph (DAG) ---")
    #   5 -> 0 <- 4
    #   |         |
    #   v         v
    #   2         1 <- 3 <- 4 -> 1
    dag = Graph(directed=True)
    dag.add_edge(5, 0)
    dag.add_edge(5, 2)
    dag.add_edge(4, 0)
    dag.add_edge(4, 1)
    dag.add_edge(2, 3)
    dag.add_edge(3, 1)

    print("Has cycle (directed)?", dag.has_cycle_directed())        # False
    print("Topological sort (Kahn):", dag.topological_sort_kahn())
    print("Topological sort (DFS):", dag.topological_sort_dfs())

    print("\n--- Directed graph with a cycle ---")
    cyclic = Graph(directed=True)
    cyclic.add_edge("A", "B")
    cyclic.add_edge("B", "C")
    cyclic.add_edge("C", "A")
    print("Has cycle (directed)?", cyclic.has_cycle_directed())     # True
