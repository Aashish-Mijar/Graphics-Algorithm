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

