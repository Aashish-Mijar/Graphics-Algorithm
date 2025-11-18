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

def visualize_clipping():
    """Create interactive visualization of Cohen-Sutherland algorithm"""
    fig, ax = plt.subplots(figsize=(12, 10))
    plt.subplots_adjust(bottom=0.3)
    
    # Clipping window
    x_min, x_max = 2, 8
    y_min, y_max = 2, 8
    
    # Initial line coordinates
    x1, y1 = 1, 1
    x2, y2 = 9, 9
    
    # Create clipping window rectangle
    clip_rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, 
                                 linewidth=2, edgecolor='blue', facecolor='lightblue', alpha=0.3)
    ax.add_patch(clip_rect)
    
    # Plot region codes
    ax.text(0.5, 0.5, '1001', fontsize=10, ha='center', va='center', color='red')
    ax.text(5, 0.5, '1000', fontsize=10, ha='center', va='center', color='red')
    ax.text(9.5, 0.5, '1010', fontsize=10, ha='center', va='center', color='red')
    
    ax.text(0.5, 5, '0001', fontsize=10, ha='center', va='center', color='red')
    ax.text(5, 5, '0000', fontsize=10, ha='center', va='center', color='red')
    ax.text(9.5, 5, '0010', fontsize=10, ha='center', va='center', color='red')
    
    ax.text(0.5, 9.5, '0101', fontsize=10, ha='center', va='center', color='red')
    ax.text(5, 9.5, '0100', fontsize=10, ha='center', va='center', color='red')
    ax.text(9.5, 9.5, '0110', fontsize=10, ha='center', va='center', color='red')
    
    # Draw the original line
    original_line, = ax.plot([x1, x2], [y1, y2], 'ro-', linewidth=2, markersize=8, label='Original Line')
    
    # Draw the clipped line (initially hidden)
    clipped_line, = ax.plot([], [], 'go-', linewidth=3, markersize=10, label='Clipped Line')
    
    # Set plot properties
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Cohen-Sutherland Line Clipping Algorithm')
    ax.legend()
    
    # Add text information
    info_text = ax.text(0.02, 0.98, '', transform=ax.transAxes, verticalalignment='top',
                       bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # Update function for the visualization
    def update_visualization():
        accept, clipped_coords, all_steps = cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max)
        
        # Update original line
        original_line.set_data([x1, x2], [y1, y2])
        
        # Update clipped line
        if accept:
            cx1, cy1, cx2, cy2 = clipped_coords
            clipped_line.set_data([cx1, cx2], [cy1, cy2])
            clipped_line.set_visible(True)
            info_text.set_text(f'Line Accepted!\nClipped: ({cx1:.2f}, {cy1:.2f}) to ({cx2:.2f}, {cy2:.2f})')
        else:
            clipped_line.set_visible(False)
            info_text.set_text('Line Rejected!')
        
        # Draw intermediate steps
        for i, step in enumerate(all_steps):
            sx1, sy1, sx2, sy2 = step
            if i == 0:
                # Original line
                ax.plot([sx1, sx2], [sy1, sy2], 'ro-', alpha=0.3, linewidth=1)
            else:
                # Intermediate steps
                ax.plot([sx1, sx2], [sy1, sy2], 'mo-', alpha=0.5, linewidth=1, markersize=4)
        
        plt.draw()
    
    