import itertools as it
import networkx as nx

def count_paper_streets(x_intercepts, y_intercepts, homes):

## Establish variables
    xi =  x_intercepts
    yi = y_intercepts
    hm = homes
    r = len(yi)
    c = len(xi)

## Establish function definitions

    def neighbors(i,j):
    # returns list of neighbor nodes in grid
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        neigh = []
        for dir in dirs:
            idx = [i + dir[0], j + dir[1]]
            if 0 <= idx[0] < c and 0 <= idx[1] < r:
                neigh.append((xi[idx[0]],yi[idx[1]]))
        return neigh
    
    def between(u,v,h): 
    # returns true if house loc is on edge between nodes u and v

        if h == u or h == v: # house is on intersection (not between)
            return False

        xs = [u[0], v[0]]
        ys = [u[1], v[1]]

        if min(xs)<=h[0]<=max(xs) and min(ys)<=h[1]<=max(ys): 
            return True
        else: 
            return False


## 1. Build undirected graph (nodes = intersections; edges = roads)
    G = nx.Graph()   
    for i in range(c):
        for j in range(r):
            u = (xi[i],yi[j]) 
            neigh = neighbors(i,j)
            for v in neigh:
                G.add_edge(u,v)

## 2. Remove "real" roads (edges with homes on them) from the graph
    for u, v in list(G.edges):
        for h in hm:
            if between(u,v,h):
                G.remove_edge(u,v)
                hm.remove(h)
                break

## 3. Count the # of connected components with more than 1 node
    ans = len([c for c in list(nx.connected_components(G)) if len(c)>1])
    return ans
