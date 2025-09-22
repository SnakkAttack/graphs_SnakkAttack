import sys
from heapq import heappush, heappop

def dijkstra(graph: dict[int, dict[int, int]], source: int):
    # collect all vertices (keys + neighbors)
    vertices = set(graph.keys())
    for u, nbrs in graph.items():
        vertices.update(nbrs.keys())
    if not vertices:
        return [], {}

    n = max(vertices) + 1
    dist = [sys.maxsize] * n
    dist[source] = 0

    prev: dict[int, int | None] = {source: None}  # predecessor map
    heap = [(0, source)]

    while heap:
        d_u, u = heappop(heap)
        if d_u != dist[u]:
            continue
        for v, w_uv in graph.get(u, {}).items():
            if w_uv < 0:
                raise ValueError("Dijkstra requires non-negative weights.")
            nd = d_u + w_uv
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heappush(heap, (nd, v))

    # reconstruct paths
    def build_path(d):
        if dist[d] == sys.maxsize:
            return None  # unreachable
        path = []
        cur = d
        while cur is not None:
            path.append(cur)
            cur = prev.get(cur)
        path.reverse()
        return path

    path = {d: build_path(d) for d in vertices if dist[d] != sys.maxsize}
    return dist, path




from collections import deque

def bfs_shortest_hops(graph: dict[int, dict[int, int]], source: int):
    """
    Unweighted shortest-paths (fewest edges) using BFS.

    Args:
        graph: adjacency dict {u: {v: weight, ...}, ...}  (weights ignored)
        source: starting vertex id

    Returns:
        hops: list where hops[v] = number of edges from source to v
              (sys.maxsize for unreachable)
        path: dict {v: [source, ..., v]} only for reachable v
    """
    import sys

    # Collect all vertices (keys + neighbors)
    vertices = set(graph.keys())
    for u, nbrs in graph.items():
        vertices.update(nbrs.keys())
    if not vertices:
        return [], {}

    n = max(vertices) + 1
    hops = [sys.maxsize] * n
    prev: dict[int, int | None] = {source: None}

    q = deque([source])
    hops[source] = 0

    while q:
        u = q.popleft()
        for v in graph.get(u, {}):
            if hops[v] == sys.maxsize:        # not visited
                hops[v] = hops[u] + 1
                prev[v] = u
                q.append(v)

    # Reconstruct paths for reachable vertices
    path: dict[int, list[int]] = {}
    for d in vertices:
        if hops[d] == sys.maxsize:
            continue
        cur = d
        rev = []
        while cur is not None:
            rev.append(cur)
            cur = prev.get(cur)
        path[d] = list(reversed(rev))

    return hops, path
