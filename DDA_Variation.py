import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2, color='blue', label='DDA Line'):
    """Draws a line using DDA Algorithm"""
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    x_points = []
    y_points = []

    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    plt.plot(x_points, y_points, color=color, marker='o', label=label)
    plt.text(x2, y2, f"({x2},{y2})", fontsize=8, color=color)
    return x_points, y_points


# Example variations
plt.figure(figsize=(8, 8))
plt.title("DDA Line Drawing Algorithm Variations")



