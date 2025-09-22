# graphs_snakkattack

A Python library of graph algorithms.  
Implements **Dijkstra’s shortest paths** (weighted graphs) and **BFS shortest hops** (unweighted graphs) using a simple adjacency-dictionary representation.

This package was built for a Software Development Methods assignment to practice **Python packaging**, **branch management**, and **pip installation**.

## Features

- Dijkstra’s algorithm for weighted shortest paths  
- BFS (Breadth-First Search) for unweighted shortest hops (bonus)  
- Simple adjacency-dict graph representation (`{u: {v: weight}}`)  
- Installable with `pip`  
- Example CLI runner with `test.py`  

## Installation

### From GitHub

pip install graphs_snakkattack

### Local Development

git clone https://github.com/SnakkAttack/graphs_SnakkAttack.git
cd graphs_SnakkAttack
pip install -e .

## Usage

### In Python

from graphs_snakkattack import dijkstra, bfs_shortest_hops

graph = {
    0: {1: 5, 2: 2},
    2: {1: 1},
    1: {3: 3}
}

# Weighted shortest paths
dist, path = dijkstra(graph, 0)
print("Dijkstra to 3:", dist[3], path[3])   # 6, [0, 2, 1, 3]

# Unweighted shortest hops
hops, bpath = bfs_shortest_hops(graph, 0)
print("BFS hops to 3:", hops[3], bpath[3])  # 3, [0, 2, 1, 3]

### CLI Example

python test.py data/example2.txt

Example `example2.txt` file:

8
0 1 5
0 2 2
2 1 1
1 3 3

## Project Layout

data/                  # example graph files
pics/                  # diagrams and images
src/
  graphs_snakkattack/
    __init__.py
    heapq.py
    sp.py
test.py                # CLI runner
pyproject.toml         # build configuration
README.md              # project documentation

## Development Workflow

- Active development happens on the `dev` branch  
- The `main` branch is **protected**  
- Workflow:
  1. Create a feature branch from `dev`
  2. Commit your changes
  3. Open a Pull Request into `dev`
  4. Merge into `main` via PR  

## Assignment Rubric Checklist

- [x] GitHub repository has `main` (protected) and `dev` branches  
- [x] README explains the library, install, usage  
- [x] Library installable via `pip` and usable  
- [x] Bonus: BFS shortest hops  

## License

MIT License © 2025 Gage Gunn
