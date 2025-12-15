import tkinter as tk

# ===================== DDA LINE ALGORITHM =====================
def dda_line(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points

# ================= MIDPOINT CIRCLE ALGORITHM ==================
def midpoint_circle(xc, yc, r):
    points = []
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        points.extend([
            (xc+x, yc+y), (xc-x, yc+y),
            (xc+x, yc-y), (xc-x, yc-y),
            (xc+y, yc+x), (xc-y, yc+x),
            (xc+y, yc-x), (xc-y, yc-x)
        ])

        x += 1
        if p < 0:
            p += 2*x + 1
        else:
            y -= 1
            p += 2*(x - y) + 1

    return points

# ===================== DRAW PIXELS ============================
def draw_pixels(points, color):
    for x, y in points:
        canvas.create_rectangle(x, y, x+1, y+1, fill=color, outline=color)


