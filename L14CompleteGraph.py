import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices (greater than 3): "))

if n > 3:
    G = nx.complete_graph(n)

    nx.draw(G, with_labels=True, node_color="lightblue")
    plt.title("Complete Graph")
    plt.show()
else:
    print("Number of vertices must be greater than 3.")