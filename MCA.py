import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, color):
    """Plot 8 symmetric points of a circle"""
    plt.plot([xc+x, xc-x, xc+x, xc-x, xc+y, xc-y, xc+y, xc-y],
             [yc+y, yc+y, yc-y, yc-y, yc+x, yc+x, yc-x, yc-x],
             'o', color=color)

