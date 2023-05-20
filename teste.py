import json
import networkx as nx
import matplotlib.pyplot as plt

# Read the JSON file
with open('foda.json', 'r') as file:
    data = json.load(file)

# Create a directed graph
G = nx.DiGraph()

# Function to recursively traverse the JSON data and create nodes and edges
def traverse_json(graph, node, parent=None):
    if isinstance(node, dict):
        for key, value in node.items():
            child_key = f"{key} ({type(value).__name__})"
            graph.add_node(child_key)
            if parent:
                graph.add_edge(parent, child_key)
            traverse_json(graph, value, child_key)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            child_key = f"item{index} ({type(item).__name__})"
            graph.add_node(child_key)
            if parent:
                graph.add_edge(parent, child_key)
            traverse_json(graph, item, child_key)
    else:
        graph.add_node(node)
        if parent:
            graph.add_edge(parent, node)

# Create the graph
traverse_json(G, data)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, k=0.3)
nx.draw_networkx(G, pos, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', edge_color='gray', arrows=True, width=0.5)
nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')

# Remove axes
plt.axis('off')

# Display the graph
plt.show()
