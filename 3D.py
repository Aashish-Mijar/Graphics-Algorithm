from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# --- 3D Illustration ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("3D Illustration Example")

# Draw coordinate axes
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Plot 3D line
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)
z = np.linspace(0, 5, 100)
ax.plot(x, y, z, color='red', label='3D Line')

# Plot a 3D surface (curved plane)
X = np.linspace(-3, 3, 50)
Y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, label='3D Surface')

# Plot a 3D scatter sphere
phi = np.linspace(0, np.pi, 20)
theta = np.linspace(0, 2*np.pi, 40)
X = np.outer(np.sin(phi), np.cos(theta))
Y = np.outer(np.sin(phi), np.sin(theta))
Z = np.outer(np.cos(phi), np.ones_like(theta))
ax.plot_wireframe(X, Y, Z, color='blue', label='Sphere')

