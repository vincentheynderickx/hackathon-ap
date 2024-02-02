#%%
import create_graph_osdm
import numpy as np
import sys
import osmnx
import matplotlib.pyplot as plt


#%%

matrice, routes = create_graph_osdm.get_graph_destinations()



def tsp(graph):
    n = len(graph)
    
    # Memoization table
    memo = {}

    # Helper function to compute the optimal tour starting from node 0
    def tsp_helper(mask, current):
        if (mask, current) in memo:
            return memo[(mask, current)]

        # If all nodes have been visited, return the distance to the starting node
        if mask == (1 << n) - 1:
            return graph[current][0], [0]

        # Try all possible next nodes and find the minimum distance
        min_distance = float('inf')
        optimal_path = []

        for next_node in range(1, n):
            if (mask >> next_node) & 1 == 0:
                distance, path = tsp_helper(mask | (1 << next_node), next_node)
                distance += graph[current][next_node]

                if distance < min_distance:
                    min_distance = distance
                    optimal_path = [current] + path

        memo[(mask, current)] = (min_distance, optimal_path)
        return min_distance, optimal_path

    # Start from node 0
    distance, optimal_path = tsp_helper(1, 0)
    
    return distance, optimal_path
    

distance, path_num = tsp(matrice)

all_destinations = {**create_graph_osdm.station, **create_graph_osdm.destinations}

path = [create_graph_osdm.conversion_index_name[i] for i in path_num]

routes = [routes[(path[i], path[i+1])] for i in range(len(path)-1)]

osmnx.plot_graph_route(create_graph_osdm.G2, routes[0], route_linewidth=6, node_size=0, bgcolor='k')


# %%
