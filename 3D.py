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


