import matplotlib.pyplot as plt

# --- 2D Illustration ---
plt.figure(figsize=(7, 7))
plt.title("2D Illustration Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Draw 2D shapes
# Line
plt.plot([0, 5], [0, 5], color='red', label='Line')

# Rectangle
rect_x = [1, 4, 4, 1, 1]
rect_y = [1, 1, 3, 3, 1]
plt.plot(rect_x, rect_y, color='blue', label='Rectangle')

# Circle (using parametric form)
import numpy as np
theta = np.linspace(0, 2*np.pi, 100)
x_circle = 2 + np.cos(theta)
y_circle = 5 + np.sin(theta)
plt.plot(x_circle, y_circle, color='green', label='Circle')

# Text labels
plt.text(5, 5, "Line", color='red')
plt.text(2.5, 2, "Rectangle", color='blue')
plt.text(2, 6, "Circle", color='green')

plt.legend()
plt.axis('equal')
plt.show()
