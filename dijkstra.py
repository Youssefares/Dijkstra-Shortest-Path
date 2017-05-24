# from basic_types import Vertex
# from heapq import heappop, heappush, heapify
#
from print_paths import print_paths


#uses array implementation
def dijkstra(G, s):
    d = {}               # node distances from source
    predecessor = {}     # node predecessor on the shortest path

    #initing distances to INF for all but source.
    for v in G:
        if v == s:
            d[v] = 0
        else:
            d[v] = float("inf")

    predecessor[s] = None

    Q = list(G.keys())   # contains all nodes to find shortest paths to, intially everything.
    while(Q):                            # until there is nothing left in Q
        u = min(Q, key = d.get)          # get min distance node
        Q.remove(u)
        for v in G[u]:                   # relax all outgoing edges from it
            relax(u, v, d, predecessor)

    print(d)
    print_paths(predecessor)


def relax(u, v, d, predecessor):
    weight = v[1]
    v = v[0]
    if d[v] > d[u] + weight:
        d[v] = d[u] + weight
        predecessor[v] = u



G = {
"a": [("b", 10), ("c", 3)],
"b": [("c",  1), ("d", 2)],
"c": [("b",  4), ("d", 8), ("e", 2)],
"d": [("e",  7)],
"e": [("d",  9)]
}

dijkstra(G, "e")
