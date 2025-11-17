# Point Clipping Program in Python

# Define clipping window boundaries
xmin = float(input("Enter xmin: "))
ymin = float(input("Enter ymin: "))
xmax = float(input("Enter xmax: "))
ymax = float(input("Enter ymax: "))


# Input the point to be clipped
x = float(input("Enter x-coordinate of the point: "))
y = float(input("Enter y-coordinate of the point: "))

# Function to check if the point is inside the clipping window
def is_point_visible(x, y, xmin, ymin, xmax, ymax):
    if xmin <= x <= xmax and ymin <= y <= ymax:
        return True
    else:
        return False

