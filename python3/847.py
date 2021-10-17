from collections import deque
from typing import NamedTuple

class Journey(NamedTuple):
    vertices: tuple[int, ...]
    visited: frozenset[int]
    @classmethod
    def from_start(cls, vertex: int) -> "Journey":
        vs = (vertex,)
        return cls(vs, frozenset(vs))
    def add(self, vertex: int) -> "Journey":
        return Journey((*self.vertices, vertex), self.visited | {vertex})
    def __len__(self) -> int:
        return len(self.vertices) - 1
    def last(self) -> int:
        return self.vertices[-1]
    def state(self) -> tuple[int, frozenset[int]]:
        return (self.last(), self.visited)

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        all_vertices = frozenset(range(len(graph)))
        # initialize journeys with starting vertices
        journeys = deque(map(Journey.from_start, all_vertices))
        # initialize visited_states with starting journeys
        visited_states = set(j.state() for j in journeys)
        # advance journeys breadth-first until the first that visits every vertex is found
        while True:
            j = journeys.popleft()
            if j.visited == all_vertices:
                return len(j)
            for v in graph[j.last()]:
                k = j.add(v)
                if k.state() not in visited_states:
                    visited_states.add(k.state())
                    journeys.append(k)
