
import numpy as np
import itertools as it
import networkx as nx
import matplotlib.pyplot as plt


xi =  [0, 2, 5, 7]
yi = [0, 3, 5, 7]

homes = [(0, 0), (0, 3), (0, 5), (0, 6), (0, 7), (1, 0), (1, 3), (1, 5), (1, 7), (2, 1), (2, 3), (2, 4),
                      (2, 5), (2, 6), (2, 7), (3, 0), (4, 3), (4, 7), (5, 0), (5, 1), (5, 3), (5, 4), (5, 5), (5, 7),
                      (6, 0), (6, 5), (6, 7), (7, 0), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]

r = len(yi)
c = len(xi)


a = [[(xi[i],yi[j]) for i in range(c)] for j in range(r)] 
print(a)

for b in a:
    print(b)

