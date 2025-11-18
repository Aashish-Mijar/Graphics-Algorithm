import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button, Slider
import numpy as np

# Cohen-Sutherland region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def compute_code(x, y, x_min, y_min, x_max, y_max):
    """Compute region code for point (x, y)"""
    code = INSIDE
    
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
        
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
        
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    """Implement Cohen-Sutherland line clipping algorithm"""
    code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
    code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max)
    accept = False
    
    clipped_points = [(x1, y1, x2, y2)]  # Store original line
    
    while True:
        # Both endpoints inside clipping window
        if code1 == 0 and code2 == 0:
            accept = True
            break
            
        # Both endpoints outside clipping window (same region)
        elif (code1 & code2) != 0:
            break
            
        # Some segment lies inside clipping window
        else:
            # Select endpoint outside clipping window
            code_out = code1 if code1 != 0 else code2
            
            # Find intersection point
            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min
                
            # Replace outside point with intersection point
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
                clipped_points.append((x1, y1, x2, y2))
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max)
                clipped_points.append((x1, y1, x2, y2))
    
    return accept, (x1, y1, x2, y2), clipped_points

