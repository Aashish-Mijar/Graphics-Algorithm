import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, color):
    """Plot 8 symmetric points of a circle"""
    plt.plot([xc+x, xc-x, xc+x, xc-x, xc+y, xc-y, xc+y, xc-y],
             [yc+y, yc+y, yc-y, yc-y, yc+x, yc+x, yc-x, yc-x],
             'o', color=color)

def midpoint_circle(xc, yc, r, color='blue', label=None):
    """Midpoint Circle Drawing Algorithm"""
    x = 0
    y = r
    p = 1 - r
    plt.plot([], [], color=color, label=label)  # for legend

    plot_circle_points(xc, yc, x, y, color)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y, color)


# --- VARIATIONS DEMO ---
plt.figure(figsize=(8, 8))
plt.title("Midpoint Circle Drawing Algorithm Variations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Circle variations
midpoint_circle(0, 0, 10, 'red', 'Circle 1 (center: 0,0 | r=10)')
midpoint_circle(15, 10, 5, 'green', 'Circle 2 (center: 15,10 | r=5)')
midpoint_circle(-10, -5, 8, 'blue', 'Circle 3 (center: -10,-5 | r=8)')
