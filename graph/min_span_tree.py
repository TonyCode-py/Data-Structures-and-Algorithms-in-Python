import numpy as np


g = np.array([[0, 8, 5, 9, 12, 14, 12, 16, 17, 22],
              [8, 0, 9, 15, 16, 8, 11, 18, 14, 22],
              [5, 9, 0, 7, 9, 11, 7, 12, 12, 17],
              [9, 15, 7, 0, 3, 17, 10, 7, 15, 15],
              [12, 16, 9, 3, 0, 8, 10, 6, 15, 15],
              [14, 8, 11, 17, 8, 0, 9, 14, 8, 16],
              [12, 11, 7, 10, 10, 9, 0, 8, 6, 11],
              [16, 18, 12, 7, 6, 14, 8, 0, 11, 11],
              [17, 14, 12, 25, 15, 8, 6, 11, 0, 10],
              [22, 22, 17, 15, 15, 16, 11,11, 10, 0]])
n = g.shape[0]
nodes = list(range(n))
edges = {}
for i in range(n):
    for j in range(n):
        if g[i,j] > 0:
            edges[(i,j)] = g[i,j]

def find_parent(i, parent):
    if i != parent[i]:
        parent[i] = find_parent(parent[i], parent)
    return parent[i]

def kruskal(g, nodes, edges):
    n = len(nodes)
    count = n
    sorted_edges = sorted(edges.items(), key=lambda item:item[1])
    parent = list(range(n))
    minimum_spanning_tree_cost = 0
    minimum_spanning_tree = []
    for edge in sorted_edges:
        node2, w = edge
        i,j = node2
        parent_a = find_parent(i, parent)
        parent_b = find_parent(j, parent)
        if parent_a != parent_b:
            minimum_spanning_tree_cost +=w
            minimum_spanning_tree.append(edge)
            parent[parent_a] = parent_b
            count += 1
            if count == n-1:
                break
    return minimum_spanning_tree, minimum_spanning_tree_cost

def prim(g, nodes, edges):
    n = len(nodes)
    sorted_edges = sorted(edges.items(), key=lambda item:item[1])
    candidate_nodes = nodes.copy()
    selected_nodes = []
    minimum_spanning_tree_cost = 0
    minimum_spanning_tree = []
    selected_nodes.append(0)
    candidate_nodes.remove(0)
    
    while len(candidate_nodes) > 0:
        begin, end, minweight = 0, 0, 999999
        for i in selected_nodes:
            for j in candidate_nodes:
                if g[i][j] < minweight:
                    minweight = g[i][j]
                    begin = i
                    end = j
        minimum_spanning_tree_cost += minweight
        minimum_spanning_tree.append(((begin,end), minweight))
        selected_nodes.append(end)
        candidate_nodes.remove(end)
    return minimum_spanning_tree, minimum_spanning_tree_cost
    
mstree, cost = kruskal(g, nodes, edges)
mstree2, cost2 = prim(g, nodes, edges)
