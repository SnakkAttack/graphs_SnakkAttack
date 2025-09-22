"""
test.py
Run Dijkstra (weighted) and BFS (unweighted hops) on a graph file.

Usage:
    python test.py data/example2.txt
"""

from graphs_snakkattack import sp
import sys


def load_graph(path: str) -> dict[int, dict[int, int]]:
    graph: dict[int, dict[int, int]] = {}
    with open(path, "rt") as f:
        f.readline()  # skip first line (count/header)
        for line in f:
            line = line.strip()
            if not line:
                continue
            s, d, w = line.split()
            s, d, w = int(s), int(d), int(w)
            # ensure both ends exist as keys (harmless for leaves)
            if s not in graph:
                graph[s] = {}
            if d not in graph:
                graph[d] = {}
            graph[s][d] = w
    return graph


def validate_weighted_paths(graph, dist, path, source=0) -> bool:
    """Check: paths start at source, end at dest, and sum of weights == dist."""
    ok = True
    for d, p in path.items():
        if not p or p[0] != source or p[-1] != d:
            print(f"[X] Dijkstra endpoints invalid for {d}: {p}")
            ok = False
            continue
        # sum edge weights
        wsum = 0
        for u, v in zip(p, p[1:]):
            if u not in graph or v not in graph[u]:
                print(f"[X] Dijkstra missing edge {u}->{v} while checking {d}")
                ok = False
                break
            wsum += graph[u][v]
        if wsum != dist[d]:
            print(f"[X] Dijkstra weight mismatch for {d}: sum {wsum} vs dist {dist[d]}")
            ok = False
    if ok:
        print("[✓] Dijkstra paths validated.")
    return ok


def validate_bfs_paths(graph, hops, bpath, source=0) -> bool:
    """Check: paths start at source, end at dest, and len-1 == hops (fewest edges)."""
    ok = True
    for d, p in bpath.items():
        if not p or p[0] != source or p[-1] != d:
            print(f"[X] BFS endpoints invalid for {d}: {p}")
            ok = False
            continue
        # count edges
        edges = 0
        for u, v in zip(p, p[1:]):
            if u not in graph or v not in graph[u]:
                print(f"[X] BFS missing edge {u}->{v} while checking {d}")
                ok = False
                break
            edges += 1
        if edges != hops[d]:
            print(f"[X] BFS hop mismatch for {d}: edges {edges} vs hops {hops[d]}")
            ok = False
    if ok:
        print("[✓] BFS paths validated.")
    return ok


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Use: {sys.argv[0]} graph_file")
        sys.exit(1)

    graph_file = sys.argv[1]
    graph = load_graph(graph_file)

    # ----- Dijkstra (weighted) -----
    s = 0
    dist, path = sp.dijkstra(graph, s)
    print(f"Shortest distances from {s}:")
    print(dist)
    for d in sorted(path):
        print(f"spf to {d}: {path[d]}")
    validate_weighted_paths(graph, dist, path, s)

    # ----- BFS (unweighted hops) -----
    if hasattr(sp, "bfs_shortest_hops"):
        hops, bpath = sp.bfs_shortest_hops(graph, s)
        print(f"\nUnweighted hops from {s}:")
        print(hops)
        for d in sorted(bpath):
            print(f"bfs path to {d}: {bpath[d]}  (hops={hops[d]})")
        validate_bfs_paths(graph, hops, bpath, s)
    else:
        print("\n[!] bfs_shortest_hops not found (bonus function not available).")
