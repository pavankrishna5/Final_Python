import networkx as net
import matplotlib.pyplot as plt
g = net.read_pajek('pajek.net')
print("Find the number of nodes in the graph?")
print ("Nodes: ",len(g))
print("###################################################################")
print("Find the number of components (connected subgraphs)?")
print ("Number of components (Connected Subgraphs): ",len(list(net.connected_component_subgraphs(g))))
print ("Number of components (Connected Subgraphs): ",net.number_connected_components(g))
print("###################################################################")
print("Find the node with the maximum degree? What is that degree?")
deg = net.degree(g)
print("Node with Maximum Degree: ", max(deg, key=deg.get))
print("Maximum Degree: ", max(deg.values()))
print("###################################################################")
print("Convert the graph to an undirected graph. What is the number of edges?")
undirected = g.to_undirected()
print ('Number of edges for undirected graph: ',len(undirected.edges()))
print("###################################################################")
print("What is the density of the graph?")
print ("Density of the Graph: ",net.density(g))
print("###################################################################")
print("Create a degree distribution plot?")
print("There will be pop up window with the graph if you run the code")
degs = {}
for n in g.nodes():
    deg = g.degree(n)
    if deg not in degs:
        degs [ deg ] = 0
    degs [ deg ] += 1
items = sorted(degs.items())
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot ([k for (k ,v) in items],[v for (k ,v ) in items])
plt.title('Degree Distribution')
plt.ylabel("Count")
plt.xlabel("Degree")
plt.show()