import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def create_random_graph(n_nodes=30, edge_probability=0.15):
    """Create a random graph using Erdős-Rényi model"""
    G = nx.erdos_renyi_graph(n_nodes, edge_probability, seed=42)
    return G

def create_adjacency_matrix(G):
    """Get adjacency matrix from graph"""
    return nx.to_numpy_array(G)

def create_wave_function_matrix(size=100):
    """Create a wave function visualization matrix"""
    x = np.linspace(-3, 3, size)
    y = np.linspace(-3, 3, size)
    X, Y = np.meshgrid(x, y)

    # Create wave interference pattern
    Z = np.sin(np.sqrt(X**2 + Y**2)) * np.cos(X) * np.cos(Y)
    Z += np.sin(2*np.sqrt((X-1)**2 + (Y-1)**2)) * 0.5
    Z += np.sin(2*np.sqrt((X+1)**2 + (Y+1)**2)) * 0.5

    return Z

def plot_matrix_visualizations():
    """Create all matrix and graph visualizations"""

    # Set style for green-on-black theme
    plt.style.use('dark_background')

    fig = plt.figure(figsize=(16, 16), facecolor='black')
    fig.suptitle('Matrix Graph Visualizations', fontsize=20, color='lime', fontweight='bold', y=0.995)

    # Create graph
    G = create_random_graph(n_nodes=30, edge_probability=0.15)
    adj_matrix = create_adjacency_matrix(G)

    # Plot 1: Adjacency Matrix
    ax1 = plt.subplot(2, 2, 1)
    im1 = ax1.imshow(adj_matrix, cmap='Greens', interpolation='nearest')
    ax1.set_title('Adjacency Matrix', fontsize=14, color='lime', pad=10)
    ax1.set_xlabel('Node j', fontsize=11, color='lime')
    ax1.set_ylabel('Node i', fontsize=11, color='lime')
    ax1.tick_params(colors='lime')

    # Plot 2: Network Graph Structure
    ax2 = plt.subplot(2, 2, 2)
    pos = nx.spring_layout(G, seed=42, k=0.5, iterations=50)
    nx.draw_networkx_nodes(G, pos, node_color='lime', node_size=300, ax=ax2)
    nx.draw_networkx_edges(G, pos, edge_color='lime', width=0.5, alpha=0.6, ax=ax2)
    ax2.set_title('Network Graph Structure', fontsize=14, color='lime', pad=10)
    ax2.axis('off')
    ax2.set_facecolor('black')

    # Plot 3: Wave Function Matrix
    ax3 = plt.subplot(2, 2, 3)
    wave_matrix = create_wave_function_matrix(100)
    im3 = ax3.imshow(wave_matrix, cmap='Greens', interpolation='bilinear',
                     extent=[-3, 3, -3, 3])
    ax3.set_title('Wave Function Matrix', fontsize=14, color='lime', pad=10)
    ax3.set_xlabel('x', fontsize=11, color='lime')
    ax3.set_ylabel('y', fontsize=11, color='lime')
    ax3.tick_params(colors='lime')

    # Plot 4: Circular Correlation Graph
    ax4 = plt.subplot(2, 2, 4)
    # Create a smaller graph for circular layout
    G_circular = create_random_graph(n_nodes=12, edge_probability=0.25)
    pos_circular = nx.circular_layout(G_circular)

    # Draw edges with varying transparency based on edge weight
    edges = G_circular.edges()
    nx.draw_networkx_edges(G_circular, pos_circular, edgelist=edges,
                          edge_color='lime', width=1.5, alpha=0.6, ax=ax4)

    # Draw nodes
    nx.draw_networkx_nodes(G_circular, pos_circular, node_color='lime',
                          node_size=500, ax=ax4)

    # Draw labels
    nx.draw_networkx_labels(G_circular, pos_circular, font_color='black',
                           font_weight='bold', font_size=10, ax=ax4)

    ax4.set_title('Circular Correlation Graph', fontsize=14, color='lime', pad=10)
    ax4.axis('off')
    ax4.set_facecolor('black')

    plt.tight_layout()
    plt.savefig('matrix_graph_visualizations.png', dpi=200, bbox_inches='tight',
                facecolor='black', edgecolor='none')
    print("Saved: matrix_graph_visualizations.png")
    plt.close()

    # Reset style
    plt.style.use('default')

if __name__ == "__main__":
    plot_matrix_visualizations()
