import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def mandelbrot(c, max_iter=100):
    """
    Calculate the number of iterations for a complex number c
    in the Mandelbrot set
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_mandelbrot(xmin, xmax, ymin, ymax, width=800, height=800, max_iter=100):
    """
    Generate a Mandelbrot set image for a given region
    """
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)

    mandelbrot_set = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            mandelbrot_set[i, j] = mandelbrot(c, max_iter)

    return mandelbrot_set

def create_mandelbrot_visualizations():
    """Create three different Mandelbrot set visualizations"""

    # Create custom colormap (yellow on black like the images)
    colors = ['black', 'darkblue', 'blue', 'cyan', 'yellow', 'white']
    n_bins = 256
    cmap = LinearSegmentedColormap.from_list('mandelbrot', colors, N=n_bins)

    # Visualization 1: Full Mandelbrot set
    print("Generating full Mandelbrot set...")
    mandelbrot1 = generate_mandelbrot(-2.5, 1.5, -2, 2, width=800, height=800, max_iter=256)

    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot1, extent=[-2.5, 1.5, -2, 2], cmap=cmap, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('mandelbrot_full.png', dpi=150, bbox_inches='tight', pad_inches=0, facecolor='black')
    print("Saved: mandelbrot_full.png")
    plt.close()

    # Visualization 2: Zoom into edge detail
    print("Generating zoomed Mandelbrot (edge detail)...")
    mandelbrot2 = generate_mandelbrot(-0.8, 0.2, -0.2, 0.8, width=800, height=800, max_iter=512)

    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot2, extent=[-0.8, 0.2, -0.2, 0.8], cmap=cmap, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('mandelbrot_zoom1.png', dpi=150, bbox_inches='tight', pad_inches=0, facecolor='black')
    print("Saved: mandelbrot_zoom1.png")
    plt.close()

    # Visualization 3: Deep zoom into the set
    print("Generating deep zoom Mandelbrot...")
    mandelbrot3 = generate_mandelbrot(-0.7, -0.4, -0.15, 0.15, width=800, height=800, max_iter=1024)

    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot3, extent=[-0.7, -0.4, -0.15, 0.15], cmap=cmap, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('mandelbrot_zoom2.png', dpi=150, bbox_inches='tight', pad_inches=0, facecolor='black')
    print("Saved: mandelbrot_zoom2.png")
    plt.close()

    # Visualization 4: Classic Mandelbrot view (main cardioid and bulb)
    print("Generating classic Mandelbrot view...")
    mandelbrot4 = generate_mandelbrot(-2.0, 0.5, -1.25, 1.25, width=1000, height=1000, max_iter=256)

    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot4, extent=[-2.0, 0.5, -1.25, 1.25], cmap=cmap, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('mandelbrot_classic.png', dpi=150, bbox_inches='tight', pad_inches=0, facecolor='black')
    print("Saved: mandelbrot_classic.png")
    plt.close()

if __name__ == "__main__":
    create_mandelbrot_visualizations()
