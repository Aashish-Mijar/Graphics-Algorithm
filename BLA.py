import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2, color='blue', label='BLA Line'):
    """Draws a line using Bresenham's Line Drawing Algorithm"""
    x_points = []
    y_points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    while True:
        x_points.append(x1)
        y_points.append(y1)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    plt.plot(x_points, y_points, color=color, marker='o', label=label)
    plt.text(x2, y2, f"({x2},{y2})", fontsize=8, color=color)

# Plot multiple variations
plt.figure(figsize=(8, 8))
plt.title("Bresenham's Line Drawing Algorithm Variations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)


# Different coordinates for variations
bresenham_line(0, 0, 5, 5, 'red', 'Line 1 (Diagonal)')
bresenham_line(2, 3, 10, 3, 'green', 'Line 2 (Horizontal)')
bresenham_line(3, 2, 3, 10, 'blue', 'Line 3 (Vertical)')
bresenham_line(1, 1, 8, 4, 'orange', 'Line 4 (Shallow Slope)')
bresenham_line(2, 8, 6, 3, 'purple', 'Line 5 (Negative Slope)')

plt.legend()
plt.axis('equal')
plt.show()
plt.show()

