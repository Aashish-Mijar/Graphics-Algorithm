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


# ====================== SCENE OBJECTS =========================
def draw_house(x, y, color):
    pixels = []

    # Base
    pixels += dda_line(x, y, x+120, y)
    pixels += dda_line(x+120, y, x+120, y-80)
    pixels += dda_line(x+120, y-80, x, y-80)
    pixels += dda_line(x, y-80, x, y)

    # Roof
    pixels += dda_line(x, y-80, x+60, y-130)
    pixels += dda_line(x+60, y-130, x+120, y-80)

    draw_pixels(pixels, color)


def draw_tree(x, y, color):
    trunk = []
    trunk += dda_line(x, y, x, y-50)
    trunk += dda_line(x+10, y, x+10, y-50)
    trunk += dda_line(x, y-50, x+10, y-50)
    draw_pixels(trunk, "brown")

    leaves = []
    leaves += midpoint_circle(x+5, y-65, 15)
    leaves += midpoint_circle(x-10, y-65, 15)
    leaves += midpoint_circle(x+20, y-65, 15)
    draw_pixels(leaves, color)


def draw_road():
    road = []
    road += dda_line(0, 300, 600, 300)
    road += dda_line(0, 340, 600, 340)
    draw_pixels(road, "black")


def draw_sun(color):
    sun = midpoint_circle(500, 80, 30)
    draw_pixels(sun, color)

    rays = []
    rays += dda_line(500, 20, 500, 130)
    rays += dda_line(440, 80, 560, 80)
    rays += dda_line(460, 40, 540, 120)
    rays += dda_line(460, 120, 540, 40)
    draw_pixels(rays, color)


# ====================== ANIMATION =============================
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
color_index = 0

def animate():
    global color_index
    canvas.delete("all")

    animated_color = colors[color_index % len(colors)]

    draw_sun(animated_color)
    draw_house(100, 300, animated_color)
    draw_house(260, 300, colors[(color_index+2) % len(colors)])
    draw_tree(60, 300, colors[(color_index+1) % len(colors)])
    draw_tree(450, 300, colors[(color_index+3) % len(colors)])
    draw_road()

    color_index += 1
    window.after(600, animate)


