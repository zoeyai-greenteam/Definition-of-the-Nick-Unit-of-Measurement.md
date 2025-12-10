import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    """Continuous logistic map: x_n+1 = r * x_n * (1 - x_n)"""
    return r * x * (1 - x)

def floor_logistic_map(r, x):
    """Floor logistic map: applies floor to result"""
    return np.floor(4 * x * (1 - x))

def generate_logistic_sequence(map_func, r, x0, n_iterations):
    """Generate sequence of values from iterating a map function"""
    values = [x0]
    x = x0
    for _ in range(n_iterations):
        x = map_func(r, x)
        values.append(x)
    return values

def plot_logistic_maps():
    """Generate all logistic map visualizations"""
    fig = plt.figure(figsize=(16, 10))

    # Parameters
    r = 4
    n_iterations = 50

    # Plot 1: Continuous Logistic Map
    ax1 = plt.subplot(2, 2, 1)
    x0_continuous = 0.4
    continuous_values = generate_logistic_sequence(logistic_map, r, x0_continuous, n_iterations)
    ax1.plot(range(len(continuous_values)), continuous_values, 'o-', linewidth=1, markersize=4)
    ax1.set_xlabel('Iteration', fontsize=12)
    ax1.set_ylabel('x_n', fontsize=12)
    ax1.set_title(f'Continuous Logistic Map (r={r}, x₀={x0_continuous})', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # Plot 2: Floor-Logistic Map
    ax2 = plt.subplot(2, 2, 2)
    x0_floor = 0.5
    floor_values = generate_logistic_sequence(floor_logistic_map, r, x0_floor, 20)
    ax2.plot(range(len(floor_values)), floor_values, 'o-', color='red', linewidth=1, markersize=8)
    ax2.set_xlabel('Iteration', fontsize=12)
    ax2.set_ylabel('x_n', fontsize=12)
    ax2.set_title(f'Floor-Logistic Map (r={r}, x₀={x0_floor})', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)

    # Plot 3: Floor-Logistic Map Long-term Behavior
    ax3 = plt.subplot(2, 2, 3)
    x0_range = np.linspace(0, 1, 1000)
    long_term_values = []
    for x0 in x0_range:
        # Iterate many times to reach steady state
        x = x0
        for _ in range(1000):
            x = floor_logistic_map(r, x)
        long_term_values.append(x)
    ax3.plot(x0_range, long_term_values, ',', color='black', markersize=0.5)
    ax3.set_xlabel('Initial Condition x₀', fontsize=12)
    ax3.set_ylabel('Long-term Values', fontsize=12)
    ax3.set_title('Floor-Logistic Map: Long-term Behavior', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.set_ylim(-0.05, 0.05)

    # Plot 4: Map Functions Comparison
    ax4 = plt.subplot(2, 2, 4)
    x_range = np.linspace(0, 1, 1000)
    continuous_map = 4 * x_range * (1 - x_range)
    floor_map = np.floor(4 * x_range * (1 - x_range))
    ax4.plot(x_range, continuous_map, label='Continuous: 4x(1-x)', linewidth=2)
    ax4.plot(x_range, floor_map, label='Floor: ⌊4x(1-x)⌋', linewidth=2, color='red')
    ax4.plot(x_range, x_range, '--', label='y=x', color='gray', linewidth=1)
    ax4.set_xlabel('x_n', fontsize=12)
    ax4.set_ylabel('x_{n+1}', fontsize=12)
    ax4.set_title('Map Functions Comparison', fontsize=14, fontweight='bold')
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('logistic_maps_comparison.png', dpi=300, bbox_inches='tight')
    print("Saved: logistic_maps_comparison.png")
    plt.close()

if __name__ == "__main__":
    plot_logistic_maps()
