from networkx import DiGraph
from vrpy import VehicleRoutingProblem
import create_graph_osdm

matrice = create_graph_osdm.get_graph_destinations()
l = len(matrice[:][0])

G = DiGraph()
for i in range(l):
    for j in range(l):
        G.add_edge(i,j,cost = matrice[i,j])

prob = VehicleRoutingProblem(G)
prob.solve()
print(prob.best_value)
print(prob.best_routes)