"""
Graph using adjacency list.
Algorithms:
- BFS / DFS: O(V + E)
- Dijkstra (binary heap): O(E log V)


PT-BR resumo:
- Representação por lista de adjacência com pesos opcionais (default = 1.0).
"""
from __future__ import annotations
from collections import deque
from typing import Dict, List, Tuple, Iterable
import heapq




class Graph:
def __init__(self) -> None:
# adjacency: node -> list[(neighbor, weight)]
self.adj: Dict[str, List[Tuple[str, float]]] = {}


def add_node(self, v: str) -> None:
self.adj.setdefault(v, [])


def add_edge(self, u: str, v: str, w: float = 1.0, undirected: bool = True) -> None:
self.add_node(u)
self.add_node(v)
self.adj[u].append((v, w))
if undirected:
self.adj[v].append((u, w))


def nodes(self) -> Iterable[str]:
return self.adj.keys()


# ---------- BFS ----------
def bfs(self, start: str) -> List[str]:
visited = set([start])
q = deque([start])
order: List[str] = []
while q:
u = q.popleft()
order.append(u)
for v, _ in self.adj.get(u, []):
if v not in visited:
visited.add(v)
q.append(v)
return order


# ---------- DFS ----------
def dfs(self, start: str) -> List[str]:
visited = set()
order: List[str] = []
def _dfs(u: str):
visited.add(u)
order.append(u)
for v, _ in self.adj.get(u, []):
if v not in visited:
_dfs(v)
if start in self.adj:
_dfs(start)
return order


# ---------- Dijkstra ----------
def dijkstra(self, source: str) -> Dict[str, float]:
dist: Dict[str, float] = {v: float('inf') for v in self.adj}
dist[source] = 0.0
pq: List[Tuple[float, str]] = [(0.0, source)]
while pq:
d, u = heapq.heappop(pq)
if d > dist[u]:
continue
for v, w in self.adj.get(u, []):
nd = d + w
if nd < dist[v]:
dist[v] = nd
heapq.heappush(pq, (nd, v))
return dist
