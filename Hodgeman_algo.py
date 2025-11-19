import tkinter as tk

# -----------------------------------
# SUTHERLAND–HODGMAN CLIPPING LOGIC
# -----------------------------------

def inside(p, edge, xmin, ymin, xmax, ymax):
    x, y = p
    if edge == "LEFT":   return x >= xmin
    if edge == "RIGHT":  return x <= xmax
    if edge == "BOTTOM": return y >= ymin
    if edge == "TOP":    return y <= ymax

def intersection(p1, p2, edge, xmin, ymin, xmax, ymax):
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        m = None
    else:
        m = (y2 - y1) / (x2 - x1)

    if edge == "LEFT":
        x = xmin
        y = y1 + (xmin - x1) * m if m is not None else y1
    elif edge == "RIGHT":
        x = xmax
        y = y1 + (xmax - x1) * m if m is not None else y1
    elif edge == "BOTTOM":
        y = ymin
        x = x1 + (ymin - y1) / m if m is not None else x1
    elif edge == "TOP":
        y = ymax
        x = x1 + (ymax - y1) / m if m is not None else x1

    return [x, y]

def clip_polygon(poly, edge, xmin, ymin, xmax, ymax):
    clipped = []
    n = len(poly)

    for i in range(n):
        curr = poly[i]
        prev = poly[i - 1]

        curr_in = inside(curr, edge, xmin, ymin, xmax, ymax)
        prev_in = inside(prev, edge, xmin, ymin, xmax, ymax)

        if prev_in and curr_in:
            clipped.append(curr)

        elif prev_in and not curr_in:
            clipped.append(intersection(prev, curr, edge, xmin, ymin, xmax, ymax))

        elif not prev_in and curr_in:
            clipped.append(intersection(prev, curr, edge, xmin, ymin, xmax, ymax))
            clipped.append(curr)

    return clipped


