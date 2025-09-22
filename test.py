'''
test.py
'''

from graphs_snakkattack import sp
import sys

def load_graph(path):
    graph = {}
    with open(path, "rt") as f:
        f.readline()  # skip first line
        for line in f:
            line = line.strip()
            if not line:
                continue
            s, d, w = line.split()
            s, d, w = int(s), int(d), int(w)
            # ensure both ends exist as keys
            if s not in graph:
                graph[s] = {}
            if d not in graph:
                graph[d] = {}
            graph[s][d] = w
    return graph

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Use: {sys.argv[0]} graph_file")
        sys.exit(1)

    graph = load_graph(sys.argv[1])
    s = 0
    dist, path = sp.dijkstra(graph, s)
    print(f"Shortest distances from {s}:")
    print(dist)
    for d in sorted(path):
        print(f"spf to {d}: {path[d]}")
