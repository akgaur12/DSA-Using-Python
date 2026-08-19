# Graphs in Python

A **Graph** is a non-linear data structure made up of a set of **vertices** (nodes) connected by a set of **edges**. Unlike a tree, a graph has no fixed root, a node can have any number of connections, and — critically — **cycles are allowed**. Graphs are the most general way to model relationships: road networks, social networks, dependency chains, web pages, and more.

---

## 1. Terminology

| Term                | Meaning                                                                 |
| -------------------- | ------------------------------------------------------------------------ |
| **Vertex (Node)**    | A single point/entity in the graph.                                     |
| **Edge**             | A connection between two vertices.                                      |
| **Degree**           | Number of edges connected to a vertex.                                  |
| **In-degree**        | (Directed graph) number of edges *coming into* a vertex.                |
| **Out-degree**       | (Directed graph) number of edges *going out of* a vertex.               |
| **Path**             | A sequence of vertices connected by edges, no repeated vertex.          |
| **Cycle**            | A path that starts and ends at the same vertex.                         |
| **Connected Graph**  | Every vertex is reachable from every other vertex (undirected).         |
| **Connected Component** | A maximal set of vertices all reachable from one another.            |
| **Weighted Graph**   | Each edge carries a cost/weight.                                        |
| **Unweighted Graph** | All edges are considered equal (weight = 1).                            |
| **Directed Graph (Digraph)** | Edges have a direction: `u -> v` does not imply `v -> u`.       |
| **Undirected Graph** | Edges are bidirectional: `u — v` implies `v — u`.                       |
| **DAG**              | **D**irected **A**cyclic **G**raph — directed, with no cycles.          |

### Visual Representation

```text
Undirected graph:              Directed graph:

    1 --- 2                        1 --> 2
    |     |                        ^     |
    |     |                        |     v
    3 --- 4                        4 <-- 3
```

> A **Tree** is simply a connected, acyclic, undirected graph with exactly `N - 1` edges for `N` nodes — i.e. a graph is the generalization, a tree is a special case.

---

## 2. Types of Graphs

- **Undirected / Directed** — see terminology above.
- **Weighted / Unweighted** — whether edges carry a cost.
- **Cyclic / Acyclic** — whether a cycle exists.
- **Connected / Disconnected** — whether every vertex is reachable from every other.
- **Complete Graph** — every pair of vertices is directly connected.
- **Bipartite Graph** — vertices can be split into two sets such that every edge connects a vertex in one set to a vertex in the other (no edge within the same set).
- **DAG (Directed Acyclic Graph)** — used to model dependencies (build systems, task scheduling, course prerequisites).

---

## 3. Representing a Graph

There are three common ways to store a graph; the trade-off is **space vs. edge-lookup speed**.

### a) Adjacency Matrix

A `V x V` 2D array where `matrix[u][v] = 1` (or the weight) if an edge exists between `u` and `v`.

```python
# 4 vertices (0-3), undirected, unweighted
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
```

- **Space**: O(V²) — wasteful for sparse graphs (few edges).
- **Edge lookup** `is_edge(u, v)`: O(1).
- **Iterating all neighbors of u**: O(V), even if u has only 1 neighbor.

### b) Adjacency List (most common)

Each vertex stores a list of its neighbors. This repo's implementation (`02_Graph.py`) uses this representation.

```python
# same graph as above
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2],
}
```

- **Space**: O(V + E) — efficient for sparse graphs (most real-world graphs are sparse).
- **Edge lookup** `is_edge(u, v)`: O(degree(u)) — O(1) if using a set instead of a list.
- **Iterating all neighbors of u**: O(degree(u)) — exactly the work needed, no waste.

### c) Edge List

A flat list of `(u, v)` or `(u, v, weight)` tuples. Simple to build and sort, commonly used as the *input* format for algorithms like Kruskal's MST which need to process edges sorted by weight.

```python
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
```

### Representation Trade-off Summary

| Representation      | Space   | Check if edge (u,v) exists | Iterate neighbors of u |
| --------------------- | --------- | ----------------------------- | -------------------------- |
| Adjacency Matrix      | O(V²)     | O(1)                           | O(V)                        |
| Adjacency List        | O(V + E)  | O(degree(u))                   | O(degree(u))                |
| Edge List             | O(E)      | O(E)                           | O(E)                        |

---

## 4. Graph Traversals

Both traversals visit every reachable vertex exactly once, but explore in a different order — this difference is why each fits different problems.

Example graph (undirected, adjacency list):

```text
0 — 1        0: [1, 2]
|   |        1: [0, 3]
2 — 3        2: [0, 3]
             3: [1, 2]
```

### a) Breadth-First Search (BFS) — level by level, using a Queue

Explores all neighbors at the current distance before moving further out. **Guarantees the shortest path in an unweighted graph.**

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```

Output starting at `0`: `[0, 1, 2, 3]`

### b) Depth-First Search (DFS) — go as deep as possible, using a Stack (or recursion)

```python
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited, order = set(), []
    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order
```

Output starting at `0`: `[0, 1, 3, 2]`

### Traversal Complexity

| Traversal | Time (adjacency list) | Space          |
| --------- | ------------------------ | ---------------- |
| BFS       | O(V + E)                  | O(V) — queue + visited set |
| DFS       | O(V + E)                  | O(V) — recursion/stack + visited set |

---

## 5. Cycle Detection

- **Undirected graph**: during DFS, if you reach an already-visited vertex that is **not** the immediate parent, a cycle exists. (Alternatively: Union-Find — if two vertices of an edge already share the same set, adding that edge creates a cycle.)
- **Directed graph**: DFS with 3 states per vertex — `WHITE` (unvisited), `GRAY` (in the current recursion path), `BLACK` (fully processed). If DFS reaches a `GRAY` vertex, a cycle exists (a "back edge").

---

## 6. Topological Sort (DAGs only)

A **topological order** is a linear ordering of vertices such that for every directed edge `u -> v`, `u` comes before `v`. Only possible for a **DAG** (a cycle would create a contradiction). Used for build/task scheduling, course prerequisite ordering, etc.

Two standard approaches:
- **Kahn's Algorithm (BFS-based)**: repeatedly remove vertices with in-degree 0.
- **DFS-based**: run DFS, push each vertex onto a stack *after* all its descendants are processed, then reverse the stack.

---

## 7. Shortest Path & Minimum Spanning Tree Algorithms

| Algorithm       | Problem                                     | Handles negative weights? | Time Complexity          |
| ---------------- | --------------------------------------------- | ---------------------------| --------------------------- |
| BFS              | Shortest path, **unweighted** graph            | N/A                          | O(V + E)                      |
| Dijkstra         | Shortest path from one source, weighted        | No                           | O((V + E) log V) with a heap  |
| Bellman-Ford     | Shortest path from one source, weighted        | Yes (detects negative cycles) | O(V · E)                    |
| Prim's           | Minimum Spanning Tree                          | —                            | O(E log V) with a heap        |
| Kruskal's        | Minimum Spanning Tree                          | —                            | O(E log E) (sorting edges)    |

*(Full implementations of Dijkstra, Bellman-Ford, Prim's, and Kruskal's — with a Union-Find/Disjoint-Set helper — are in [`03_Graph_Algorithms.py`](./03_Graph_Algorithms.py).)*

---

## 8. Applications

- **Maps & navigation** (shortest route — Dijkstra).
- **Social networks** (friend suggestions, community detection).
- **Web crawling / PageRank** (the web as a directed graph).
- **Build systems / task scheduling** (topological sort over a dependency DAG).
- **Network routing protocols**.
- **Compiler dependency resolution**.
- **Recommendation engines** (bipartite graphs of users ↔ items).

---

## 9. Graph vs Tree

| Feature            | Tree                          | Graph                              |
| ------------------- | -------------------------------| --------------------------------------|
| Cycles              | Never                           | May or may not have cycles            |
| Root                | Exactly one                     | No inherent root                      |
| Edges (connected)   | Exactly `N - 1` for N nodes      | 0 to `N*(N-1)/2` (undirected)         |
| Traversal           | DFS (pre/in/post), BFS          | DFS, BFS — needs a `visited` set (cycles!) |

> Traversing a graph **without** a `visited` set can infinite-loop the moment a cycle exists — this is the single biggest bug source when adapting tree-traversal code to graphs.

---

## ✅ Summary

- A graph generalizes a tree: vertices + edges, **cycles allowed**, no fixed root.
- **Adjacency list** is the standard representation for sparse, real-world graphs — O(V + E) space vs. O(V²) for a matrix.
- **BFS** finds shortest paths in unweighted graphs; **DFS** is the workhorse for cycle detection, topological sort, and connected components.
- For weighted shortest paths use **Dijkstra** (non-negative weights) or **Bellman-Ford** (handles negative weights); for **Minimum Spanning Trees** use **Prim's** or **Kruskal's**.
- Always track `visited` vertices — graphs, unlike trees, can contain cycles.
