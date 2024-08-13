import matplotlib.pyplot as plt
import numpy as np

class Triangle_shape:
    def __init__(self, l: int, b: int, h: int):
        self.l = l  # Length (side along the y-axis)
        self.b = b  # Breadth (side along the x-axis)
        self.h = h  # Hypotenuse

    def calculate_vertices(self):
        """Calculate the vertices of the triangle based on side lengths."""
        # Assuming the right triangle:
        # Vertex A at (0, 0)
        # Vertex B at (b, 0) for the base
        # Vertex C at (0, l) for the height
        self.vertices = np.array([[0, 0], [self.b, 0], [0, self.l]])

    def plot_triangle(self):
        """Plot the triangle using Matplotlib."""
        self.calculate_vertices()

        # Create a new figure
        plt.figure()

        # Create a polygon representing the triangle
        triangle = plt.Polygon(self.vertices, fill=True, edgecolor='blue', facecolor='lightblue')

        # Add the triangle to the plot
        plt.gca().add_patch(triangle)

        # Set the x and y limits of the plot
        plt.xlim(-1, max(self.b, self.l) + 1)
        plt.ylim(-1, max(self.b, self.l) + 1)

        # Set aspect ratio to be equal
        plt.gca().set_aspect('equal', adjustable='box')

        # Adding grid for better visualization
        plt.grid(True)

        # Display the triangle
        plt.show()

# Example usage:
# triangle = Triangle_shape(3, 4, 5)
# triangle.plot_triangle()
