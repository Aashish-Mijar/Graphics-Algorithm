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



# -----------------------------------
# GUI IMPLEMENTATION
# -----------------------------------

class PolygonClipGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sutherland–Hodgman Polygon Clipping - GUI Model")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.points = []
        self.clipped_polygon = []
        self.clipping_window = None
        self.start_rect = None

        # Buttons
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Button(frame, text="Draw Polygon (click)", command=self.enable_polygon).pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Draw Clipping Window (drag)", command=self.enable_window).pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Clip Polygon", command=self.perform_clipping).pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Clear All", command=self.clear_all).pack(side=tk.LEFT, padx=10)

        self.mode = None

        # Bind events
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def enable_polygon(self):
        self.mode = "POLYGON"

    def enable_window(self):
        self.mode = "WINDOW"

    def on_click(self, event):
        if self.mode == "POLYGON":
            self.points.append([event.x, event.y])
            if len(self.points) > 1:
                self.canvas.create_line(self.points[-2][0], self.points[-2][1],
                                        self.points[-1][0], self.points[-1][1],
                                        fill="blue", width=2)

        elif self.mode == "WINDOW":
            self.start_rect = (event.x, event.y)
