import itertools as it
import networkx as nx
import matplotlib.pyplot as plt

def count_paper_streets(x_intercepts, y_intercepts, homes):

    xi =  x_intercepts
    yi = y_intercepts
    hm = homes

    r = len(yi)
    c = len(xi)

    G = nx.Graph()

    for j in range(r):
        for i in range(c):
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            node = (xi[i],yi[j]) 
            for dir in dirs:
                idx = [i + dir[0], j + dir[1]]
                if 0 <= idx[0] < c and 0 <= idx[1] < r:
                    neighbor = (xi[idx[0]],yi[idx[1]])
                    G.add_edge(node,neighbor,color='b')

    def between(u,v,h): 

        if h == u or h == v:
            return False

        xs = [u[0], v[0]]
        ys = [u[1], v[1]]

        if min(xs)<=h[0]<=max(xs) and min(ys)<=h[1]<=max(ys): 
            return True
        else: 
            return False


    for u, v in list(G.edges):
        for h in hm:
            if between(u,v,h):
                G.remove_edge(u,v)
                hm.remove(h)
                break

    ans = len([c for c in list(nx.connected_components(G)) if len(c)>1])

    return ans
